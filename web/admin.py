from django.contrib import admin
from django.contrib.auth.models import Group as authGroup
from SEL4C.models import *

admin.site.unregister(authGroup)
admin.site.register(User)
admin.site.register(Group)
admin.site.register(Institution)
admin.site.register(Discipline)
admin.site.register(Degree)
admin.site.register(Student)