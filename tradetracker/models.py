from django.db import models
from django.conf import settings

class TradeTracker(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    currency_pair = models.CharField(max_length=6, null=True, blank=True)  # No choices defined
    signal_image = models.ImageField(upload_to='signals/', blank=True, null=True)
    monday_image = models.ImageField(upload_to='signals/monday/', blank=True, null=True)
    tuesday_image = models.ImageField(upload_to='signals/tuesday/', blank=True, null=True)
    wednesday_image = models.ImageField(upload_to='signals/wednesday/', blank=True, null=True)
    thursday_image = models.ImageField(upload_to='signals/thursday/', blank=True, null=True)
    friday_image = models.ImageField(upload_to='signals/friday/', blank=True, null=True)
    pips_gained = models.DecimalField(max_digits=10, blank=True, null=True, decimal_places=2, default=0)
    pips_lost = models.DecimalField(max_digits=10, blank=True, null=True, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.currency_pair or 'Unknown Pair'} - {self.user.username} - {self.created_at.strftime('%Y-%m-%d')}"

    class Meta:
        ordering = ['-created_at']
