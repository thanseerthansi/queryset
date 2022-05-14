"""studypro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from selectedrelated import views

urlpatterns = [
    
    path('book/',views.booksget),
    path('store/',views.storeget),
    path('transaction/',views.Transaction),
    path('aggregate/',views.aggregate),
    path('annotate/',views.annotate),
    path('values/',views.values),
    path('f/',views.f),
    path('manager/',views.manager),
    path('revererelation/',views.revererelation),
    path('bulkcreate/',views.bulkcreate),
    path('bulkupdate/',views.bulkupdate),
    path('defer/',views.defer),
]
