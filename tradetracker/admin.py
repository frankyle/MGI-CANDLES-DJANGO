from django.contrib import admin
from .models import TradeTracker

# Define the admin interface for the TradeTracker model
@admin.register(TradeTracker)
class TradeTrackerAdmin(admin.ModelAdmin):
    list_display = ('user', 'currency_pair', 'pips_gained', 'pips_lost', 'created_at')  # Fields to display in the list view
    search_fields = ('user__username', 'currency_pair')  # Allow searching by user and currency pair
    list_filter = ('currency_pair', 'created_at')  # Filter by currency pair and creation date
    ordering = ('-created_at',)  # Order by most recent trades first
    readonly_fields = ('created_at', 'updated_at')  # Make timestamps read-only
