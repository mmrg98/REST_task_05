from rest_framework.permissions import BasePermission

class IsOwner(BasePermission):
    message = "not allowed"

    def has_object_permission(self, request, view, obj):
        if (obj.user == request.user):
            return True
        else:
            return False
