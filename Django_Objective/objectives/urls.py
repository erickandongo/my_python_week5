from django.urls import path 
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("objective_details//<int:objective_id>/", views.objective_details, name="objective-details")
]
