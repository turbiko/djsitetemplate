from django.contrib import admin
from .models import UserProfile, Person1C


# class UserProfileAdmin(admin.ModelAdmin):
#     readonly_fields = ('created',)

admin.site.register(UserProfile)
admin.site.register(Person1C)