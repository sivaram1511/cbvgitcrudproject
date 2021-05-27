from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView,CreateView,UpdateView
from testapp.models import Company
from django.urls import reverse_lazy
class CompanyListview(ListView):
    model = Company
class CompanyDetailview(DetailView):
    model=Company
class CompanyCreateView(CreateView):
    model=Company
    fields = ('name','location','ceo')
class CompanyUpdateview(UpdateView):
    model=Company
    fields = ('name','ceo')
class CompanyDeleteView(DetailView):
    model = Company
    success_url=reverse_lazy('/')
