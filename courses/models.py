from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Course(models.Model):
    MODALITY_CHOICES = [
        ('online', _('Online')),
        ('in_person', _('In-Person')),
        ('hybrid', _('Hybrid')),
    ]

    STATUS_CHOICES = [
        ('active', _('Active')),
        ('inactive', _('Inactive')),
        ('pending', _('Pending')),
    ]

    code = models.CharField(
        max_length=20,
        unique=True,
        blank=True,
        verbose_name=_('Course Code')
    )
    name = models.CharField(
        max_length=100,
        verbose_name=_('Course Name')
    )
    description = models.TextField(
        verbose_name=_('Description')
    )
    start_date = models.DateField(
        verbose_name=_('Start Date')
    )
    end_date = models.DateField(
        verbose_name=_('End Date')
    )
    credits = models.PositiveIntegerField(
        verbose_name=_('Credits')
    )
    modality = models.CharField(
        max_length=20,
        choices=MODALITY_CHOICES,
        verbose_name=_('Modality')
    )
    max_students = models.PositiveIntegerField(
        verbose_name=_('Maximum Students')
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        verbose_name=_('Status')
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('Created At')
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_('Updated At')
    )

    def save(self, *args, **kwargs):
        if not self.pk:  # Solo se ejecuta si el objeto es nuevo
            super().save(*args, **kwargs)  # Guarda el objeto para obtener pk
            self.code = f"CS{self.pk:03d}"  # Genera el código del curso
            super().save(update_fields=['code'])  # Guarda el campo 'code' actualizado
        else:
            super().save(*args, **kwargs)  # Guarda normalmente para objetos existentes

    def __str__(self):
        return "{} ({})".format(self.name, self.code)