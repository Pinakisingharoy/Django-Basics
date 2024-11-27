from django.shortcuts import render
from .models import Invoice


# Create your views here.

def list(request):
    invoice=Invoice.objects.all()
    return render(request,'myapp/list.html',{'invoice':invoice})
