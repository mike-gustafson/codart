from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import Profile, Dart

# unregister groups
admin.site.unregister(Group)

# Mix profile info into user info
class ProfileInline(admin.StackedInline):
    model = Profile

# Extend User model
class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ["username", "email", "first_name", "last_name", "is_active", "is_staff", "is_superuser"]
    inlines = [ProfileInline]

# Unregister initial User model
admin.site.unregister(User)

#register new User model
admin.site.register(User, UserAdmin)
# admin.site.register(Profile)

#register darts
admin.site.register(Dart)