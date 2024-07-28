"""bill of quantity urls"""
from django.urls import path
from .views import (
    BillOfQuantityCreateView, 
    BillOfQuantityRetrieveUpdateDestroyView,
    BillOfQuantityListByProjectView,
    KeyCreateView,
    KeyRetrieveUpdateDestroyView,
    KeyListView
)

urlpatterns = [
    # Bill of Quantity URLs
    path('', BillOfQuantityCreateView.as_view(), name='boq-create'),
    path('<int:pk>/',
         BillOfQuantityRetrieveUpdateDestroyView.as_view(), name='boq-detail'),
    path('projects/<int:project_id>/',
         BillOfQuantityListByProjectView.as_view(),
         name='boq-list-by-project'),

    # Key URLs
    path('keys/', KeyListView.as_view(), name='key-list'),
    path('keys/create/', KeyCreateView.as_view(), name='key-create'),
    path('keys/<int:pk>/',
         KeyRetrieveUpdateDestroyView.as_view(), name='key-detail'),
]
