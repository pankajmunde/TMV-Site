# Generated by Django 3.0.7 on 2021-06-06 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admission_app', '0002_auto_20210606_1352'),
    ]

    operations = [
        migrations.AddField(
            model_name='storeprimaryadmissionformdetails',
            name='email',
            field=models.EmailField(default=1, max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='storeprimaryadmissionformdetails',
            name='username',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
