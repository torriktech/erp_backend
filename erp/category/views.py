from rest_framework import generics
from .models import Category
from .serializers import CategorySerializer


class BaseCategoryView:
    """
    Base view for Category operations.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryCreateView(
        BaseCategoryView,
        generics.CreateAPIView):
    """
    API view to create a new Category.
    Handles POST requests.
    """
    pass


class CategoryUpdateView(
        BaseCategoryView,
        generics.UpdateAPIView):
    """
    API view to update an existing Category.
    Handles PUT and PATCH requests.
    """
    pass


class CategoryDeleteView(
        BaseCategoryView,
        generics.DestroyAPIView):
    """
    API view to delete an existing Category.
    Handles DELETE requests.
    """
    pass


class CategoryListView(
        BaseCategoryView,
        generics.ListAPIView):
    """
    API view to list all Categories.
    Handles GET requests.
    """
    pass


class CategoryDetailView(
        BaseCategoryView,
        generics.RetrieveAPIView):
    """
    API view to retrieve a single Category.
    Handles GET requests.
    """
    pass
