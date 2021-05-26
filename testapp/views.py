from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView
from testapp.models import Company

class CompanyListview(ListView):
    model = Company
class CompanyDetailview(DetailView):
    model=Company