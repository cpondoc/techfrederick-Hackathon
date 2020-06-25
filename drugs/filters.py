import django_filters
from .models import Drug

class DrugFilter(django_filters.FilterSet):

    class Meta:
        model = Drug
        fields = ('unit', 'date', 'shift_hours', 'rsi_kit_seal_number', 'expiration_date', 'incident_number', 'hospital_number', 'contact_bc_cole', 'comments')