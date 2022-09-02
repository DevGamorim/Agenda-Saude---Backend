from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class HomePageView(TemplateView, IsAuthenticated):
    template_name = 'Pages/home.html'