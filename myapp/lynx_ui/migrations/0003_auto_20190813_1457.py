# Generated by Django 2.2.3 on 2019-08-13 05:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lynx_ui', '0002_ocrjsonreturnvaluemodel'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='OCRJsonReturnValueModel',
            new_name='OCRInputModel',
        ),
    ]
