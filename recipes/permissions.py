# from rest_framework.permissions import BasePermission

# class IsOwnerOrReadOnly(BasePermission):
#     def has_object_permission(self, request, view, obj):
#         if request.method in ['GET', 'HEAD', 'OPTIONS']:
#             return True
#         return obj.created_by == request.user


from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsOwnerOrReadOnly(BasePermission):
    """
    Custom permission to allow only the owner of an object to edit or delete it.
    """

    def has_object_permission(self, request, view, obj):
        # Allow safe methods for everyone (GET, HEAD, OPTIONS)
        if request.method in SAFE_METHODS:
            return True

        # Otherwise, only the owner has permission
        return obj.created_by == request.user