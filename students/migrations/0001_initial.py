# Generated by Django 5.0.6 on 2024-06-02 02:52

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre')),
                ('last_name', models.CharField(max_length=100, verbose_name='Apellido')),
                ('user_name', models.CharField(max_length=50, verbose_name='Nombre de usuario')),
                ('email', models.EmailField(max_length=100, verbose_name='Correo')),
                ('phone', models.CharField(max_length=100, verbose_name='Telefono')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Fecha de registro')),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Fecha de actualizacion')),
                ('age', models.IntegerField(verbose_name='Edad')),
                ('date_of_birth', models.DateField(verbose_name='Fecha de nacimiento')),
                ('address', models.CharField(max_length=100, verbose_name='Direccion')),
                ('gender', models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino')], max_length=1, verbose_name='Genero')),
            ],
        ),
    ]
