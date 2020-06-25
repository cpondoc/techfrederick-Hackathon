import django_filters
from .models import Vehicle

class VehicleFilter(django_filters.FilterSet):

    class Meta:
        model = Vehicle
        fields = ('unit', 'date', 'oil', 'transmission_fluid', 'brake_fluid', 'coolant_fluid', 'lucas', 'ems_equipment', 'suction', 'front_left_tire_pressure', 'front_right_tire_pressure', 'rear_left_tire_pressure', 'rear_right_tire_pressure', 'provider_name', 'comments')