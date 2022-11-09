from django.urls import path
from . import views

urlpatterns = [
    path('show/', views.GameListView.as_view(), name='game-list'),
    path('show/<int:pk>/', views.GameDetailView.as_view(), name='game-detail'),
    path('add/', views.GameCreateView.as_view(), name='game-create'),
    path('delete/', views.GameDeleteView.as_view(), name='game-delete'),
]
