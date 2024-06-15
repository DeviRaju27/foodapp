from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item
from .forms import ItemForm

def index(request):
    items = Item.objects.all()
    context = {
        "items" : items,
    }
    return render(request,"menu/index.html", context)
    

def detail(request, item_id):
    item = Item.objects.get(pk=item_id)
    context = {
        "item" : item,
    }
    return render(request, "menu/detail.html", context)
    
def add_item(request):

    form_obj = ItemForm(request.POST or None)

    if form_obj.is_valid():
        form_obj.save()
        return redirect('food:index')

    return render(request, "menu/form.html", {'form': form_obj})

def update_item(request, id):
    item_id = Item.objects.get(id = id)
    form_obj = ItemForm(request.POST or None, instance= item_id)

    if form_obj.is_valid():
        form_obj.save()
        return redirect('food:index')
    
    context = {
        "id" : item_id,
        "form": form_obj
    }
    
    return render(request, "menu/form.html", context )

