urlpatterns = [
    path('', views.storefront, name='storefront'),
    path('profile/', views.profile, name='profile'),
]