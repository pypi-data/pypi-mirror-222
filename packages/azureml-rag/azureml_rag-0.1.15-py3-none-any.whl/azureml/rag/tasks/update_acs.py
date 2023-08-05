# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
import base64
import json
import logging
import os
import requests
import tenacity
import time
import traceback
import yaml

from azure.identity import DefaultAzureCredential
from azure.core.credentials import AzureKeyCredential
from azure.search.documents.indexes import SearchIndexClient
from azure.search.documents.indexes.models import SearchIndex, SimpleField, SearchableField, SemanticSettings, SemanticConfiguration, PrioritizedFields, SemanticField, SearchField, ComplexField
from azure.search.documents import SearchClient
from azureml.rag.embeddings import EmbeddingsContainer
from azureml.rag.mlindex import MLIndex
from azureml.rag.utils.connections import get_connection_credential
from azureml.rag.utils.logging import get_logger, enable_stdout_logging, enable_appinsights_logging, track_activity, _logger_factory
from pathlib import Path
from typing import Optional


logger = get_logger('update_acs')

_azure_logger = logging.getLogger('azure.core.pipeline')
_azure_logger.setLevel(logging.WARNING)


def search_client_from_config(acs_config: dict, credential):
    return SearchClient(endpoint=acs_config['endpoint'],
                        index_name=acs_config['index_name'],
                        credential=credential,
                        api_version=acs_config['api_version'])


def create_search_index_sdk(acs_config: dict, credential):
    logger.info(f"Ensuring search index {acs_config['index_name']} exists")
    index_client = SearchIndexClient(endpoint=acs_config['endpoint'],
                                    credential=credential)
    if acs_config['index_name'] not in index_client.list_index_names():
        index = SearchIndex(
            name=acs_config['index_name'],
            fields=[
                SimpleField(name="id", type="Edm.String", key=True),
                SearchableField(name="content", type="Edm.String", analyzer_name="en.microsoft"),
                SimpleField(name="category", type="Edm.String", filterable=True, facetable=True),
                SimpleField(name="sourcepage", type="Edm.String", filterable=True, facetable=True),
                SimpleField(name="sourcefile", type="Edm.String", filterable=True, facetable=True),
                SimpleField(name="title", type="Edm.String", filterable=True, facetable=True),
                SimpleField(name="content_hash", type="Edm.String", filterable=True, facetable=True),
                SimpleField(name="meta_json_string", type="Edm.String", filterable=True, facetable=True)
                # TODO: Support constructing typed metadata schema, need to ensure there's consistency across file types, with a section for differing meta that is just string.
                #ComplexField(name="meta", fields=dict_to_fields()),
                # TODO: Insert embeddings once SDK supports it.
                #SearchField(name=f"embedding_vector_{emb.kind}", type="Collection(Edm.Single)", searchable=False), # dimensions=embedding_dimensions), # , retrievable=True
            ],
            semantic_settings=SemanticSettings(
                configurations=[SemanticConfiguration(
                    name='default',
                    prioritized_fields=PrioritizedFields(
                        title_field=None, prioritized_content_fields=[SemanticField(field_name='content')]))])
        )
        logger.info(f"Creating {acs_config['index_name']} search index")
        index_client.create_index(index)
    else:
        logger.info(f"Search index {acs_config['index_name']} already exists")


@tenacity.retry(
    wait=tenacity.wait_fixed(5),  # wait 5 seconds between retries
    stop=tenacity.stop_after_attempt(3),  # stop after 3 attempts
    reraise=True,  # re-raise the exception after the last retry attempt
)
def send_put_request(url, headers, payload):
    response = requests.put(url, data=json.dumps(payload), headers=headers)

    # Raise an exception if the response contains an HTTP error status code
    response.raise_for_status()
    return response


def create_search_index_rest(acs_config: dict, credential, embeddings: Optional[EmbeddingsContainer] = None):
    # TODO: Ask users in private preview to provide the new api_version? 2023-07-01-Preview
    logger.info(f"Ensuring search index {acs_config['index_name']} exists")
    if 'api_version' not in acs_config:
        acs_config['api_version'] = "2023-07-01-preview"
    index_client = SearchIndexClient(endpoint=acs_config['endpoint'],
                                    credential=credential,
                                    api_version=acs_config['api_version'])
    if acs_config['index_name'] not in index_client.list_index_names():
        base_url = f"{acs_config['endpoint']}/indexes/{acs_config['index_name']}?api-version={acs_config['api_version']}"
        headers = {
            "Content-Type": "application/json"
        }
        if isinstance(credential, DefaultAzureCredential):
            headers["Authorization"] = f"Bearer {credential.get_token('https://search.azure.com/.default').token}"
        else:
            headers["api-key"] = credential.key

        payload = {
            "name": acs_config['index_name'],
            "fields": [
                {"name": "id", "type": "Edm.String", "key": True},
                {"name": "content", "type": "Edm.String", "searchable": True},
                {"name": "category", "type": "Edm.String", "filterable": True, "facetable": True},
                {"name": "sourcepage", "type": "Edm.String", "filterable": True, "facetable": True},
                {"name": "sourcefile", "type": "Edm.String", "filterable": True, "facetable": True},
                {"name": "title", "type": "Edm.String", "filterable": True, "facetable": True},
                {"name": "content_hash", "type": "Edm.String", "filterable": True, "facetable": True},
                {"name": "meta_json_string", "type": "Edm.String", "filterable": True, "facetable": True},
            ],
            "semantic": {
                "configurations": [
                    {
                        "name": "default",
                        "prioritizedFields": {
                            "titleField": {"fieldName": "title"},
                            "prioritizedContentFields": [{"fieldName": "content"}],
                            "prioritizedKeywordsFields": [],
                        },
                    }
                ]
            },
        }

        if embeddings and embeddings.kind != "none":
            field_name = f"content_vector_{embeddings.kind}"
            payload['fields'].append({
                "name": field_name,
                "type": "Collection(Edm.Single)",
                "searchable": True,
                "retrievable": True,
                "dimensions": embeddings.get_embedding_dimensions(),
                "vectorSearchConfiguration": f"{field_name}_config"
            })
            payload['vectorSearch'] = {
                "algorithmConfigurations": [
                    {
                        "name": f"{field_name}_config",
                        "kind": "hnsw",
                        "hnswParameters": {
                            "m": 4,
                            "efConstruction": 400,
                            "metric": "cosine",
                            "efSearch": 500
                        }
                    }
                ]
            }

        logger.info(f"Creating {acs_config['index_name']} search index with embeddings")
        try:
            response = send_put_request(base_url, headers, payload)
            logger.info(response.text)
        except requests.exceptions.RequestException as e:
            logger.error(f"Request failed: {e}\nResponse: {e.response.text}")
            raise
    else:
        logger.info(f"Search index {acs_config['index_name']} already exists")


@tenacity.retry(
    wait=tenacity.wait_fixed(5),  # wait 5 seconds between retries
    stop=tenacity.stop_after_attempt(3),  # stop after 3 attempts
    reraise=True,  # re-raise the exception after the last retry attempt
)
def send_post_request(url, headers, payload):
    response = requests.post(url, data=json.dumps(payload), headers=headers)

    # Raise an exception if the response contains an HTTP error status code
    response.raise_for_status()
    return response


def upload_documents_rest(acs_config: dict, credential, documents):
    if 'api_version' not in acs_config:
        acs_config['api_version'] = "2023-07-01-preview"
    base_url = f"{acs_config['endpoint']}/indexes/{acs_config['index_name']}/docs/index?api-version={acs_config['api_version']}"
    headers = {
        "Content-Type": "application/json"
    }
    if isinstance(credential, DefaultAzureCredential):
        headers["Authorization"] = f"Bearer {credential.get_token('https://search.azure.com/.default').token}"
    else:
        headers["api-key"] = credential.key

    payload = {
        "value": documents
    }

    try:
        response = send_post_request(base_url, headers, payload)
        logger.info(response.text)
    except requests.exceptions.RequestException as e:
        logger.error(f"Request failed: {e}\nResponse: {e.response.text}")
        raise

    return response.json()['value']


def create_index_from_raw_embeddings(emb: EmbeddingsContainer, acs_config={}, connection={}, output_path: Optional[str] = None) -> MLIndex:
    with track_activity(logger, 'update_acs', custom_dimensions={'num_documents': len(emb._document_embeddings)}) as activity_logger:
        logger.info("Updating ACS index")

        credential = get_connection_credential(connection)

        if str(acs_config.get('push_embeddings')).lower() == "false":
            create_search_index_sdk(acs_config, credential)
            search_client = search_client_from_config(acs_config, credential)

            def upload_docs_batch(batch):
                return search_client.upload_documents(documents=batch)
        else:
            create_search_index_rest(acs_config, credential, emb)

            def upload_docs_batch(batch):
                return upload_documents_rest(acs_config, credential, batch)

        batch_size = acs_config['batch_size'] if 'batch_size' in acs_config else 100

        def process_upload_results(results, start_time):
            succeeded = []
            failed = []
            for r in results:
                if isinstance(r, dict):
                    if r['status'] is False:
                        failed.append(r)
                    else:
                        succeeded.append(r)
                else:
                    if r.succeeded:
                        succeeded.append(r)
                    else:
                        failed.append(r)
            duration = time.time() - start_time
            logger.info(f"Uploaded {len(succeeded)} documents to ACS in {duration:.4f} seconds, {len(failed)} failed")
            activity_logger.info("Uploaded documents", extra={'properties': {'succeeded': len(succeeded), 'failed': len(failed), 'duration': duration}})
            if len(failed) > 0:
                for r in failed:
                    if isinstance(r, dict):
                        error = r['errorMessage']
                    else:
                        error = r.error_message
                    logger.error(f"Failed document reason: {error}")
                return failed
            return []

        t1 = time.time()
        num_source_docs = 0
        batch = []
        for doc_id, emb_doc in emb._document_embeddings.items():
            logger.info(f'Adding document: {doc_id}')
            acs_doc = {
                "@search.action": "mergeOrUpload",
                "id": base64.urlsafe_b64encode(doc_id.encode('utf-8')).decode('utf-8'),
                "content": emb_doc.get_data(),
                "category": "document",
                "sourcepage": emb_doc.metadata.get("source", {}).get("url"),
                "sourcefile": emb_doc.metadata.get("source", {}).get("filename"),
                "title": emb_doc.metadata.get("source", {}).get("title"),
                "content_hash": emb_doc.document_hash,
                "meta_json_string": json.dumps(emb_doc.metadata),
            }

            if str(acs_config.get('push_embeddings')).lower() == "false":
                pass
            else:
                acs_doc[f"content_vector_{emb.kind}"] = emb_doc.get_embeddings()

            batch.append(acs_doc)
            if len(batch) % batch_size == 0:
                logger.info(f"Sending {len(batch)} documents to ACS")
                start_time = time.time()
                results = upload_docs_batch(batch)
                failed = process_upload_results(results, start_time)
                if len(failed) > 0:
                    logger.info(f"Retrying {len(failed)} documents")
                    failed_ids = [fail['key'] for fail in failed]
                    results = upload_docs_batch([doc for doc in batch if doc['id'] in failed_ids])
                    failed = process_upload_results(results, start_time)
                    if len(failed) > 0:
                        raise RuntimeError(f"Failed to upload {len(failed)} documents.")
                batch = []
                num_source_docs += batch_size

        if len(batch) > 0:
            logger.info(f"Sending {len(batch)} documents to ACS")
            start_time = time.time()
            results = upload_docs_batch(batch)
            failed = process_upload_results(results, start_time)
            if len(failed) > 0:
                logger.info(f"Retrying {len(failed)} documents")
                failed_ids = [fail['key'] for fail in failed]
                results = upload_docs_batch([doc for doc in batch if doc['id'] in failed_ids])
                failed = process_upload_results(results, start_time)
                if len(failed) > 0:
                    raise RuntimeError(f"Failed to upload {len(failed)} documents.")

            num_source_docs += len(batch)

        duration = time.time()-t1
        logger.info(f"Built index from {num_source_docs} documents and {len(emb._document_embeddings)} chunks, took {duration:.4f} seconds")
        activity_logger.info("Built index", extra={'properties': {'num_source_docs': num_source_docs, 'duration': duration}})


        logger.info('Writing MLIndex yaml')
        mlindex_config = {
            "embeddings": emb.get_metadata()
        }
        mlindex_config["index"] = {
            "kind": "acs",
            "engine": "azure-sdk",
            "index": acs_config['index_name'],
            "api_version": acs_config['api_version'],
            "field_mapping": {
                "content": "content",
                "url": "sourcepage",
                "filename": "sourcefile",
                "title": "title",
                "metadata": "meta_json_string",
            }
        }
        if str(acs_config.get('push_embeddings')).lower() == "false":
            pass
        else:
            mlindex_config["index"]["field_mapping"]["embedding"] = f"content_vector_{emb.kind}"

        if not isinstance(connection, DefaultAzureCredential):
            mlindex_config["index"] = {**mlindex_config["index"], **connection}

        # Keyvault auth and Default ambient auth need the endpoint, Workspace Connection auth could get endpoint.
        mlindex_config["index"]["endpoint"] = acs_config['endpoint']

        if output_path is not None:
            output = Path(output_path)
            output.mkdir(parents=True, exist_ok=True)
            with open(output / "MLIndex", "w") as f:
                yaml.dump(mlindex_config, f)

    mlindex = MLIndex(mlindex_config=mlindex_config)
    return mlindex


def main(args, logger, activity_logger):
    try:
        raw_embeddings_uri = args.embeddings
        logger.info(f'got embeddings uri as input: {raw_embeddings_uri}')
        splits = raw_embeddings_uri.split('/')
        embeddings_dir_name = splits.pop(len(splits)-2)
        logger.info(f'extracted embeddings directory name: {embeddings_dir_name}')
        parent = '/'.join(splits)
        logger.info(f'extracted embeddings container path: {parent}')

        acs_config = json.loads(args.acs_config)

        connection_args = {}
        connection_id = os.environ.get('AZUREML_WORKSPACE_CONNECTION_ID_ACS')
        if connection_id is not None:
            connection_args['connection_type'] = 'workspace_connection'
            connection_args['connection'] = {'id': connection_id}
            from azureml.rag.utils.connections import get_connection_by_id_v2

            connection = get_connection_by_id_v2(connection_id)
            acs_config['endpoint'] = connection['properties']['target']
            acs_config['api_version'] = connection['properties'].get('metadata', {}).get('apiVersion', "2023-07-01-preview")
        elif 'endpoint_key_name' in acs_config:
            connection_args['connection_type'] = 'workspace_keyvault'
            from azureml.core import Run
            run = Run.get_context()
            ws = run.experiment.workspace
            connection_args['connection'] = {
                'key': acs_config['endpoint_key_name'],
                "subscription": ws.subscription_id,
                "resource_group": ws.resource_group,
                "workspace": ws.name,
            }

        from azureml.dataprep.fuse.dprepfuse import (MountOptions, rslex_uri_volume_mount)
        mnt_options = MountOptions(
            default_permission=0o555, allow_other=False, read_only=True)
        logger.info(f'mounting embeddings container from: \n{parent} \n   to: \n{os.getcwd()}/embeddings_mount')
        with rslex_uri_volume_mount(parent, f'{os.getcwd()}/embeddings_mount', options=mnt_options) as mount_context:
            emb = EmbeddingsContainer.load(embeddings_dir_name, mount_context.mount_point)
            create_index_from_raw_embeddings(emb, acs_config=acs_config, connection=connection_args, output_path=args.output)
    except Exception as e:
        logger.error('Failed to update ACS index')
        exception_str = str(e)
        if isinstance(e, requests.exceptions.RequestException):
            activity_logger.activity_info['error'] = 'Failed request to ACS'
            activity_logger.activity_info['response_code'] = e.response.status_code
            activity_logger.activity_info['error_classification'] = 'SystemError'
            if 'Floats quota has been exceeded for this service.' in e.response.text:
                logger.error('Floats quota exceeded on Azure Cognitive Search Service. For more information check these docs: https://github.com/Azure/cognitive-search-vector-pr#storage-and-vector-index-size-limits')
                logger.error('The usage statistic of an index can be checked using this REST API: https://learn.microsoft.com/en-us/rest/api/searchservice/get-index-statistics ')
                activity_logger.activity_info['error_classification'] = 'UserError'
                activity_logger.activity_info['error'] += ": Floats quota has been exceeded for this service."
            elif 'Cannot find nested property' in e.response.text:
                logger.error(f'The vector index provided "{acs_config["index_name"]}" has a different schema than outlined in this components description. This can happen if a different embedding model was used previously when updating this index.')
                activity_logger.activity_info['error_classification'] = 'UserError'
                activity_logger.activity_info['error'] += ": Cannot find nested property"
        elif 'Failed to upload' in exception_str:
            activity_logger.activity_info['error'] = str(e)
            activity_logger.activity_info['error_classification'] = 'SystemError'
        else:
            activity_logger.activity_info['error'] = str(e.__class__.__name__)
            activity_logger.activity_info['error_classification'] = 'SystemError'
        raise e

    logger.info('Updated ACS index')


def main_wrapper(args, logger):
    with track_activity(logger, "update_acs") as activity_logger:
        try:
            main(args, logger, activity_logger)
        except Exception:
            activity_logger.error(f"update_acs failed with exception: {traceback.format_exc()}")  # activity_logger doesn't log traceback
            raise


if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument("--embeddings", type=str)
    parser.add_argument("--acs_config", type=str)
    parser.add_argument("--output", type=str)
    args = parser.parse_args()

    print('\n'.join(f'{k}={v}' for k, v in vars(args).items()))

    enable_stdout_logging()
    enable_appinsights_logging()

    try:
        main_wrapper(args, logger)
    finally:
        if _logger_factory.appinsights:
            _logger_factory.appinsights.flush()
            time.sleep(5)
