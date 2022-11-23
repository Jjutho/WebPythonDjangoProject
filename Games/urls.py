from django.urls import path
from . import views

urlpatterns = [
    path('show/', views.game_list, name='game-list'),
    path('show/<int:pk>/', views.game_detail, name='game-detail'),
    path('add/', views.game_create, name='game-create'),
    path('delete/<int:pk>/', views.game_delete, name='game-delete'),
    path('delete/<int:pk>/comment/<int:ck>/', views.comment_delete, name='comment-delete'),
    path('show/<int:pk>/comment/<int:ck>/vote/<str:up_or_down>/', views.comment_vote, name='comment-vote'),
]
