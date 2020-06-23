from django.urls import path
from .views import (
    DrugListView,
    DrugDetailView,
    DrugUpdateView,
    DrugCreateView,
    DrugDeleteView
)
from . import views

urlpatterns = [
    path('', DrugListView.as_view(), name="drugs-home"),
    path('<int:pk>/', DrugDetailView.as_view(), name="drugs-detail"),
    path('<int:pk>/update/', DrugUpdateView.as_view(), name="drugs-update"),
    path('new/', DrugCreateView.as_view(), name="drugs-create"),
    path('<int:pk>/delete', DrugDeleteView.as_view(), name="drugs-delete")
]