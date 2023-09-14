from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views import generic

# Create your views here.

class index(generic.ListView):
    template_name = 'mainsite/index.html'

    def get_queryset(self):
        return {}

