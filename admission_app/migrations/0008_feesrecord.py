# Generated by Django 3.0.7 on 2021-06-10 17:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admission_app', '0007_storeprimaryadmissionformdetails_form_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeesRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=False)),
                ('form_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='admission_app.StorePrimaryAdmissionFormDetails')),
            ],
        ),
    ]