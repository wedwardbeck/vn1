from django.db import models
from django.utils import timezone


# Create your models here.


class TimeStampedModel(models.Model):
    created = models.DateTimeField(default=timezone.now)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
