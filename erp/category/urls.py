from django.urls import path
from .views import (
    CategoryCreateView,
    CategoryUpdateView,
    CategoryDeleteView,
    CategoryListView,
    CategoryDetailView
)

urlpatterns = [
    path(
        '',
        CategoryListView.as_view(),
        name='category-list'),
    path(
        'create/',
        CategoryCreateView.as_view(),
        name='category-create'),
    path(
        'detailed/<int:pk>/',
        CategoryDetailView.as_view(),
        name='category-detail'),
    path(
        'update/<int:pk>/', 
        CategoryUpdateView.as_view(),
        name='category-update'
        ),
    path(
        'delete/<int:pk>/',
        CategoryDeleteView.as_view(),
        name='category-delete'),
]
