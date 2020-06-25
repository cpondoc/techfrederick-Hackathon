from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Vehicle
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

""" Vehicle Views """

# Viewing all vehicles
def vehicle(request):

    # Creating dictionary of vehicles 
    context = {
        'title': "Vehicles",
        'vehicles': Vehicle.objects.all()
    }
    
    # Return List
    return render(request, 'vehicles/vehicles.html', context)


# Rendering lists of vehicles to the view
class VehicleListView(LoginRequiredMixin, ListView):

    # Setting the model to vehicle to list all the vehicles
    model = Vehicle

    # Setting the template name
    template_name = 'vehicles/vehicles.html'

    # Will list the vehicles
    context_object_name = 'vehicles'

# Viewing a single vehicle
class VehicleDetailView(LoginRequiredMixin, DetailView):

    # Setting the model to view singular vehicle
    model = Vehicle

# Updating a vehicle view
class VehicleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):

    # Setting the model to update a vehicle
    model = Vehicle

    # Setting fields of vehicle
    fields = ['unit', 'date', 'oil', 'transmission_fluid', 'brake_fluid', 'coolant_fluid', 'lucas', 'ems_equipment', 'suction', 'front_left_tire_pressure', 'front_right_tire_pressure', 'rear_left_tire_pressure', 'rear_right_tire_pressure', 'provider_name', 'comments']

    # Check if form is valid
    def form_valid(self, form):
        return super().form_valid(form)

     # Check if user is author of post
    def test_func(self):
        return True

# Creating a vehicle view
class VehicleCreateView(LoginRequiredMixin, CreateView):

    # Setting the model to create a vehicle
    model = Vehicle

    # Setting fields of vehicle
    fields = ['unit', 'date', 'oil', 'transmission_fluid', 'brake_fluid', 'coolant_fluid', 'lucas', 'ems_equipment', 'suction', 'front_left_tire_pressure', 'front_right_tire_pressure', 'rear_left_tire_pressure', 'rear_right_tire_pressure', 'provider_name', 'comments']

    # Check if form is valid
    def form_valid(self, form):
        return super().form_valid(form)

# Viewing a single vehicle
class VehicleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):

    # Setting the model to view singular drug
    model = Vehicle

    # Where to redirect
    success_url = "/vehicles/"

    # Test func return true
    def test_func(self):
        return True