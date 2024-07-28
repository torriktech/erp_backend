# urls for clients
from django.urls import path
from .views import ClientListCreateView, ClientRetrieveUpdateDestroyView

urlpatterns = [
    path('',
         ClientListCreateView.as_view(), name='client-list-create'),
    path(
        '<int:pk>/',
        ClientRetrieveUpdateDestroyView.as_view(),
        name='client-retrieve-update-destroy'),
]
