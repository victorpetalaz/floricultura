from django.urls import path
from . import views

urlpatterns = [
    path('', views.storefront, name='storefront'),
    path('profile/', views.profile, name='profile'),
    path('flower/<int:flower_id>/', views.flower_detail, name='flower_detail'),
    path('flower/<int:flower_id>/add/', views.test_add_to_cart, name='test_add_to_cart'),
]