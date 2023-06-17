from typing import ItemsView
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404, render
from .forms import addNewItem
import products

from products.apps import ProductsConfig
from .models import Items


def index(request):
    product_list = Items.objects.order_by('price')[:100]
    context = {'product_list': product_list}
    return render(request, 'products/index.html', context)


def detail(request, product_id):
    return HttpResponse("You're looking at product: %s." % product_id)

def addProduct(request):
    if(request.method=="POST"):
        form=addNewItem(request.POST)
        if form.is_valid():
            n=form.cleaned_data["item_name"]
            pr=form.cleaned_data["price"]
            st=form.cleaned_data["stock"]
            item = Items.objects.create(item_name=n, price=pr, stock=st)
            print(item)
        return render(request, 'products/result.html', {"item":item})
        

    else:
        form=addNewItem()
    return render(request, 'products/addProduct.html', {"form":form})


def NewAdded(request):
    item = Items.objects[:1]
    print(item.item_name)
    context = {'item': item}
    return render(request, 'products/result.html', context)



