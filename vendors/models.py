from django.db import models
from django.utils import timezone
from core.models import TimeStampedModel


# Create your models here.


class Entity(models.Model):
    ent_name = models.CharField(max_length=50)
    ent_taxnum = models.CharField(max_length=15)
    ent_code = models.CharField(max_length=5)

    def publish(self):
        # self.mod_dt = timezone.now()
        self.save()

    def __str__(self):
        return self.ent_name


class Vendor(TimeStampedModel, models.Model):
    name1 = models.CharField(max_length=50)
    name2 = models.CharField(max_length=50, blank=True)
    address1 = models.CharField(max_length=50)
    address2 = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    vnstatus = models.SmallIntegerField()
    vntaxnum = models.CharField(max_length=15)
    vn_ent = models.ForeignKey(Entity)
    added_dt = models.DateTimeField(default=timezone.now)
    added_by = models.ForeignKey('auth.User')
    mod_dt = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.mod_dt = timezone.now()
        self.save()

    def __str__(self):
        return self.name1
