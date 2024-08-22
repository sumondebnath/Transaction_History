from django.urls import path, include
from rest_framework.routers import DefaultRouter

from bank_transaction.views import BankAccountViews, TransactionViews, TransactionPurposeViews

router = DefaultRouter()

router.register(r"accounts", BankAccountViews, basename="bank_account")
# router.register(r"transaction", TransactionViews, basename="transaction")
router.register(r"transaction purpose", TransactionPurposeViews, basename="purpose")

urlpatterns = [
    path("", include(router.urls)),
    path("transaction/", TransactionViews.as_view(), name="transaction"),
]