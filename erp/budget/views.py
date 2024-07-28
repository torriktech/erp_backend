# budget views
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import Budget
from .serializers import BudgetSerializer


class BudgetCreateView(generics.CreateAPIView):
    """
    Create a new budget instance.
    """
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
            headers=headers
        )

class BudgetListView(generics.ListAPIView):
    """
    List all budget instances.
    """
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer


class BudgetRetrieveView(generics.RetrieveAPIView):
    """
    Retrieve a specific budget instance by its ID.
    """
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer


class BudgetUpdateView(generics.UpdateAPIView):
    """
    Update a specific budget instance by its ID.
    """
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(
            instance,
            data=request.data,
            partial=partial
        )
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)


class BudgetDestroyView(generics.DestroyAPIView):
    """
    Delete a specific budget instance by its ID.
    """
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


class BudgetListByProjectView(generics.ListAPIView):
    """
    View to list budgets based on project ID.
    """
    serializer_class = BudgetSerializer

    def get_queryset(self):
        project_id = self.kwargs['project_id']
        return Budget.objects.filter(project_id=project_id)
