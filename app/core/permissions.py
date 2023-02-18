from rest_framework import permissions

class IsCreatorOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            # Allow safe methods (GET, HEAD, OPTIONS) for everyone
            return True
        elif request.method == 'POST':
            # Allow POST requests for authenticated users only
            return request.user.is_authenticated
        # Allow PUT, PATCH and DELETE requests for the owner of the object only
        return obj.user == request.user
    
    
class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return bool(request.user and request.user.is_staff)



class IsAuthenticatedOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_authenticated