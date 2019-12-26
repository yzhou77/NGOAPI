# Generated by Django 2.2.7 on 2019-12-03 01:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('User_id', models.CharField(default='', max_length=30)),
                ('firstName', models.CharField(default='', max_length=30)),
                ('lastName', models.CharField(default='', max_length=30)),
                ('email', models.CharField(default='', max_length=50)),
                ('password', models.CharField(default='', max_length=30)),
                ('role', models.CharField(choices=[('Admin', 'Admin'), ('Regular', 'Regular')], default='Admin', max_length=30)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]