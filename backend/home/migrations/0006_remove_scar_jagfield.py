# Generated by Django 2.2.28 on 2023-05-22 14:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_scar_jagfield'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scar',
            name='jagField',
        ),
    ]
