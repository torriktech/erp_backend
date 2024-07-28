from rest_framework import generics
from .models import Supplier
from .serializers import SupplierSerializer


class SupplierListView(generics.ListAPIView):
    """
    View to list all Supplier instances.
    """
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer


class SupplierCreateView(generics.CreateAPIView):
    """
    View to create a new Supplier instance.
    """
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer


class SupplierDetailView(generics.RetrieveAPIView):
    """
    View to retrieve a specific Supplier instance by its ID.
    """
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer


class SupplierUpdateView(generics.UpdateAPIView):
    """
    View to update a specific Supplier instance by its ID.
    """
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer


class SupplierDestroyView(generics.DestroyAPIView):
    """
    View to delete a specific Supplier instance by its ID.
    """
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
