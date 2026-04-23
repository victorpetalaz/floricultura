from django import forms
from .models import Flower

class FlowerForm(forms.ModelForm):
    class Meta:
        model = Flower
        fields = ['category', 'name', 'price', 'stock', 'image', 'is_available']
        
        widgets = {
            'category': forms.Select(attrs={'class': 'form-select bg-dark text-light border-secondary'}),
            'name': forms.TextInput(attrs={'class': 'form-control bg-dark text-light border-secondary'}),
            'price': forms.NumberInput(attrs={'class': 'form-control bg-dark text-light border-secondary', 'step': '0.01'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control bg-dark text-light border-secondary'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control bg-dark text-light border-secondary'}),
            'is_available': forms.CheckboxInput(attrs={'class': 'form-check-input bg-dark border-secondary'}),
        }