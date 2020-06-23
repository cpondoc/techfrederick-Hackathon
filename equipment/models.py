from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from vehicles.models import Vehicle

# Model for Vehicle Equipment
class Equipment(models.Model):

    # Attributes for vehicle equipment
    unit = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    date = models.DateField(help_text="Please display in the form yyyy-mm-dd!")
    mileage = models.DecimalField(decimal_places=0, max_digits=4)
    fuel = models.CharField(max_length=1, help_text="Please enter E for empty or F for full.")
    emergency_lights = models.BooleanField(verbose_name="Emergency Lights")
    driving_lights = models.BooleanField(verbose_name="Driving Lights")
    red_bag = models.BooleanField(verbose_name="Red Bag")
    lp_fifteen = models.BooleanField(verbose_name="LP 15")
    trans_box = models.BooleanField(verbose_name="Trans Box")
    bls_bag = models.BooleanField(verbose_name="BLS Bag")
    rtf_bags = models.BooleanField(verbose_name="RTF Bags")
    suction = models.BooleanField()
    oxygen_bag = models.BooleanField(verbose_name="Oxygen Bag")
    signature = models.CharField(max_length=50, verbose_name="Provider Signature")
    comments = models.TextField()

    # Redirecting after created
    def get_absolute_url(self):
        return reverse('equipment-detail', kwargs={'pk' : self.pk})