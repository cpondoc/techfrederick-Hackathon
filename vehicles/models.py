from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Model for vehicle
class Vehicle(models.Model):

    # Attributes of each vehicle
    unit = models.CharField(max_length=30)
    date = models.DateField(help_text="Please display in the form yyyy-mm-dd!")
    oil = models.BooleanField()
    transmission_fluid = models.BooleanField()
    brake_fluid = models.BooleanField()
    coolant_fluid = models.BooleanField()
    lucas = models.BooleanField(verbose_name="LUCAS")
    ems_equipment = models.BooleanField(verbose_name="EMS Equipment")
    suction = models.BooleanField()
    front_left_tire_pressure = models.DecimalField(decimal_places=0, max_digits=2, verbose_name="Front Left Tire Pressure (in PSI)")
    front_right_tire_pressure = models.DecimalField(decimal_places=0, max_digits=2, verbose_name="Front Right Tire Pressure (in PSI)")
    rear_left_tire_pressure = models.DecimalField(decimal_places=0, max_digits=2, verbose_name="Rear Left Tire Pressure (in PSI)")
    rear_right_tire_pressure = models.DecimalField(decimal_places=0, max_digits=2, verbose_name="Rear Right Tire Pressure (in PSI)")
    provider_name = models.CharField(max_length=30)
    comments = models.TextField()

    # Redirecting after created
    def get_absolute_url(self):
        return reverse('vehicles-detail', kwargs={'pk' : self.pk})

    # Defining the name
    def __str__(self):
        return (self.unit)