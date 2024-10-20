from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserProfile

class UserProfileAdmin(UserAdmin):
    model = UserProfile
    list_display = ['username', 'email', 'first_name', 'last_name', 'phone_number', 'address', 'work', 'is_staff']
    
    # Add the extra fields to the fieldsets to display them in the admin
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('phone_number', 'address', 'work')}),
    )
    
    # This is for adding new users
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('first_name', 'last_name', 'phone_number', 'address', 'work')}),
    )

admin.site.register(UserProfile, UserProfileAdmin)
