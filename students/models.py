from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Students(models.Model):
    name = models.CharField(
        _('Nombre'), max_length=100, blank=False, null=False)
    last_name = models.CharField(
        _('Apellido'), max_length=100, blank=False, null=False)
    user_name = models.CharField(
        _('Nombre de usuario'), max_length=50, blank=False, null=False)
    email = models.EmailField(
        _('Correo'), max_length=100, blank=False, null=False)
    phone = models.CharField(
        _('Telefono'), max_length=100, blank=False, null=False)
    created_at = models.DateTimeField(
        _('Fecha de registro'), default=timezone.now)
    updated_at = models.DateTimeField(
        _('Fecha de actualizacion'), default=timezone.now)
    age = models.IntegerField(_('Edad'), blank=False, null=False)
    date_of_birth = models.DateField(
        _('Fecha de nacimiento'), blank=False, null=False)
    address = models.CharField(
        _('Direccion'), max_length=100, blank=False, null=False)
    gender_choices = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    ]
    gender = models.CharField(
        _('Genero'), max_length=1, choices=gender_choices, null=False, blank=False)
