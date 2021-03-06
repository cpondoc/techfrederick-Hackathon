# Generated by Django 3.0.7 on 2020-06-25 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drugs', '0004_auto_20200623_1935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drug',
            name='date',
            field=models.DateField(help_text='Please display in the form yyyy-mm-dd!'),
        ),
        migrations.AlterField(
            model_name='drug',
            name='shift_hours',
            field=models.DurationField(help_text='Please display in the form hh:mm:ss!', verbose_name='Shift Hours'),
        ),
    ]
