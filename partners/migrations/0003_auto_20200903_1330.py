# Generated by Django 3.1 on 2020-09-03 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partners', '0002_auto_20200903_1326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partners',
            name='discount',
            field=models.DecimalField(decimal_places=0, max_digits=2),
        ),
    ]
