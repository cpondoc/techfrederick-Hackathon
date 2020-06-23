from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Drug
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

""" Drug Views """

# Viewing all drugs
def drug(request):

    # Creating dictionary of drugs 
    context = {
        'title': "Drugs",
        'drugs': Drug.objects.all()
    }

    # Return List
    return render(request, 'drugs/drugs.html', context)

# Rendering lists of drugs to the view
class DrugListView(LoginRequiredMixin, ListView):

    # Setting the model to drug to list all the drugs
    model = Drug

    # Setting the template name
    template_name = 'drugs/drugs.html'

    # Will list the drugs
    context_object_name = 'drugs'

# Viewing a single drug
class DrugDetailView(LoginRequiredMixin, DetailView):

    # Setting the model to view singular drug
    model = Drug

# Updating a drug view
class DrugUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):

    # Setting the model to update a drug
    model = Drug

    # Setting fields of drug
    fields = ['unit', 'date', 'shift_hours', 'rsi_kit_seal_number', 'expiration_date', 'incident_number', 'hospital_number', 'contact_bc_cole', 'comments']

    # Check if form is valid
    def form_valid(self, form):
        return super().form_valid(form)

     # Check if user is author of post
    def test_func(self):
        return True

# Creating a drug view
class DrugCreateView(LoginRequiredMixin, CreateView):

    # Setting the model to create a drug
    model = Drug

    # Setting fields of drug
    fields = ['unit', 'date', 'shift_hours', 'rsi_kit_seal_number', 'expiration_date', 'incident_number', 'hospital_number', 'contact_bc_cole', 'comments']
    # Check if form is valid
    def form_valid(self, form):
        return super().form_valid(form)

# Viewing a single drug
class DrugDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):

    # Setting the model to view singular drug
    model = Drug

    # Where to redirect
    success_url = "/drugs/"

    # Test func return true
    def test_func(self):
        return True