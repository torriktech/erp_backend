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
        'categories/',
        CategoryListView.as_view(),
        name='category-list'),
    path(
        'categories/create/',
        CategoryCreateView.as_view(),
        name='category-create'),
    path(
        'categories/<int:pk>/',
        CategoryDetailView.as_view(),
        name='category-detail'),
    path(
        'categories/<int:pk>/update/', 
        CategoryUpdateView.as_view(),
        name='category-update'
        ),
    path(
        'categories/<int:pk>/delete/',
        CategoryDeleteView.as_view(),
        name='category-delete'),
]
