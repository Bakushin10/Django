# Generated by Django 2.2.3 on 2019-07-30 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OrchestratorInputModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agentCode', models.CharField(max_length=15)),
                ('companyCode', models.CharField(max_length=2)),
                ('imageSourceType', models.CharField(max_length=1)),
            ],
        ),
    ]