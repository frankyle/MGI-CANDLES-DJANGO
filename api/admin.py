from django.contrib import admin
from .models import User, Profile  # Import models from the same app

# User Admin Configuration
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_staff', 'is_active', 'date_joined')  # Added useful fields
    list_filter = ('is_staff', 'is_active', 'is_superuser')  # Add filters
    search_fields = ('username', 'email')  # Add search functionality


# Profile Admin Configuration
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'full_name', 'verified', 'bio')  # Added 'bio'
    list_editable = ('verified',)  # Tuple for single editable field
    list_filter = ('verified',)   # Filter by verification status
    readonly_fields = ('user',)  # Prevent modifying the user field in the admin

# Register the models with their custom configurations
admin.site.register(User, UserAdmin)
admin.site.register(Profile, ProfileAdmin)
