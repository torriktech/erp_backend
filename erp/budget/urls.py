# urls
from django.urls import path
from .views import (
    BudgetCreateView,
    BudgetListView,
    BudgetRetrieveView,
    BudgetUpdateView,
    BudgetDestroyView,
    BudgetListByProjectView
)

urlpatterns = [
    path(
        '',
        BudgetListView.as_view(),
        name='budget-list'
        ),
    path(
        'create/',
        BudgetCreateView.as_view(),
        name='budget-create'
    ),
    path(
        '<int:pk>/',
        BudgetRetrieveView.as_view(),
        name='budget-detail'
    ),
    path(
        '<int:pk>/update/',
        BudgetUpdateView.as_view(),
        name='budget-update'),
    path(
        '<int:pk>/delete/',
        BudgetDestroyView.as_view(),
        name='budget-delete'
    ),
    path(
        'project/<int:project_id>/',
        BudgetListByProjectView.as_view(),
        name='budgets-by-project'),
]
