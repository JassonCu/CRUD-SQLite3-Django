from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Proffesor(models.Model):
    name = models.CharField(verbose_name=_(
        'Nombre'), max_length=100, null=False, blank=False)
    last_name = models.CharField(verbose_name=_(
        'Apellido'), max_length=100, null=False, blank=False)
    email = models.EmailField(verbose_name=_(
        'Email'), max_length=100, null=False, blank=False)
    phone = models.PositiveIntegerField(verbose_name=_(
        'Telefono'), max_length=8, null=False, blank=False)
    age = models.PositiveSmallIntegerField(
        verbose_name=_('Edad'), null=False, blank=False)
    address = models.CharField(verbose_name=_(
        'Direccion'), max_length=100, null=False, blank=False)
    date_of_birth = models.DateField(verbose_name=_(
        'Fecha de nacimiento'), null=False, blank=False)
    gender_choices = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    ]
    gender = models.CharField(verbose_name=_(
        'Genero'), max_length=1, choices=gender_choices, null=False, blank=False)
    created_at = models.DateTimeField(verbose_name=_(
        'Fecha de creacion'), default=timezone.now)
    updated_at = models.DateTimeField(verbose_name=_(
        "Fecha de actualización"), default=timezone.now)

    class Meta:
        verbose_name = _("Profesor")
        verbose_name_plural = _("Profesores")
        ordering = ['name']

    def __str__(self):
        return f'{self.name} {self.last_name}'