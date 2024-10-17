from django.contrib import admin
from .models import MgiCandles

class MgiCandlesAdmin(admin.ModelAdmin):
    list_display = (
        'user', 'trade_signal', 'is_active', 'signal_candle', 'hour_candle', 'created_at', 'currency_pair', 'session',
        'five_min_order_block', 'flip_four_hour_candle', 'four_hour_break_of_structure', 'five_min_break_of_structure',
        'change_color_ut_alert'
    )
    search_fields = (
        'user__username', 'trade_signal',
    )
    readonly_fields = ('created_at',)
    fieldsets = (
        (None, {
            'fields': ('user', 'created_at')
        }),
        ('Trade Details', {
            'fields': ('trade_signal', 'is_active', 'currency_pair', 'session')
        }),
        ('Candles', {
            'fields': ('signal_candle','idea_candle','line_graph_candle','monday_candle','tuesday_candle','wednesday_candle','thursday_candle','friday_candle', 'saturday_candle', 'sunday_candle', 'hour_candle', 'two_hour_candle', 'entry_candle', 'breakeven_candle', 'take_profit_candle')
        }),
        ('Additional Details', {
            'fields': ('pips_lost', 'pips_gained', 'five_min_order_block', 'flip_four_hour_candle', 'four_hour_break_of_structure', 'five_min_break_of_structure', 'change_color_ut_alert')
        }),
    )

admin.site.register(MgiCandles, MgiCandlesAdmin)
