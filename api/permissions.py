from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied


class ClientProfilePermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True

        elif request.user.groups.filter(name='partner').exists():
            if request.method in permissions.SAFE_METHODS or request.method == 'POST':
                return True

        raise PermissionDenied

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True

        elif request.user.groups.filter(name='partner').exists():
            return True

        return obj.partner == request.user


class OfferPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True

        elif request.user.groups.filter(name__in=['organization', 'partner']).exists():
            if request.method in permissions.SAFE_METHODS:
                return True

        raise PermissionDenied

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True

        elif request.user.groups.filter(name='partner').exists():
            if request.method in permissions.SAFE_METHODS:
                return True

        return PermissionDenied


class RequestPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        elif request.user.groups.filter(name='partner').exists():
            if request.method in permissions.SAFE_METHODS or request.method == 'POST':
                return True
        elif request.user.groups.filter(name='organization').exists():
            if request.method in permissions.SAFE_METHODS or request.method == 'PATCH':
                return True

        raise PermissionDenied

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True

        elif request.user.groups.filter(name='partner').exists():
            if request.method in permissions.SAFE_METHODS:
                return True

        return PermissionDenied