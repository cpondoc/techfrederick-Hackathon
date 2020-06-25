import django_filters
from .models import Narcotic

class NarcoticsFilter(django_filters.FilterSet):

    class Meta:
        model = Narcotic
        fields = ('unit', 'date', 'shift_hours', 'morphine_in_stock', 'ketamine_in_stock_hundred_miligram_millileter', 'ketamine_in_stock_ten_miligram_millileter', 'versed_in_stock', 'seal_number', 'incident_number', 'medication_used', 'medication_amount_mg', 'provider_name', 'waste_witness_initials', 'waste_amount_mg', 'comments')