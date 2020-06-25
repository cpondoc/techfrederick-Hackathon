from django.urls import path
from .views import (
    NarcoticListView,
    NarcoticDetailView,
    NarcoticUpdateView,
    NarcoticCreateView,
    NarcoticDeleteView
)
from . import views

urlpatterns = [
    path('', NarcoticListView.as_view(), name="narcotics-home"),
    path('<int:pk>/', NarcoticDetailView.as_view(), name="narcotics-detail"),
    path('<int:pk>/update/', NarcoticUpdateView.as_view(), name="narcotics-update"),
    path('new/', NarcoticCreateView.as_view(), name="narcotics-create"),
    path('<int:pk>/delete/', NarcoticDeleteView.as_view(), name="narcotics-delete")
]