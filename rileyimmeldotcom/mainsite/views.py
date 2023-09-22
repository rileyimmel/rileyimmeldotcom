import os

from django.shortcuts import render
from django.http import HttpResponse, FileResponse, Http404
from django.template import loader
from django.views import generic


# Create your views here.

class index(generic.ListView):
    template_name = 'mainsite/index.html'

    def get_queryset(self):
        return {}


def pdf_view(request):
    with open('./mainsite/static/resume.pdf', 'rb') as pdf:
        response = HttpResponse(pdf.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'inline;filename=mypdf.pdf'
        return response