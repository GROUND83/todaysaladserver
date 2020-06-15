from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    def has_object_permission(self, request, view, destination):
        print("isOwner")
        print(destination.user)
        print(request.user)
        return destination.user == request.user
