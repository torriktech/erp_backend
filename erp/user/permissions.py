from rest_framework.permissions import BasePermission


class IsAdministrator(BasePermission):
    """
    Custom permission to only allow administrators.
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_administrator()


class IsClient(BasePermission):
    """
    Custom permission to only allow clients.
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_client()


class IsStaff(BasePermission):
    """
    Custom permission to only allow staff members.
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_staff()


class IsAdminOrClient(BasePermission):
    """
    Custom permission to allow only administrators
    and clients to view project details.
    """
    def has_permission(self, request, view):
        # Check if the user is authenticated and has
        # the role of either 'administrator' or 'client'
        return request.user.is_authenticated and (
            request.user.roles == 'administrator' or
            request.user.roles == 'client'
        )
