# urls.py
from django.urls import path
from .views import (
    SiteInspectionCreateView,
    SiteInspectionListView,
    SiteInspectionDetailView,
    SiteInspectionUpdateView,
    SiteInspectionDeleteView,
    SiteInspectionByProjectView
)

urlpatterns = [
    path(
        'site-inspections/',
        SiteInspectionListView.as_view(),
        name='site-inspection-list'),
    path(
        'site-inspections/create/',
        SiteInspectionCreateView.as_view(),
        name='site-inspection-create'),
    path(
        'site-inspections/<int:pk>/',
        SiteInspectionDetailView.as_view(),
        name='site-inspection-detail'),
    path(
        'site-inspections/<int:pk>/update/',
        SiteInspectionUpdateView.as_view(),
        name='site-inspection-update'),
    path(
        'site-inspections/<int:pk>/delete/',
        SiteInspectionDeleteView.as_view(),
        name='site-inspection-delete'),
    path(
        'site-inspections/project/<int:project_id>/',
        SiteInspectionByProjectView.as_view(),
        name='site-inspections-by-project'),
]
