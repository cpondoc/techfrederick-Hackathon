from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Narcotic
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

""" Narcotic Views """

# Viewing all narcotics
def narcotic(request):

    # Creating dictionary of narcotics 
    context = {
        'title': "Narcotics",
        'narcotics': Narcotic.objects.all()
    }

    # Return List
    return render(request, 'narcotics/narcotics.html', context)

# Rendering lists of narcotics to the view
class NarcoticListView(LoginRequiredMixin, ListView):

    # Setting the model to drug to list all the drugs
    model = Narcotic

    print(type(Narcotic.objects.all()))

    # Setting the template name
    template_name = 'narcotics/narcotics.html'

    # Will list the narcotics
    context_object_name = 'narcotics'

# Viewing a single narcotic
class NarcoticDetailView(LoginRequiredMixin, DetailView):

    # Setting the model to view singular drug
    model = Narcotic

# Updating a narcotic view
class NarcoticUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):

    # Setting the model to update a narcotic
    model = Narcotic

    # Setting fields of narcotic
    fields = ['unit', 'date', 'shift_hours', 'morphine_in_stock', 'ketamine_in_stock_hundred_miligram_millileter', 'ketamine_in_stock_ten_miligram_millileter', 'versed_in_stock', 'seal_number', 'incident_number', 'medication_used', 'medication_amount_mg', 'provider_name', 'waste_witness_initials', 'waste_amount_mg', 'comments']

    # Check if form is valid
    def form_valid(self, form):
        return super().form_valid(form)

     # Return true
    def test_func(self):
        return True

# Creating a narcotic view
class NarcoticCreateView(LoginRequiredMixin, CreateView):

    # Setting the model to create a narcotic
    model = Narcotic

    # Setting fields of narcotic
    fields = ['unit', 'date', 'shift_hours', 'morphine_in_stock', 'ketamine_in_stock_hundred_miligram_millileter', 'ketamine_in_stock_ten_miligram_millileter', 'versed_in_stock', 'seal_number', 'incident_number', 'medication_used', 'medication_amount_mg', 'provider_name', 'waste_witness_initials', 'waste_amount_mg', 'comments']

    # Check if form is valid
    def form_valid(self, form):
        return super().form_valid(form)

# Viewing a single narcotic
class NarcoticDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):

    # Setting the model to view singular drug
    model = Narcotic

    # Where to redirect
    success_url = "/narcotics/"

    # Test func return true
    def test_func(self):
        return True