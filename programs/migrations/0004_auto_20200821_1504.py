# Generated by Django 3.1 on 2020-08-21 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0003_auto_20200821_1418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='programs',
            name='type',
            field=models.CharField(max_length=100),
        ),
    ]
