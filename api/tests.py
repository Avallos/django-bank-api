from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Loan


class LoanTestCase(APITestCase):
    def setUp(self):
        self.username = "testuser"
        self.password = "testpass"
        self.user = User.objects.create_user(username=self.username, password=self.password)
        
        response = self.client.post("/token/", {
            "username": self.username,
            "password": self.password
        })
        self.token = response.data.get("token")
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token)

    def test_create_loan(self):
        data = {
            "amount": "1000.00",
            "interest_rate": "2.5",
            "bank": "Banco Casa Verde",
            "client": "João da Silva",
        }
        response = self.client.post("/api/loan", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Loan.objects.count(), 1)

    def test_create_payment(self):
        loan = Loan.objects.create(
            amount=1000.00,
            interest_rate=2.5,
            ip_address="127.1.1.1",
            bank="Banco Casa Verde",
            client="Cristiano Ronaldo",
            user=self.user
        )
        data = {
            "loan": loan.id,
            "amount": "100.00",
            "payment_date": "2023-10-01"
        }
        response = self.client.post("/api/payment", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(loan.payments.count(), 1)

    def test_list_loans(self):
        response = self.client.get("/api/loan")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list)

    def test_list_payments(self):
        response = self.client.get("/api/payment")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list)