from rest_framework import authentication, permissions, serializers


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


"""Returns true when agreed on policy"""
def is_agreed_on_policy(value):
    if value != "true":
        raise serializers.ValidationError('Policies have to be accepted')