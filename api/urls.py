from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LoanViewSet, PaymentViewSet


class NoTrailingSlashRouter(DefaultRouter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Define a opção trailing_slash como False
        self.trailing_slash = "/?"


# configura o router para as urls do django rest framework
router = NoTrailingSlashRouter()
router.register(r"loan", LoanViewSet, basename="loan")
router.register(r"payment", PaymentViewSet, basename="payment")


urlpatterns = [
    # adiciona as urls do router
    path("", include(router.urls)),
]
