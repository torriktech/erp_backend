from rest_framework import generics
from .models import SiteInspection
from .serializers import SiteInspectionSerializer


class SiteInspectionCreateView(generics.CreateAPIView):
    """
    API view to create a new SiteInspection.
    """
    queryset = SiteInspection.objects.all()
    serializer_class = SiteInspectionSerializer


class SiteInspectionListView(generics.ListAPIView):
    """
    API view to list all SiteInspections.
    """
    serializer_class = SiteInspectionSerializer

    def get_queryset(self):
        """
        Return a queryset with related project_operation
        and inspection_officer fields.
        """
        return SiteInspection.objects.select_related(
            'project_operation', 'inspection_officer').all()


class SiteInspectionDetailView(generics.RetrieveAPIView):
    """
    API view to retrieve a single SiteInspection.
    """
    serializer_class = SiteInspectionSerializer

    def get_object(self):
        """
        Retrieve a single SiteInspection with related
        projects_inspection and inspection_officer fields.
        """
        queryset = SiteInspection.objects.select_related(
            'projects_inspection', 'inspection_officer')
        obj = generics.get_object_or_404(queryset, pk=self.kwargs['pk'])
        return obj
    

class SiteInspectionUpdateView(generics.UpdateAPIView):
    """
    API view to update an existing SiteInspection.
    """
    queryset = SiteInspection.objects.all()
    serializer_class = SiteInspectionSerializer


class SiteInspectionDeleteView(generics.DestroyAPIView):
    """
    API view to delete an existing SiteInspection.
    """
    queryset = SiteInspection.objects.all()
    serializer_class = SiteInspectionSerializer


class SiteInspectionByProjectView(generics.ListAPIView):
    """
    API view to list SiteInspections by ProjectOperation.
    """
    serializer_class = SiteInspectionSerializer

    def get_queryset(self):
        """
        Filter the queryset based on the project_operation ID.
        """
        project_id = self.kwargs['project_id']
        return SiteInspection.objects.filter(
            project_id=project_id
        )
