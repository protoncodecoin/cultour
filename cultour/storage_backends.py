from django.conf import settings
from storage_backends.s3boto3 import S3BotoStorage


class StaticStorage(S3BotoStorage):
    location = "static"
    default_acl = "public-read"


class PublicMediaStorage(S3BotoStorage):
    location = "media"
    default_acl = "public-read"
    file_overwrite = False
