# Generated by Django 2.1.15 on 2021-02-08 03:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('t', '0003_auto_20210208_1148'),
    ]

    operations = [
        migrations.RenameField(
            model_name='treatment',
            old_name='patient_id',
            new_name='patient',
        ),
    ]
