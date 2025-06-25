from rest_framework import serializers
from ..models import Loan
from api.serializers.payment_serializer import PaymentSerializer


class LoanSerializer(serializers.ModelSerializer):
    payments = PaymentSerializer(many=True, read_only=True)
    total_paid = serializers.DecimalField(
        max_digits=12, decimal_places=2, read_only=True
    )
    outstanding_balance = serializers.DecimalField(
        max_digits=12, decimal_places=2, read_only=True
    )

    class Meta:
        model = Loan
        fields = "__all__"
        read_only_fields = [
            "id",
            "ip_address",
            "requested_at",
            "user",
            "total_paid",
            "outstanding_balance",
        ]
