'''procurement routes'''
from django.urls import path
from .views import (
    ProcurementListCreateAPIView,
    ProcurementDetailAPIView
    )

urlpatterns = [
    path('',
         ProcurementListCreateAPIView.as_view(),
         name='procurement-list-create'),
    path('<int:pk>/',
         ProcurementDetailAPIView.as_view(),
         name='procurement-detail'),
]
