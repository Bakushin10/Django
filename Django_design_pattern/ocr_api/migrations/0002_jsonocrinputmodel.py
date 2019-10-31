# Generated by Django 2.2.3 on 2019-08-14 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ocr_api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='JsonOCRInputModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field', models.CharField(max_length=5)),
                ('hasField', models.BooleanField(default=False)),
                ('coordinates', models.TextField(max_length=1000)),
                ('text', models.CharField(max_length=50)),
            ],
        ),
    ]
