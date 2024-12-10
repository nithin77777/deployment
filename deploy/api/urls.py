from django.contrib import admin
from django.urls import path
from .views import UserCRUSView

urlpatterns = [
    path('crus/', UserCRUSView.as_view(), name="crus"),
    path('crus/<int:pk>/',UserCRUSView.as_view(), name="crus put")
]