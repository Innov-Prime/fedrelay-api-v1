from django.shortcuts import render


# Create your views here.

def documentation(request,kwargs):
    
    render(request,"documentation.py")
