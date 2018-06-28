from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from user.models import Person


class PersonInline(admin.StackedInline):
    model = Person
    verbose_name_plural = 'Person'


class UserAdmin(BaseUserAdmin):
    inlines = (PersonInline,)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
