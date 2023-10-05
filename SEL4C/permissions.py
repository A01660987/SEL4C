from rest_framework import permissions


"""Returns true when the user requests a list and is authenticated"""


class list_authenticated(permissions.BasePermission):
    def has_permission(self, request, view):
        if view.action == "list":
            return request.user.is_authenticated
        else:
            return request.user.is_superuser


"""Returns true when the user requests a own object and is authenticated"""


class list_authenticated(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if view.action == "retreive":
            return obj.user == request.user
        else:
            return request.user.is_superuser


"""Returns true when non-authorized persons want to create a user and authenticated users want to see or change their own account"""


class user_permissions(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if view.action in ["retrieve", "update", "partial_update"]:
            return obj.user == request.user
        elif view.action == "create":
            return True
        else:
            request.user.is_superuser


# from rest_framework import authentication, permissions


# # Permissions
# def permission_get(self):
#     if self.request.method == "GET":
#         return [permissions.IsAuthenticated()]
#     else:
#         return [permissions.IsAdminUser()]


# def permission_user(self):
#     if self.request.method in ["POST", "PUT"]:
#         return [permissions.AllowAny()]
#     else:
#         return [permissions.IsAdminUser()]
