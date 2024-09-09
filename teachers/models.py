from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

# Create your models here.

class Teacher(models.Model):
    name = models.CharField(_('Name'), max_length=50)
    last_name = models.CharField(_('Last name'), max_length=50)
    email = models.EmailField(_('Email'), max_length=254, unique=True)
    created_at = models.DateTimeField(_('Created at'), default=timezone.now)
    updated_at = models.DateTimeField(_('Updated at'), auto_now=True)


    def __str__(self):
        return "{} ({})".format(self.name, self.email)