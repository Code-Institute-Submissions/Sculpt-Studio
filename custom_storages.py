from django.conf import settings
from storages.beckends.s3boto3 import S3Boto3Storage


def StaticStorage(S3Boto3Storage):
    location = settings.STATICFILES_LOCATION



def MediaStorage(S3Boto3Storage):
    location = settings.MEDIAFILES_LOCATION