import logging
from uuid import uuid4

import boto3
from botocore.utils import ClientError
from fastapi import UploadFile

from app.core.config import settings


def upload_file(file: UploadFile):
    s3_client = boto3.client(
        "s3",
        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_SECRET_KEY,
    )

    original_name = file.filename
    mimetype = original_name.split(".")[-1] if original_name else ""
    filename = f"{uuid4()}.{mimetype}"

    try:
        file.file.read()
        file.file.seek(0)

        s3_client.upload_fileobj(file.file, settings.AWS_BUCKET, filename)
    except ClientError as e:
        logging.error(e)
        return False
    finally:
        file.file.close()

    return filename
