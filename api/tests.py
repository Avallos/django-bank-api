from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Loan, Payment
from .serializers import LoanSerializer, PaymentSerializer


class LoanTestCase(APITestCase):
    def setUp(self):
        self.username = "testuser"
        self.password = "testpass"
        self.user = User.objects.create_user(
            username=self.username, password=self.password
        )

        response = self.client.post(
            "/token/", {"username": self.username, "password": self.password}
        )
        self.token = response.data.get("token")
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token)
        self.default_loan = Loan.objects.create(
            amount=1000.00,
            interest_rate=2.5,
            ip_address="127.1.1.1",
            bank="Banco Casa Verde",
            requested_at="2025-01-01",
            client="Cristiano Ronaldo",
            user=self.user,
        )
        self.default_payment = Payment.objects.create(
            loan=self.default_loan,
            amount=100.00,
            payment_date="2025-02-01",
        )

    def test_create_loan(self):
        data = {
            "amount": 1000.00,
            "interest_rate": 2.5,
            "bank": "Banco Casa Verde",
            "client": "João da Silva",
        }
        response = self.client.post("/api/loan", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Loan.objects.count(), 2)

    def test_create_payment(self):
        loan = self.default_loan
        data = {
            "loan": loan.id,
            "amount": 100.00,
            "payment_date": "2023-10-01",
        }
        response = self.client.post("/api/payment", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(loan.payments.count(), 2)
        self.assertEqual(response.data["loan"], loan.id)

    def test_list_loans(self):
        loan_payload = LoanSerializer(self.default_loan).data
        response = self.client.get("/api/loan")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list)
        self.assertEqual(response.data[0], loan_payload)

    def test_get_payments_by_loan_id(self):
        loan = self.default_loan
        payment = self.default_payment
        response = self.client.get(f"/api/payment/get_payments_by_loan_id/{loan.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list)
        self.assertEqual(response.data[0], PaymentSerializer(payment).data)
