from django.db import models
from django.conf import settings
import uuid
# Create your models here.


class TimeStampedModel(models.Model):
    """
    An abstract base class model that provides selfupdating
    ``created`` and ``modified`` fields.
    """
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Device(TimeStampedModel):
    name = models.CharField(max_length=100)
    manufacturer_id = models.CharField(max_length=100, unique=True)
    uuid = models.UUIDField(  # Used by the API to look up the record
        db_index=True,
        default=uuid.uuid4,
        editable=False
    )
    type = models.CharField(max_length=100)
    location = models.TextField(max_length=100)

    def __str__(self):
        return self.name
