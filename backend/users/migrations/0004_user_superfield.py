# Generated by Django 2.2.28 on 2023-05-16 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20230516_1236'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='superField',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
