# views
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import Item
from .serializers import ItemSerializer


class ItemListCreateView(generics.ListCreateAPIView):
    """
    View to list and create items.
    """
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def create(self, request, *args, **kwargs):
        """
        Create a new item.
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


class ItemRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    View to retrieve, update, and delete an item.
    """
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def update(self, request, *args, **kwargs):
        """
        Update an existing item.
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
        Delete an item.
        """
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


class ItemListByCategoryView(generics.ListAPIView):
    """
    View to list items based on inventory.
    """
    serializer_class = ItemSerializer

    def get_queryset(self):
        """
        Get the queryset of items filtered by category.
        """
        category_id = self.kwargs['category_id']
        return Item.objects.filter(category_id=category_id)


class ItemIncrementView(generics.UpdateAPIView):
    """
    View to increment the quantity of an item.
    """
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def patch(self, request, *args, **kwargs):
        """
        Increment item quantity.
        """
        item = self.get_object()
        increment_by = request.data.get('quantity', 0)
        if increment_by < 0:
            return Response({
                "error": "Increment value must be non-negative"},
                status=status.HTTP_400_BAD_REQUEST)
        item.quantity += increment_by
        item.save()
        serializer = self.get_serializer(item)
        return Response(serializer.data)


class ItemDecrementView(generics.UpdateAPIView):
    """
    View to decrement the quantity of an item.
    """
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def patch(self, request, *args, **kwargs):
        """
        Decrement item quantity.
        """
        item = self.get_object()
        decrement_by = request.data.get('quantity', 0)
        if decrement_by < 0:
            return Response(
                {"error": "Decrement value must be non-negative"},
                status=status.HTTP_400_BAD_REQUEST)
        if decrement_by > item.quantity:
            return Response(
                {"error": "Decrement value exceeds available quantity"},
                status=status.HTTP_400_BAD_REQUEST)
        item.quantity -= decrement_by
        item.save()
        serializer = self.get_serializer(item)
        return Response(serializer.data)
