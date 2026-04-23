from django.urls import path
from . import views

urlpatterns = [
    path('', views.storefront, name='storefront'),
    path('profile/', views.profile, name='profile'),
    path('flower/<int:flower_id>/', views.flower_detail, name='flower_detail'),
    path('flower/<int:flower_id>/add/', views.test_add_to_cart, name='test_add_to_cart'),
    path('flower/new/', views.flower_create, name='flower_create'),
    path('flower/<int:flower_id>/edit/', views.flower_update, name='flower_update'),
    path('flower/<int:flower_id>/delete/', views.flower_delete, name='flower_delete'),
]