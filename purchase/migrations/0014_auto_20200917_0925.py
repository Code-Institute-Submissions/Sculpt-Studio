# Generated by Django 3.1 on 2020-09-17 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchase', '0013_auto_20200914_1910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkout',
            name='program_cost',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
        migrations.AlterField(
            model_name='checkout',
            name='total_cost',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
    ]
