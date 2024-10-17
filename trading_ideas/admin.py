from django.contrib import admin
from .models import TraderIdea

class TraderIdeaAdmin(admin.ModelAdmin):
    list_display = ('user', 'trade_signal', 'currency_pair', 'post_date_time', 'publisher_trader', 'trader_platform', 'created_at')
    search_fields = ('user__username', 'trade_signal', 'currency_pair', 'publisher_trader', 'trader_platform')
    readonly_fields = ('created_at',)
    fieldsets = (
        (None, {
            'fields': ('user', 'created_at')
        }),
        ('Trade Details', {
            'fields': ('trade_signal', 'currency_pair')
        }),
        ('Trader Idea', {
            'fields': ('trader_idea',)
        }),
        ('Additional Information', {
            'fields': ('post_date_time', 'publisher_trader', 'trader_platform')
        }),
    )

admin.site.register(TraderIdea, TraderIdeaAdmin)
