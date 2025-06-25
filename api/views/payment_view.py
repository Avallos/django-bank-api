from rest_framework import viewsets, permissions
from ..models import Payment
from ..serializers import PaymentSerializer
from rest_framework.exceptions import PermissionDenied


class PaymentViewSet(viewsets.ModelViewSet):
    serializer_class = PaymentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Payment.objects.filter(loan__user=self.request.user)

    def perform_create(self, serializer):
        if serializer.validated_data["loan"].user != self.request.user:
            raise PermissionDenied(
                "Você não pode adicionar pagamentos a empréstimos de outros usuários."
            )
        serializer.save()
