from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def EQ_page(request):
    return render(request,'EQ_page.html'),
    