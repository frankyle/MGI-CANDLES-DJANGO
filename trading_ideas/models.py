from django.db import models
from django.conf import settings

class TraderIdea(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    # Trade Details
    trade_signal = models.CharField(max_length=4, choices=(("buy", "Buy"), ("sell", "Sell")), null=True, blank=True)
    currency_pair = models.CharField(max_length=6, null=True, blank=True)
    trader_idea = models.ImageField(upload_to='trader_ideas/', null=True, blank=True)
    
     # Additional Fields
    post_date_time = models.DateTimeField(null=True, blank=True)
    publisher_trader = models.CharField(max_length=50, null=True, blank=True)
    trader_platform = models.CharField(max_length=50, null=True, blank=True)
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Trader Idea by {self.user.username} on {self.created_at}"

    class Meta:
        verbose_name = "Trader Idea"
        verbose_name_plural = "Trader Ideas"
