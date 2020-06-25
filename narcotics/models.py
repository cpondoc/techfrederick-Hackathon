from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from vehicles.models import Vehicle

# Model for Narcotics
class Narcotic(models.Model):

    # Attributes of each narcotic
    unit = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    date = models.DateField(help_text="Please display in the form yyyy-mm-dd!")
    shift_hours = models.DurationField(verbose_name="Shift Hours", help_text="Please enter a time in the form hh:mm:ss indicating total duration!")
    morphine_in_stock = models.DecimalField(decimal_places=0, max_digits=3, verbose_name="Morphine In Stock")
    ketamine_in_stock_hundred_miligram_millileter = models.DecimalField(decimal_places=0, max_digits=5, verbose_name="Ketamine In Stock (in 100mg/ml)")
    ketamine_in_stock_ten_miligram_millileter = models.DecimalField(decimal_places=0, max_digits=4, verbose_name="Ketamine In Stock (in 10mg/ml)")
    versed_in_stock = models.DecimalField(decimal_places=0, max_digits=3, verbose_name="Versed In Stock")
    seal_number = models.DecimalField(decimal_places=0, max_digits=5, verbose_name="Seal #")
    incident_number = models.CharField(max_length=9, verbose_name="Incident #", blank=True)
    medication_used = models.CharField(max_length=10, verbose_name="Medication Used", blank=True)
    medication_amount_mg = models.DecimalField(decimal_places=0, max_digits=4, verbose_name="Medication Amount (in mg)", blank=True)
    provider_name = models.CharField(max_length=30, verbose_name="Provider Last Name")
    waste_witness_initials = models.CharField(max_length=2, verbose_name="Waste Witness Initials", blank=True)
    waste_amount_mg = models.DecimalField(decimal_places=0, max_digits=3, verbose_name="Amount Wasted (in mg)")
    comments = models.TextField()

    # Redirecting after created
    def get_absolute_url(self):
        return reverse('narcotics-detail', kwargs={'pk' : self.pk})
