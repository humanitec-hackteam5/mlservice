# Generated by Django 2.1.5 on 2019-06-04 16:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Train',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataset_uuid', models.UUIDField(verbose_name='DataSet UUID')),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.SmallIntegerField(choices=[(0, 'Not trained yet'), (1, 'Training'), (2, 'Trained')])),
                ('trained_model', models.FileField(blank=True, null=True, upload_to='')),
                ('dataset_url', models.URLField(blank=True, null=True)),
            ],
        ),
    ]
