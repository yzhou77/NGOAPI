# Generated by Django 2.2.7 on 2019-12-23 15:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Event', '0010_auto_20191223_0412'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='author',
        ),
    ]
