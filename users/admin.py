from django.contrib import admin
from .models import Profile
from django.contrib.auth.models import User

class ProfileInline(admin.StackedInline):  # or TabularInline if you prefer a more compact display
    model = Profile


class UserAdmin(admin.ModelAdmin):
    inlines = [ProfileInline]

admin.site.unregister(User)  # Unregister the default User admin
admin.site.register(User, UserAdmin)  # Register User admin with Profile inline
