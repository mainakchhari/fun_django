from django.db import models
from django.db.models.fields import CharField, TextField


class Ngo(models.Model):
    name = CharField(max_length=25, null=False)
    registration_no = CharField(max_length=16, null=False, primary_key=True)
    address = TextField(null=False)
    description = TextField(null=True, blank=True)  # TODO: why blank=True
