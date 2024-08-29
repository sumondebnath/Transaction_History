from django.urls import path, include
from rest_framework.routers import DefaultRouter

from bank_transaction.views import BankAccountViews, TransactionViews, TransactionPurposeViews, TransactionGetQuerys, BankAccountGETID

router = DefaultRouter()

router.register(r"account", BankAccountGETID, basename="account")
router.register(r"transaction queryes", TransactionGetQuerys, basename="transaction_querys")
router.register(r"transaction purpose", TransactionPurposeViews, basename="purpose")

urlpatterns = [
    path("", include(router.urls)),
    path("transaction/", TransactionViews.as_view(), name="transaction"),
    path("accounts/", BankAccountViews.as_view(), name="bank_account"),
]