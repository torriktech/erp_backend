from django.urls import path
from .views import CashbookListCreateAPIView, CashbookRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('create/', CashbookListCreateAPIView.as_view(), name='cashbook-list-create'),
    path('<int:pk>/', CashbookRetrieveUpdateDestroyAPIView.as_view(), name='cashbook-detail'),
]
