# Generated by Django 3.0.7 on 2020-06-22 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0003_auto_20200622_2315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='ems_equipment',
            field=models.BooleanField(verbose_name='EMS Equipment'),
        ),
    ]
