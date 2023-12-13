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

def museumpdf(request):
    with open('./mainsite/static/Immel_Breaking_Bad_Final.pdf', 'rb') as pdf:
        response = HttpResponse(pdf.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'inline;filename=mypdf.pdf'
        return response


def museumdocx(request):
    with open('./mainsite/static/Immel_Breaking_Bad_Final.docx', 'rb') as docx_file:
        response = HttpResponse(docx_file.read(), content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
        response['Content-Disposition'] = 'attachment; filename="Immel_Breaking_Bad_Final.docx"'
        return response

def museumworkscited(request):
    with open('./mainsite/static/workscited.pdf', 'rb') as pdf:
        response = HttpResponse(pdf.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'inline;filename=mypdf.pdf'
        return response

class museum(generic.ListView):
    template_name = 'mainsite/museumindex.html'

    def get_queryset(self):
        return {}
