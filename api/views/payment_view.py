from rest_framework import viewsets, permissions
from ..models import Payment
from ..serializers import PaymentSerializer
from rest_framework.exceptions import PermissionDenied
from rest_framework.decorators import action
from rest_framework.response import Response


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

    @action(detail=False, methods=['get'], url_path='get_payments_by_loan_id/(?P<loan_id>[^/.]+)')
    def get_payments_by_loan_id(self, request, loan_id=None):
        payments = Payment.objects.filter(loan__id=loan_id, loan__user=request.user)
        serializer = self.get_serializer(payments, many=True)
        return Response(serializer.data)