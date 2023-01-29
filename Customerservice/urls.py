from django.urls import path
from . import views

urlpatterns = [
    path('delete/', views.CommentDeleteView.as_view(), name='comment-delete'),
    path('edit/<int:pk>/', views.CommentEditView.as_view(), name='comment-edit'),
    path('editdelete/<int:pk>/', views.comment_edit_delete, name='comment-edit-delete'),
]