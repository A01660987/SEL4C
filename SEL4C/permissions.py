from rest_framework import authentication, permissions


"""Allow authenticated users to use GET"""
def permission_get(self):
    if self.request.method == "GET":
        return [permissions.IsAuthenticated()]
    else:
        return [permissions.IsAdminUser()]

"""Allow unauthenticated users to POST and PUT"""
def permission_user(self):
    if self.request.method in ["POST", "PUT"]:
        return [permissions.AllowAny()]
    else:
        return [permissions.IsAdminUser()]
