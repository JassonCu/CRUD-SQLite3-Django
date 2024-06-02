from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Semester(models.Model):
    number = models.IntegerField(
        unique=True, verbose_name="Número de semestre")

    class Meta:
        verbose_name = "Semestre"
        verbose_name_plural = "Semestres"

    def __str__(self):
        return f"Semestre {self.number}"


class Course(models.Model):
    name = models.CharField(verbose_name=_(
        "Nombre del curso"), max_length=100, null=False, blank=False)
    description = models.TextField(verbose_name=_(
        "Descripción"), null=False, blank=False)
    semester = models.ForeignKey(
        Semester, verbose_name=_("Semestre"), on_delete=models.CASCADE)
    prerequisites = models.ManyToManyField(
        "self", verbose_name=_("Requisitos"), blank=True)
    created_at = models.DateTimeField(
        verbose_name=_("Fecha de creación"), default=timezone.now)
    updated_at = models.DateTimeField(
        verbose_name=_("Fecha de actualización"), default=timezone.now)
    class Meta:
        verbose_name = _("Curso")
        verbose_name_plural = _("Cursos")

    def __str__(self):
        return self.name
