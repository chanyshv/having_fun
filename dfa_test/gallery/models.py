import uuid

from django.db import models
from django.contrib.auth.models import User


def get_upload_file_name(instance: 'Image', filename: str):
    return f"images/{instance.uuid}{filename[filename.rindex('.', ):]}"


class Image(models.Model):
    photo = models.ImageField(upload_to=get_upload_file_name)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
