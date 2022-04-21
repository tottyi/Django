from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.registracia, name='register'),
    path('about/', views.about, name='about'),
    path('products/', views.products, name='products'),
    path('peoples/', views.peoples, name='peoples')
]
