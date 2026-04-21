from django.shortcuts import render
from .models import Flower

def storefront(request):
    flowers = Flower.objects.filter(is_available=True)
    return render(request, 'catalogo/storefront.html', {'flowers': flowers})