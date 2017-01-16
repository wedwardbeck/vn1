from django.db import models

# Create your models here.


class Entity(models.Model):
    ent_name = models.CharField(max_length=50)
    ent_taxnum = models.CharField(max_length=15)
    ent_code = models.CharField(max_length=5)


class Vendor(models.Model):
    name1 = models.CharField(max_length=50)
    name2 = models.CharField(max_length=50, null=True, blank=True)
    address1 = models.CharField(max_length=50)
    address2 = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    vnstatus = models.SmallIntegerField()
    vntaxnum = models.CharField(max_length=15)
    vn_ent = models.ForeignKey(Entity)
    added_dt = models.DateTimeField()
    added_by = models.IntegerField()


