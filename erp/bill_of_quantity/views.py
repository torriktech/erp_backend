# key and BOQ view
from rest_framework import generics
from .models import BillOfQuantity, Key
from .serializers import BillOfQuantitySerializer, KeySerializer


class BillOfQuantityCreateView(generics.CreateAPIView):
    """
    View to create a new Bill of Quantity.
    """
    queryset = BillOfQuantity.objects.all()
    serializer_class = BillOfQuantitySerializer


class BillOfQuantityRetrieveUpdateDestroyView(
    generics.RetrieveUpdateDestroyAPIView
):
    """
    View to retrieve, update, and delete a Bill of Quantity.
    """
    queryset = BillOfQuantity.objects.all()
    serializer_class = BillOfQuantitySerializer


class BillOfQuantityListByProjectView(generics.ListAPIView):
    """
    View to list Bill of Quantity details based on project ID.
    """
    serializer_class = BillOfQuantitySerializer

    def get_queryset(self):
        project_id = self.kwargs['project_id']
        return BillOfQuantity.objects.filter(project_id=project_id)


# Key Views
class KeyCreateView(generics.CreateAPIView):
    """
    View to create a new Key.
    """
    queryset = Key.objects.all()
    serializer_class = KeySerializer


class KeyListView(generics.ListAPIView):
    """
    View to list all Keys.
    """
    queryset = Key.objects.all()
    serializer_class = KeySerializer


class KeyRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    View to retrieve, update, and delete a Key.
    """
    queryset = Key.objects.all()
    serializer_class = KeySerializer


