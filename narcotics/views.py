from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Narcotic
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
import smtplib, ssl, email
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from django.contrib.auth.models import User
from .filters import NarcoticsFilter

""" Sending Email """

def email_user(receiving_email_address, supervisor, subject, drug, recorded_amount, medic_amount):
   message = MIMEMultipart()
   port = 465 # For SSL
   smtp_server = "smtp.gmail.com"
   sender_email = "frederickcountydfrs@gmail.com"
   receiver_email = receiving_email_address
   password = "Flava$1729"
 
   SUBJECT = subject
   FROM = sender_email
   TO = receiver_email
 
   TEXT = f"""{supervisor},
   According to the records, the amount of {drug} has been falsely reported. The last record of {drug} is {recorded_amount}mg, however the medic is counting {medic_amount}mg. Please resolve immediately."""
 
   message = "From: {}\n\nTo: {}\n\nSubject: {}\n\n{}".format(FROM, TO, SUBJECT, TEXT)
  
   #Create a secure SSL Context
   context = ssl.create_default_context()
 
   with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
       server.login(sender_email, password)
       server.sendmail(sender_email, receiver_email, message)

""" Narcotic Views """

# Viewing all narcotics
def narcotic(request):

    # List of all users
    users = User.objects.all()

    # List of all narcotics
    narcotics = Narcotic.objects.all()

    # Checking narcotic amounts
    for i in range(0, len(narcotics) - 1):

        # Checking if morphine in stock doesn't match
        if (narcotics[i].morphine_in_stock != narcotics[i + 1].morphine_in_stock):

            # Print alert
            print("Sending morphine email.")

            # Send email alert to admin
            for user in users:
                if user.groups.filter(name = "admin").exists():
                    email_user(user.email, "chris.pondoc@gmail.com", "Morphine in Stock Alert", "Morphine", narcotics[i].morphine_in_stock, narcotics[i + 1].morphine_in_stock)
        
        # Checking if ketamine in stock doesn't match
        if (narcotics[i].ketamine_in_stock_hundred_miligram_millileter != narcotics[i + 1].ketamine_in_stock_hundred_miligram_millileter):

            # Print alert
            print("Sending ketamine in stock in 100 mg/ml email.")

            # Send email alert to admin
            for user in users:
                if user.groups.filter(name = "admin").exists():
                    email_user(user.email, "chris.pondoc@gmail.com", "Ketamine in Stock (100 mg/ml) Alert", "Ketamine in Stock (100 mg/ml)", narcotics[i].ketamine_in_stock_hundred_miligram_millileter, narcotics[i + 1].ketamine_in_stock_hundred_miligram_millileter)

        # Checking if second ketamine in stock doesn't match
        if (narcotics[i].ketamine_in_stock_ten_miligram_millileter != narcotics[i + 1].ketamine_in_stock_ten_miligram_millileter):

            # Print alert
            print("Sending ketamine in stock in 10 mg/ml email.")

            # Send email alert to admin
            for user in users:
                if user.groups.filter(name = "admin").exists():
                    email_user(user.email, "chris.pondoc@gmail.com", "Ketamine in Stock (10 mg/ml) Alert", "Ketamine in Stock (10 mg/ml)", narcotics[i].ketamine_in_stock_ten_miligram_millileter, narcotics[i + 1].ketamine_in_stock_ten_miligram_millileter)
        
        # Checking if versed in stock doesn't match
        if (narcotics[i].versed_in_stock != narcotics[i + 1].versed_in_stock):

            # Print alert
            print("Sending versed in stock email.")

            # Send email alert to admin
            for user in users:
                if user.groups.filter(name = "admin").exists():
                    email_user(user.email, "chris.pondoc@gmail.com", "versed_in_stock in Stock Alert", "versed_in_stock in Stock", narcotics[i].versed_in_stock, narcotics[i + 1].versed_in_stock)        
        
        # Everything is good!
        else:
            print("Looking good!")

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

    # List of all users
    users = User.objects.all()

    # List of all narcotics
    narcotics = Narcotic.objects.all()

    # Checking narcotic amounts
    for i in range(0, len(narcotics) - 1):

        # Checking if morphine in stock doesn't match
        if (narcotics[i].morphine_in_stock != narcotics[i + 1].morphine_in_stock):

            # Print alert
            print("Sending morphine email.")

            # Send email alert to admin
            for user in users:
                if user.groups.filter(name = "admin").exists():
                    email_user(user.email, "chris.pondoc@gmail.com", "Morphine in Stock Alert", "Morphine", narcotics[i].morphine_in_stock, narcotics[i + 1].morphine_in_stock)
        
        # Checking if ketamine in stock doesn't match
        if (narcotics[i].ketamine_in_stock_hundred_miligram_millileter != narcotics[i + 1].ketamine_in_stock_hundred_miligram_millileter):

            # Print alert
            print("Sending ketamine in stock in 100 mg/ml email.")

            # Send email alert to admin
            for user in users:
                if user.groups.filter(name = "admin").exists():
                    email_user(user.email, "chris.pondoc@gmail.com", "Ketamine in Stock (100 mg/ml) Alert", "Ketamine in Stock (100 mg/ml)", narcotics[i].ketamine_in_stock_hundred_miligram_millileter, narcotics[i + 1].ketamine_in_stock_hundred_miligram_millileter)

        # Checking if second ketamine in stock doesn't match
        if (narcotics[i].ketamine_in_stock_ten_miligram_millileter != narcotics[i + 1].ketamine_in_stock_ten_miligram_millileter):

            # Print alert
            print("Sending ketamine in stock in 10 mg/ml email.")

            # Send email alert to admin
            for user in users:
                if user.groups.filter(name = "admin").exists():
                    email_user(user.email, "chris.pondoc@gmail.com", "Ketamine in Stock (10 mg/ml) Alert", "Ketamine in Stock (10 mg/ml)", narcotics[i].ketamine_in_stock_ten_miligram_millileter, narcotics[i + 1].ketamine_in_stock_ten_miligram_millileter)
        
        # Checking if versed in stock doesn't match
        if (narcotics[i].versed_in_stock != narcotics[i + 1].versed_in_stock):

            # Print alert
            print("Sending versed in stock email.")

            # Send email alert to admin
            for user in users:
                if user.groups.filter(name = "admin").exists():
                    email_user(user.email, "chris.pondoc@gmail.com", "versed_in_stock in Stock Alert", "versed_in_stock in Stock", narcotics[i].versed_in_stock, narcotics[i + 1].versed_in_stock)        
        
        # Everything is good!
        else:
            print("Looking good!")

    # Setting the template name
    template_name = 'narcotics/narcotics.html'

    # Will list the narcotics
    context_object_name = 'narcotics'

    # Creating filter object!
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = NarcoticsFilter(self.request.GET, queryset = self.get_queryset())
        return context

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