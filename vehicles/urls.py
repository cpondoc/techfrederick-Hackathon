from django.urls import path
from .views import (
    VehicleListView,
    VehicleDetailView,
    VehicleUpdateView,
    VehicleCreateView,
    VehicleDeleteView
)
from . import views

urlpatterns = [
    path('', VehicleListView.as_view(), name="vehicles-home"),
    path('<int:pk>/', VehicleDetailView.as_view(), name="vehicles-detail"),
    path('<int:pk>/update/', VehicleUpdateView.as_view(), name="vehicles-update"),
    path('new/', VehicleCreateView.as_view(), name="vehicles-create"),
    path('<int:pk>/delete/', VehicleDeleteView.as_view(), name="vehicles-delete")
]