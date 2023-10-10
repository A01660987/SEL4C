from rest_framework import authentication, permissions, serializers

from rest_framework import permissions

class CustomUserPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'POST':
            # Allow unauthenticated users to register
            return True

        if request.method == 'GET':
            # Allow all authenticated users to list users
            return request.user.is_admin

        return False

    def has_object_permission(self, request, view, obj):
        if request.method == 'GET':
            # Allow any user to retrieve user details
            return True

        if request.method == 'PUT':
            # Allow users to update their own data
            return request.user.is_authenticated and request.user == obj

        if request.method == 'DELETE':
            # Allow admin users to delete users
            return request.user.is_authenticated and request.user.is_staff

        return False





# """Allow authenticated users to use GET"""
# def permission_get(self):
#     if self.request.method == "GET":
#         return [permissions.IsAuthenticated()]
#     else:
#         return [permissions.IsAdminUser()]
    
# """Allow authenticated users to use POST"""
# def permission_post(self):
#     if self.request.method == "POST":
#         return [permissions.IsAuthenticated()]
#     else:
#         return [permissions.IsAdminUser()]

# """Allow unauthenticated users to register with POST and users to change own data"""
# def permission_user(self, request, view):
#     if self.request.method in ["POST"]:
#         return [permissions.AllowAny()]
#     elif self.request.method in ["PUT"]:
#         return request.user.is_authenticated and request.user == view.get_object()
    
#     return [permissions.IsAdminUser()]


"""Returns true when agreed on policy"""
def is_agreed_on_policy(value):
    if value != "true":
        raise serializers.ValidationError('Policies have to be accepted')