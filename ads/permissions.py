from rest_framework.permissions import BasePermission

from users.models import User


class IsOwner(BasePermission):
    message = "Editing only for owners"

    def has_object_permission(self, request, view, obj):
        return request.user == obj.owner


class IsOwnerOrStaff(BasePermission):
    message = "Only owners and staff can update/delete this"

    def has_object_permission(self, request, view, obj):
        return request.user == obj.owner or request.user.role in [User.ADMIN, User.MODERATOR]


