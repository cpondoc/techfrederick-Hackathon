from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from vehicles.models import Vehicle

# Model for drug
class Drug(models.Model):

    # Attributes of each drug
    unit = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    date = models.DateField(help_text="Please display in the form yyyy-mm-dd!")
    shift_hours = models.DurationField(verbose_name="Shift Hours", help_text="Please display in the form hh:mm:ss!")
    rsi_kit_seal_number = models.CharField(max_length=5, verbose_name="RSI Kit #1 Seal #")
    expiration_date = models.DateField(verbose_name="Expiration Date")
    incident_number = models.CharField(max_length=9, verbose_name="Incident #")
    hospital_number = models.CharField(max_length=5, verbose_name="Hospital #")
    provider_name = models.CharField(max_length=30, verbose_name="Provider Name")
    contact_bc_cole = models.DateTimeField(verbose_name="Contact B/C Cole - Date and Time", help_text="Please display in the form yyyy-mm-dd hh:mm:ss!")
    comments = models.TextField()

    # Redirecting after created
    def get_absolute_url(self):
        return reverse('drugs-detail', kwargs={'pk' : self.pk})