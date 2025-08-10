from storages.backends.s3boto3 import S3Boto3Storage


class StaticStorage(S3Boto3Storage):
    """Stores static files in S3 under the 'static' folder."""

    location = "static"
    default_acl = "public-read"


class PublicMediaStorage(S3Boto3Storage):
    """Stores uploaded media files in S3 under the 'media' folder."""

    location = "media"
    default_acl = "public-read"
    file_overwrite = False
