from typing import ChainMap
from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class Course(models.Model):
    code = models.CharField(primary_key=True, max_length=6)
    name = models.CharField(max_length=50)
    credit = models.PositiveSmallIntegerField()

    def __str__(self):
        text = "{0} ({1})"
        return text.format(self.name, self.credit)
