# Generated by Django 3.0.7 on 2021-06-11 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_site_app', '0005_aboutinfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutinfo',
            name='chairman_name',
            field=models.CharField(default='Pranati. R. Tilak', max_length=255),
            preserve_default=False,
        ),
    ]
