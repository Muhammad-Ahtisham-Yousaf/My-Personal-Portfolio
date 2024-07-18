from django.shortcuts import render,redirect
from django.http import HttpResponse
from .djangoForms.clients import ClientForm
from .models import Client
# Create your views here.
def Portfolio(request):
    if request.method =='GET':
        client = ClientForm ()
        return render (request,'businiss.html',{'client':client})
    else:
        client = ClientForm(request.POST)
        if client.is_valid():
            client.save()
            return redirect(Portfolio)


def About_Me(request):
    return render (request,'About.html')


def form_sub (request):
    return render (request,'form_sub.html')

def clients_details(request):
   clients_details=Client.objects.all()
   return render (request,'Clients.html',{'clients_details': clients_details})
 
