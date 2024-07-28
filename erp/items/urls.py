"""urls for items"""
from django.urls import path
from .views import (
    ItemListCreateView,
    ItemRetrieveUpdateDestroyView,
    ItemListByCategoryView,
    ItemIncrementView,
    ItemDecrementView
)

urlpatterns = [
    path(
        '',
        ItemListCreateView.as_view(), 
        name='item-list-create'),
    path(
        '<int:pk>/',
        ItemRetrieveUpdateDestroyView.as_view(),
        name='item-retrieve-update-destroy'),
    path(
        'category/<int:category_id>/', 
        ItemListByCategoryView.as_view(),
        name='item-list-by-category'),
    path(
        '<int:pk>/increment/',
        ItemIncrementView.as_view(),
        name='item-increment'),
    path(
        '<int:pk>/decrement/',
        ItemDecrementView.as_view(),
        name='item-decrement'),
]

