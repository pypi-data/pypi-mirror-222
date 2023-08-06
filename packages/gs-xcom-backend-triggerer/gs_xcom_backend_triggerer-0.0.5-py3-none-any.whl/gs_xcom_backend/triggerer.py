
from typing import Any
import json
from airflow.models.xcom import BaseXCom
from airflow.providers.google.cloud.hooks.gcs import GCSHook

import uuid


class GCSXComBackend(BaseXCom):
    BUCKET_NAME = "corp-worflowautomation-stg_xcom_data"

    @staticmethod
    def serialize_value(
        value: Any,
        *,
        key: str,
        task_id: str,
        dag_id: str,
        run_id: str = "",
        map_index: int = -1
    ) -> Any:
        hook = GCSHook()
        object_name = "gcs_bucket_data_" + str(uuid.uuid4())
        data = json.dumps(value).encode('UTF-8')
        with hook.provide_file_and_upload(
                bucket_name=GCSXComBackend.BUCKET_NAME,
                object_name=object_name,
        ) as bucket_file:
            bucket_file.write(data)
        return BaseXCom.serialize_value(object_name)

    @staticmethod
    def deserialize_value(result) -> Any:
        object_name = BaseXCom.deserialize_value(result)
        with GCSHook().provide_file(
                bucket_name=GCSXComBackend.BUCKET_NAME,
                object_name=object_name,
        ) as bucket_file:
            bucket_file.flush()
            data = bucket_file.read()
            result = json.loads(data)
        return result
		