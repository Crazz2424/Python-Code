from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'base.html')

def index(request):
     template = loader.get_template('EQ_Website/base.html')
     context = {}
     return HttpResponse(template.render(context, request))