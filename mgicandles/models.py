from django.db import models
from django.conf import settings

class MgiCandles(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    # Trade Details
    trade_signal = models.CharField(max_length=4, choices=(("buy", "Buy"), ("sell", "Sell")), null=True, blank=True)
    is_active = models.BooleanField(default=False, null=True, blank=True)

    # New fields
    idea_candle = models.ImageField(upload_to='idea_candles/', null=True, blank=True)
    line_graph_candle = models.ImageField(upload_to='line_graph_candles/', null=True, blank=True)

    # Existing fields
    signal_candle = models.ImageField(upload_to='signal_candles/', null=True, blank=True)
    two_hour_candle = models.ImageField(upload_to='two_hour_candles/', null=True, blank=True)
    
    # New fields
    monday_candle = models.ImageField(upload_to='monday_candles/', null=True, blank=True)
    tuesday_candle = models.ImageField(upload_to='tuesday_candles/', null=True, blank=True)
    wednesday_candle = models.ImageField(upload_to='wednesday_candles/', null=True, blank=True)
    thursday_candle = models.ImageField(upload_to='thursday_candles/', null=True, blank=True)
    friday_candle = models.ImageField(upload_to='friday_candles/', null=True, blank=True)
    saturday_candle = models.ImageField(upload_to='saturday_candles/', null=True, blank=True)
    sunday_candle = models.ImageField(upload_to='sunday_candles/', null=True, blank=True)
    
    # New fields
    pips_lost = models.DecimalField(max_digits=10, blank=True, null=True, decimal_places=2, default=0)
    pips_gained = models.DecimalField(max_digits=10, blank=True, null=True, decimal_places=2, default=0)
    

    # Existing fields
    hour_candle = models.ImageField(upload_to='hour_candles/', null=True, blank=True)
    entry_candle = models.ImageField(upload_to='entry_candle/', null=True, blank=True)
    breakeven_candle = models.ImageField(upload_to='breakeven_candle/', null=True, blank=True)
    take_profit_candle = models.ImageField(upload_to='take_profit_candle/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    candle_pattern = models.CharField(
        max_length=20,
        choices=(
            ("Engulfing", "Engulfing Candle"), 
            ("Small Body", "Small Candle"),
            ("Pinbar", "Pin bar Candle"),
        ),
        blank=True,
        null=True
    )
    fibonacci_level = models.CharField(
        max_length=5,
        choices=(
            ("38.2%", "38.2%"),
            ("50%", "50%"),
            ("61.8%", "61.8%"),
            ("78.6%", "78.6%"),
        ),
        blank=True,
        null=True
    )
    session = models.CharField(
        max_length=15,
        choices=(
            ("London", "London Session"),
            ("Newyork", "New York Session"),
        ),
        blank=True,
        null=True
    )
    currency_pair = models.CharField(max_length=6, null=True, blank=True)

    five_min_order_block = models.BooleanField(default=False, null=True, blank=True)
    flip_four_hour_candle = models.BooleanField(default=False, null=True, blank=True)
    four_hour_break_of_structure = models.BooleanField(default=False, null=True, blank=True)
    five_min_break_of_structure = models.BooleanField(default=False, null=True, blank=True)
    change_color_ut_alert = models.BooleanField(default=False, null=True, blank=True)
    
    class Meta:
        verbose_name = "Mgi candle"
        verbose_name_plural = "Mgi candles"
