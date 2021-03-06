# Generated by Django 2.2.7 on 2019-12-02 15:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Event', '0004_auto_20191129_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='Event_image',
            field=models.ImageField(blank=True, upload_to='event/%Y/%m/%d'),
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Registration_id', models.CharField(default='', max_length=30)),
                ('Event_name', models.CharField(default='', max_length=30)),
                ('First_name', models.CharField(default='', max_length=30)),
                ('Last_name', models.CharField(default='', max_length=30)),
                ('Email_id', models.CharField(default='', max_length=30)),
                ('Contact', models.CharField(default='', max_length=30)),
                ('Address', models.CharField(default='', max_length=30)),
                ('Total_adult_qty', models.DecimalField(decimal_places=0, max_digits=10)),
                ('Total_child_qty', models.DecimalField(decimal_places=0, max_digits=10)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
