from django.db import models
from django.utils.translation import gettext_lazy as _
from .managers import RoleManager

# Create your models here.


class Role(models.Model):
    """
    Modelo para roles de empresas (ej. Maestro, Estudiante, etc)
    """
    objects = RoleManager()
    name = models.CharField(
        _('Nombre'), max_length=50, unique=True, blank=False, null=False)
    name_spanish = models.CharField(
        _('Nombre Español'), max_length=50, default='', unique=True, blank=False, null=False)
    description = models.CharField(
        _('Descripción'), max_length=150, unique=True, blank=False, null=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Rol')
        verbose_name_plural = _('Roles')
        ordering = ['name']
