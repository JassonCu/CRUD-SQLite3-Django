# Generated by Django 5.0.6 on 2024-06-06 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre')),
                ('name_spanish', models.CharField(default='', max_length=50, verbose_name='Nombre Español')),
                ('description', models.CharField(max_length=150, verbose_name='Descripción')),
            ],
        ),
    ]
