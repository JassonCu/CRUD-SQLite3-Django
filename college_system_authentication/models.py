from django.db import models
from django.utils.translation import gettext_lazy as _
from .managers import RoleManager
from django.contrib.auth.models import AbstractUser, BaseUserManager, Group, Permission


# Create your models here.

class UserAccountManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError('El usuario debe tener un correo electrónico')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('El superusuario debe tener is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('El superusuario debe tener is_superuser=True.')
        return self.create_user(username, email, password, **extra_fields)


class UserAccount(AbstractUser):
    phone_number = models.CharField(
        _('Número de teléfono'), max_length=25, blank=False, default='')
    role = models.ManyToManyField(
        'Role',
        blank=True
    )
    groups = models.ManyToManyField(
        Group,
        related_name='useraccount_set',
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='useraccount_set',
        blank=True,
    )

    objects = UserAccountManager()

    def __str__(self):
        return self.username


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
