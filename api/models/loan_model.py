from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Loan(models.Model):

    class Meta:
        app_label = "api"
        db_table = "loan"

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="loans")
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)
    ip_address = models.GenericIPAddressField()
    requested_at = models.DateTimeField(auto_now_add=True)
    bank = models.CharField(max_length=255)
    client = models.CharField(max_length=255)

    @property
    def total_paid(self):
        return sum(payment.amount for payment in self.payments.all())

    @property
    def outstanding_balance(self):
        delta = timezone.now().date() - self.requested_at.date()
        months = delta.days // 30
        total_with_interest = float(self.amount) * (
            (1 + (float(self.interest_rate) / 100)) ** months
        )
        return total_with_interest - float(self.total_paid)
