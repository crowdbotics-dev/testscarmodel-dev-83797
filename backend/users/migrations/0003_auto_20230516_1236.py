# Generated by Django 2.2.28 on 2023-05-16 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20230516_1234'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='nickName',
        ),
        migrations.RemoveField(
            model_name='user',
            name='otherName',
        ),
        migrations.AddField(
            model_name='user',
            name='myfield',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
