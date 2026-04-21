from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import traceback
from .models import Flower

@login_required
def storefront(request):
    flowers = Flower.objects.filter(is_available=True)
    return render(request, 'catalogo/storefront.html', {'flowers': flowers})

@login_required
def profile(request):
    return render(request, 'catalogo/profile.html', {'user': request.user})

@login_required
def flower_detail(request, flower_id):
    flower = get_object_or_404(Flower, id=flower_id, is_available=True)
    return render(request, 'catalogo/flower_detail.html', {'flower': flower})

@login_required
def test_add_to_cart(request, flower_id):
    flower = get_object_or_404(Flower, id=flower_id)
    
    if flower.stock > 0:
        messages.success(request, f'Success! {flower.name} was added to your cart.')
    else:
        messages.error(request, f'Sorry, {flower.name} is currently out of stock.')
        
    return redirect('flower_detail', flower_id=flower.id)

@login_required
def test_add_to_cart(request, flower_id):
    try:
        flower = get_object_or_404(Flower, id=flower_id)
        
        if flower.stock > 0:
            messages.success(request, f'Success! {flower.name} was added to your cart.')
        else:
            messages.error(request, f'Sorry, {flower.name} is currently out of stock.')
            
    except Exception as e:
        print("\n" + "="*50)
        print(f"[CRITICAL ERROR] Failed to process cart action:")
        traceback.print_exc()
        print("="*50 + "\n")
        messages.error(request, 'An unexpected error occurred. Please try again later.')

    return redirect('flower_detail', flower_id=flower_id)