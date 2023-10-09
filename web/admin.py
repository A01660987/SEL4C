from django.contrib import admin
from django.contrib.auth.models import Group as authGroup
from SEL4C.models import *
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

class UserAdmin(BaseUserAdmin):

    model = User
    # extra = 1

admin.site.unregister(authGroup)
admin.site.register(User, UserAdmin)
admin.site.register(Group)
admin.site.register(Institution)
admin.site.register(Discipline)
admin.site.register(Degree)
admin.site.register(Student)