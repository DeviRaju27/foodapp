from django.shortcuts import render
from django.http import HttpResponse
from .models import Item

def index(request):
    items = Item.objects.all()
    return HttpResponse(items)
    

def item(request):
    items = Item.objects.all()
    return HttpResponse(items)
    

