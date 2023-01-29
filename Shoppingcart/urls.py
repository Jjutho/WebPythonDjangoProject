from django.urls import path
from . import views

urlpatterns = [
    path('show/', views.show_shopping_cart, name='cart'),
    path('pay/', views.pay, name='pay'),
]