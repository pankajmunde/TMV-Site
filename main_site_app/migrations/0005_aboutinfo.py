# Generated by Django 3.0.7 on 2021-06-11 15:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main_site_app', '0004_upcomingevent_event_poster'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('title', models.CharField(max_length=500)),
                ('photo', models.FileField(upload_to='About_photos/')),
                ('description', models.TextField()),
            ],
        ),
    ]
