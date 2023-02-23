from django.shortcuts import render, redirect
from django.contrib import messages
import os
from .models import Item
# Create your views here.
def index(request):
    products = Item.objects.all()
    context = {'products':products}
    return render(request, 'products/index.html', context)



def addProduct(request):
    if request.method == "POST":
        prod = Item()
        prod.name = request.POST.get('name')
        prod.description = request.POST.get('description')
        prod.price = request.POST.get('price')

        if len(request.FILES) != 0:
            prod.image = request.FILES['image']

        prod.save()
        messages.success(request, "Product Added Successfully")
        return redirect('/')
    return render(request, 'products/add.html')


def editProduct(request, pk):
    prod = Item.objects.get(id=pk)

    if request.method == "POST":
        if len(request.FILES) != 0:
            if len(prod.image) > 0:
                os.remove(prod.image.path)
            prod.image = request.FILES['image']
        prod.name = request.POST.get('name')
        prod.description = request.POST.get('description')
        prod.price = request.POST.get('price')
        prod.save()
        messages.success(request, "Product Updated Successfully")
        return redirect('/')

    context = {'prod':prod}
    return render(request, 'products/edit.html', context)

def deleteProduct(request, pk):
    prod = Item.objects.get(id=pk)
    if len(prod.image) > 0:
        os.remove(prod.image.path)
    prod.delete()
    messages.success(request,"Product Deleted Successfuly")
    return redirect('/')