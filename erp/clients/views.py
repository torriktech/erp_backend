# views for clients
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import Client
from .serializers import ClientSerializer


class ClientListCreateView(generics.ListCreateAPIView):
    """
    View to list and create clients.
    
    Inherits from ListCreateAPIView to provide 'list' and 'create' actions.
    """
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    def create(self, request, *args, **kwargs):
        """
        Create a new client.

        Args:
            request (HttpRequest): The HTTP request object.

        Returns:
            Response: The HTTP response with created client data.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
            headers=headers
        )


class ClientRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    View to retrieve, update, and delete a client.
    Inherits from RetrieveUpdateDestroyAPIView to provide
    'retrieve', 'update', and 'destroy' actions.
    """
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    def update(self, request, *args, **kwargs):
        """
        Update an existing client.

        Args:
            request (HttpRequest): The HTTP request object.

        Returns:
            Response: The HTTP response with updated client data.
        """
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(
            instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        """
        Delete a client.

        Args:
            request (HttpRequest): The HTTP request object.

        Returns:
            Response: The HTTP response with no content status.
        """
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
