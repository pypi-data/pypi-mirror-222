POLLY_PY_TEST_FILES_URL = (
    "https://raw.githubusercontent.com/ElucidataInc/PublicAssets/master/"
    + "internal-user/polly_py_test_files"
)
# repo id used in the tests
INGESTION_TEST_1_REPO_ID = "1654268055800"

MOCK_RESPONSE_DOWNLOAD_DATA = {
    "data": {
        "attributes": {
            "last-modified": "2022-11-09 10:46:07.000000",
            "size": "912.43 KB",
            "download_url": "https://github.com/ElucidataInc/PublicAssets/blob/master/internal-user/add_dataset_test_file/"
            + "data_file/tcga_LIHC_Copy_Number_Segment_TCGA-FV-A3R2-01A.gct",
        }
    }
}

MOCK_403_ACCESS_DENIED_RESPONSE = {
    "errors": [
        {
            "status": "403",
            "code": "forbidden",
            "title": "Access denied",
            "detail": "Access denied for requested resource",
        }
    ]
}

MOCK_REPO_NOT_FOUND_RESPONSE = {
    "errors": [
        {
            "status": "404",
            "code": "resource_not_found",
            "title": "Data not found not found",
            "detail": "Repository with repo key not found",
        }
    ]
}
FETCH_WORKSPACES_MOCKED_RESPONSE = [
    {
        "id": 10,
        "name": "document_workspace",
        "status": "active",
        "description": None,
        "last_modified": "2023-02-07 11:38:28",
        "tag_names": [],
        "favourite": False,
        "watch": False,
    },
    {
        "id": 10,
        "name": "schema backup ",
        "status": "active",
        "description": "",
        "last_modified": "2023-02-07 13:32:34",
        "tag_names": [],
        "favourite": False,
        "watch": False,
    },
]

WORKSPACE_CREATE_COPY_POST_REQUEST_RESPONSE = {
    "data": [
        {
            "type": "files",
            "id": "id",
            "attributes": {
                "body": "Workspace_copy started, You will be notified upon completion."
            },
        }
    ],
    "included": [
        {
            "type": "file",
            "id": "id",
            "attributes": {
                "file_name": "file_name",
                "s3_key": "s3_key",
                "operation_id": "0a0-3986-4d43-94be-dd787b2f5de8",
            },
            "links": {"self": "/async_operations/24e610a0-3986-4d43-94be-dd787b2f5de8"},
        }
    ],
}

WORKSPACE_CREATE_COPY_GET_REQUEST_RESPONSE = {
    "data": {
        "user_id": 00,
        "destination_key": "destination_key",
        "source_key": "source_key",
        "status": "COMPLETE",
        "operation_id": "4df4137a-3836-4fe0-a714-45049269b5fc",
        "created_timestamp": 1679564893,
        "modified_timestamp": 1679564894,
        "type": "file",
    }
}

WORKSPACE_RESPONSE_JSON = [{"key": "value"}]

SAMPLE_QUERY = "SELECT * FROM sc_data_lake.features_singlecell LIMIT 100"
