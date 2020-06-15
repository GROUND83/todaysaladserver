from rest_framework.permissions import BasePermission


class IsSelf(BasePermission):
    def has_object_permission(self, request, view, user):
        print(self, request, view, user)
        print(bool(user == request.user))
        return bool(user == request.user)
