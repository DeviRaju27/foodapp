from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item
from .forms import ItemForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView


class IndexClassView(ListView):
    model = Item
    template_name = 'menu/index.html'
    context_object_name = 'items'

class DetailView(DetailView):
    model = Item
    template_name = 'menu/detail.html'   

class CreateItem(CreateView):
    
    model = Item
    fields = ['item_name', 'item_desc', 'item_price', 'item_image']
    template_name = "menu/create-item.html"

    def form_valid(self, form):
        form.instance.user_name = self.request.user
    
        return super().form_valid(form)


def update_item(request, id):
    item_id = Item.objects.get(id = id)
    form_obj = ItemForm(request.POST or None, instance= item_id)

    if form_obj.is_valid():
        form_obj.save()
        return redirect('menu:index')
    
    context = {
        "id" : item_id,
        "form": form_obj
    }
    
    return render(request, "menu/form.html", context )

def delete_item(request, id):
    item = Item.objects.get(id = id)

    context = {
        "item": item,
    }

    if request.method == 'POST':
        item.delete()
        return redirect('menu:index')
    
    return render(request, "menu/delete-item.html", context)

            

