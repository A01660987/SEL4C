from django.contrib import admin
from django.contrib.auth.models import Group as authGroup
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from SEL4C.models import *

class UserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = User
    list_display = ('username', 'name', 'first_lastname', 'second_lastname', 'is_staff')
    list_filter = ('is_staff',)
    fieldsets = (
        (None, {'fields': ('username', 'password', 'name', 'first_lastname', 'second_lastname')}),
        ('Permisos', {'fields': ('is_staff', 'is_superuser', 'is_active',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'name', 'first_lastname', 'second_lastname',)
            }
        ),
        ('Permisos', {
            'classes': ('wide',),
            'fields': ('is_staff', 'is_superuser',)
            }
        )
    )
    search_fields = ('username',)
    ordering = ('username',)

admin.site.unregister(authGroup)
admin.site.register(User, UserAdmin)
admin.site.register(Group)
admin.site.register(Institution)
admin.site.register(Discipline)
admin.site.register(Degree)
admin.site.register(Student)