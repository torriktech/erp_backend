"""procurement controllers"""
from rest_framework import generics
from .models import Procurement
from .serializers import ProcurementSerializer


class ProcurementListCreateAPIView(generics.ListCreateAPIView):
    """
    API endpoint for listing and creating Procurement instances.

    GET:
    Returns a list of all Procurement instances.

    POST:
    Creates a new Procurement instance.

    Serializer:
    - ProcurementSerializer: Handles serialization and
    - deserialization of Procurement instances.
    """

    queryset = Procurement.objects.all()
    serializer_class = ProcurementSerializer


class ProcurementDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint for retrieving, updating, and deleting a Procurement instance.

    GET:
    Retrieves details of a specific Procurement instance.

    PUT/PATCH:
    Updates all fields/partial fields of a specific Procurement instance.

    DELETE:
    Deletes a specific Procurement instance.

    Serializer:
    - ProcurementSerializer: Handles serialization and
    - deserialization of Procurement instances.
    """

    queryset = Procurement.objects.all()
    serializer_class = ProcurementSerializer
