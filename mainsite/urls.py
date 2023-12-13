from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index.as_view(), name="index"),
    # path('resume/', views.pdf_view, name="resume"),
    path('', views.museum.as_view(), name="museum"),
    path('museum/pdf/', views.museumpdf, name="museumpdf"),
    path('museum/docx/', views.museumdocx, name="museumdocx"),
    path('museum/wc/', views.museumworkscited, name="museumwc"),
]