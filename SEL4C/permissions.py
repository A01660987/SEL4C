from rest_framework import authentication, permissions, serializers

from rest_framework import permissions

"""Registering unauthenticated users, get and update own data is possible for authenticated users """
class CustomUserPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'POST':
            # Allow unauthenticated users to register
            return True

        if request.method == 'GET':
            # Allow admin users to list users
            return request.user.is_authenticated and request.user.is_admin
        
        return False

    def has_object_permission(self, request, view, obj):
        if request.method in ['GET', 'PUT']:
            # Allow users to retrieve and update own user details
            return request.user.is_authenticated and request.user == obj

        if request.method == 'DELETE':
            # Allow admin users to delete users
            return request.user.is_authenticated and request.user.is_admin

        return False


"""Allow only uploading files when authenticated"""
class FileUploadPermission(permissions.BasePermission):

    """Authenticated users are allowed to commit files"""
    def has_permission(self, request, view):
        if request.method == 'POST':
            return request.user.is_authenticated
        
        return False
    
    """No changes possible to commited files"""
    def has_object_permission(self, request, view, obj):
        return False



"""Returns true when agreed on policy"""
def is_agreed_on_policy(value):
    if not value:
        raise serializers.ValidationError('Policies have to be accepted')
    return True