from django.urls import path
from django.urls import path
from .views import (
    EquipmentListView,
    EquipmentDetailView,
    EquipmentUpdateView,
    EquipmentCreateView,
    EquipmentDeleteView
)
from . import views
from . import views

urlpatterns = [
    path('equipment/', EquipmentListView.as_view(), name="equipment-home"),
    path('equipment/<int:pk>/', EquipmentDetailView.as_view(), name="equipment-detail"),
    path('equipment/<int:pk>/update/', EquipmentUpdateView.as_view(), name="equipment-update"),
    path('equipment/new/', EquipmentCreateView.as_view(), name="equipment-create"),
    path('equipment/<int:pk>/delete/', EquipmentDeleteView.as_view(), name="equipment-delete"),
    path('', views.home, name="home-page")
]