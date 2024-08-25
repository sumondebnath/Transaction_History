from django.db import models
from django.contrib.auth.models import User

from bank_transaction.constants import ACCOUNT_TYPE, TRANSACTION_TYPE

# Create your models here.

class BankAccount(models.Model):
    account_name = models.CharField(max_length=120)
    account_number = models.CharField(max_length=24)
    account_type = models.CharField(max_length=10, choices=ACCOUNT_TYPE)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    limit = models.DecimalField(max_digits=10, decimal_places=2, default=0, null=True, blank=True)

    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name="bank_account")

    def save(self, *args, **kwargs):
        if not self.limit:
            self.limit += (-1 * self.balance)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Account : {self.account_number}  Balance : {self.balance}"
    


class Transaction(models.Model):
    transaction_type = models.CharField(max_length=15, choices=TRANSACTION_TYPE)
    transaction_ammount = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    note = models.TextField(null=True, blank=True)

    current_account = models.ForeignKey(BankAccount, on_delete=models.PROTECT, related_name="curr_transaction")
    transfer_account = models.ForeignKey(BankAccount, on_delete=models.PROTECT, related_name="transaction")

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return f"Current : {self.current_account.account_number} Transfer : {self.transfer_account.account_number}"



class TransactionPurpose(models.Model):
    transaction = models.OneToOneField(Transaction, on_delete=models.PROTECT, related_name="transaction_purpose")
    purpose = models.CharField(max_length=40, null=True, blank=True)

    def __str__(self):
        return f"{self.transaction.transaction_ammount} {self.purpose} {self.transaction.created_at}" 