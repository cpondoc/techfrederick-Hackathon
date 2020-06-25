import django_filters
from .models import Equipment

class EquipmentFilter(django_filters.FilterSet):

    class Meta:
        model = Equipment
        fields = ('unit', 'date', 'mileage', 'fuel', 'emergency_lights', 'driving_lights', 'red_bag', 'red_bag', 'lp_fifteen', 'trans_box', 'bls_bag', 'rtf_bags', 'suction', 'oxygen_bag', 'signature', 'comments')