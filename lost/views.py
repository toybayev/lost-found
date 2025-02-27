from django.shortcuts import render, redirect, get_object_or_404
from .models import Item, Category
from .forms import ItemForm

def index(request):
    items = Item.objects.all()
    return render(request, 'lost/item_list.html', {'items': items})

def detail(request, id):
    item = get_object_or_404(Item, id=id)
    return render(request, 'lost/item_detail.html', {'item': item})

def create(request):
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = ItemForm()
    return render(request, 'lost/item_form.html', {'form': form})

def update(request, id):
    item = get_object_or_404(Item, id=id)
    if request.method == "POST":
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = ItemForm(instance=item)
    return render(request, 'lost/item_form.html', {'form': form, 'item': item})

def delete(request, id):
    item = get_object_or_404(Item, id=id)
    if request.method == "POST":
        item.delete()
        return redirect("index")
    return render(request, 'lost/item_confirm_delete.html', {'item': item})
