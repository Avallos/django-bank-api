from django.db import models
from ..models import Loan


class Payment(models.Model):
    class Meta:
        app_label = "api"
        db_table = "payment"

    loan = models.ForeignKey(Loan, on_delete=models.CASCADE, related_name="payments")
    payment_date = models.DateField()
    amount = models.DecimalField(max_digits=12, decimal_places=2)
