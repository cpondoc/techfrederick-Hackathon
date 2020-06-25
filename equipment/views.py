from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Equipment
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

""" Vehicle Equipment Views """

# Viewing all Vehicles
def equipment(request):

    # Creating dictionary of vehicle equipment
    context = {
        'title': "Equipment",
        'equipment': Equipment.objects.all()
    }

    # Return List
    return render(request, 'equipment/equipment.html', context)

# Rendering lists of vehicle equipment to the view
class EquipmentListView(LoginRequiredMixin, ListView):

    # Setting the model to vehicle equipment to list all the vehicle equipment
    model = Equipment

    # Setting the template name
    template_name = 'equipment/equipment.html'

    # Will list the posts
    context_object_name = 'equipment'

# Viewing a single post
class EquipmentDetailView(LoginRequiredMixin, DetailView):

    # Setting the model to view singular vehicle equipment
    model = Equipment

# Updating a post view
class EquipmentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):

    # Setting the model to update a post
    model = Equipment

    # Setting fields of post
    fields = ['unit', 'date', 'mileage', 'fuel', 'emergency_lights', 'driving_lights', 'red_bag', 'red_bag', 'lp_fifteen', 'trans_box', 'bls_bag', 'rtf_bags', 'suction', 'oxygen_bag', 'signature', 'comments']

    # Check if form is valid
    def form_valid(self, form):
        return super().form_valid(form)

     # Check if user is author of post
    def test_func(self):
        return True

# Creating a Vehicle Equipment view
class EquipmentCreateView(LoginRequiredMixin, CreateView):

    # Setting the model to create a post
    model = Equipment

    # Setting fields of post
    fields = ['unit', 'date', 'mileage', 'fuel', 'emergency_lights', 'driving_lights', 'red_bag', 'red_bag', 'lp_fifteen', 'trans_box', 'bls_bag', 'rtf_bags', 'suction', 'oxygen_bag', 'signature', 'comments']

    # Check if form is valid
    def form_valid(self, form):
        return super().form_valid(form)

# Viewing a single post
class EquipmentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):

    # Setting the model to view singular post
    model = Equipment

    # Where to redirect
    success_url = "/equipment/"

    # Test func return true
    def test_func(self):
        return True

# Home Page
def home(request):

    # Print out the user group of the user.
    print(request.user.groups.all()[0].name)

    return render(request, 'equipment/home.html')