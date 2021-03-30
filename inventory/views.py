from django.shortcuts import render

from inventory.models import * 

# Create your views here.

def index(request):
    product = Product.objects.all()

    product_count = Product.objects.all().count()

    products = {
        'products' : product,
        'product_count' : product_count,
    }
    return render(request, 'inventoryhome.html', products)

def productlist(request):
    product = Product.objects.all()

    products = {
        'products' : product,
    }
    return render(request, 'inventorylist.html', products)


def createproduct(request):
    if request.method == "POST":
        category = request.POST.get('category')
        print(request.POST)

    return render(request, 'createproduct.html')



