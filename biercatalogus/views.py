from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Bier

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def product_list(request):
    products = Bier.objects.filter(available=True).order_by('quantity')
    return render(request,
        'biercatalogus/list.html',
        {'products': products})

def product_detail(request, id):
    product = get_object_or_404(Bier, id=id)
    return render(request,
        'biercatalogus/detail.html',
        {'product': product})

def ik_wil(request, id):
    product = get_object_or_404(Bier, id=id)
    products = Bier.objects.filter(available=True).order_by('quantity')
    product.quantity = product.quantity_subtract()
    product.save()
    return render(request,
        'biercatalogus/list.html',
        {'products': products})

