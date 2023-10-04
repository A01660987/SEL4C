from rest_framework import authentication, permissions


# Permissions
def permission_get(self):
    if self.request.method == "GET":
        return [permissions.IsAuthenticated()]
    else:
        return [permissions.IsAdminUser()]
