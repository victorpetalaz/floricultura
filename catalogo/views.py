from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import FlowerForm
import traceback
from .models import Flower, Cart, CartItem

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

@login_required
def flower_create(request):
    if request.method == 'POST':
        form = FlowerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Success! New flower added to the catalog.')
            return redirect('storefront')
        else:
            messages.error(request, 'Please correct the errors in the form.')
    else:
        form = FlowerForm()
        
    return render(request, 'catalogo/flower_form.html', {'form': form, 'title': 'Add New Flower'})

@login_required
def flower_update(request, flower_id):
    flower = get_object_or_404(Flower, id=flower_id)
    
    if request.method == 'POST':
        form = FlowerForm(request.POST, request.FILES, instance=flower)
        if form.is_valid():
            form.save()
            messages.success(request, f'{flower.name} was updated successfully!')
            return redirect('flower_detail', flower_id=flower.id)
    else:
        form = FlowerForm(instance=flower)
        
    return render(request, 'catalogo/flower_form.html', {'form': form, 'title': 'Edit Flower', 'flower': flower})

@login_required
def flower_delete(request, flower_id):
    flower = get_object_or_404(Flower, id=flower_id)
    
    if request.method == 'POST':
        flower_name = flower.name
        flower.delete()
        messages.success(request, f'{flower_name} has been removed from the catalog.')
        return redirect('storefront')
        
    return render(request, 'catalogo/flower_confirm_delete.html', {'flower': flower})

@login_required
def test_add_to_cart(request, flower_id):
    try:
        flower = get_object_or_404(Flower, id=flower_id)
        if flower.stock > 0:
            cart, created = Cart.objects.get_or_create(user=request.user)
            cart_item, item_created = CartItem.objects.get_or_create(cart=cart, flower=flower)
            
            if not item_created:
                cart_item.quantity += 1
                cart_item.save()
            
            messages.success(request, f'Success! {flower.name} was added to your cart.')
        else:
            messages.error(request, f'Sorry, {flower.name} is currently out of stock.')
            
    except Exception as e:
        print("\n" + "="*50)
        print(f"[CRITICAL ERROR] Failed to save to cart database:")
        traceback.print_exc()
        print("="*50 + "\n")
        messages.error(request, 'An unexpected error occurred while saving to cart.')

    return redirect('flower_detail', flower_id=flower_id)