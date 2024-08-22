from django.contrib import admin

from bank_transaction.models import BankAccount, Transaction, TransactionPurpose

# Register your models here.

admin.site.register(BankAccount)

admin.site.register(Transaction)

admin.site.register(TransactionPurpose)