# Generated by Django 5.0.6 on 2024-06-02 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0003_alter_proffesor_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proffesor',
            name='phone',
            field=models.PositiveIntegerField(verbose_name='Telefono'),
        ),
    ]
