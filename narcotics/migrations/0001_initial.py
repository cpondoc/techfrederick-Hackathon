# Generated by Django 3.0.7 on 2020-06-22 03:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('vehicles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Narcotic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('shift_hours', models.DurationField()),
                ('morphine_in_stock', models.DecimalField(decimal_places=0, max_digits=3)),
                ('ketamine_in_stock_hundred_miligram_millileter', models.DecimalField(decimal_places=0, max_digits=5)),
                ('ketamine_in_stock_ten_miligram_millileter', models.DecimalField(decimal_places=0, max_digits=4)),
                ('versed_in_stock', models.DecimalField(decimal_places=0, max_digits=3)),
                ('seal_number', models.DecimalField(decimal_places=0, max_digits=5)),
                ('incident_number', models.CharField(max_length=9)),
                ('medication_used', models.CharField(max_length=5)),
                ('medication_amount_mg', models.DecimalField(decimal_places=0, max_digits=4)),
                ('provider_name', models.CharField(max_length=30)),
                ('waste_witness_initials', models.CharField(max_length=2)),
                ('waste_amount_mg', models.DecimalField(decimal_places=0, max_digits=3)),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicles.Vehicle')),
            ],
        ),
    ]
