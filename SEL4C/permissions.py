from rest_framework import authentication, permissions


# Permissions
def permission_get(self):
    if self.request.method == "GET":
        return [permissions.IsAuthenticated()]
    else:
        return [permissions.IsAdminUser()]


def permission_user(self):
    if self.request.method in ["POST", "PUT"]:
        return [permissions.AllowAny()]
    else:
        return [permissions.IsAdminUser()]
