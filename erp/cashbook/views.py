from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import Cashbook
from .serializers import CashbookSerializer


class CashbookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Cashbook.objects.all()
    serializer_class = CashbookSerializer

class CashbookRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cashbook.objects.all()
    serializer_class = CashbookSerializer
