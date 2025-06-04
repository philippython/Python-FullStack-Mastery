from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsStudentOrReadOnly(BasePermission):
    message = 'Only student who owns the account can modify data'

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        else:
            return obj.user == request.user