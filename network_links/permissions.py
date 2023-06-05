from rest_framework import permissions


class IsActiveStaffPermission(permissions.BasePermission):
    """Разрешения пользования активным пользователям и персоналу"""
    def has_permission(self, request, view):
        return request.user and (request.user.is_active or request.user.is_staff)



