from django.shortcuts import render
from django.http import HttpResponse
import os

# Create your views here.

def help(request):
    help_dict = {'help_data':"HALP!"}
    return render(request, 'fossgis_karte/help.html',context=help_dict)