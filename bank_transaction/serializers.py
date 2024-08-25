from rest_framework import serializers

from bank_transaction.models import BankAccount, Transaction, TransactionPurpose


class BankAccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = BankAccount
        fields = "__all__"
        # exclude = ["limit"]


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = "__all__"


class TransactionPurposeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionPurpose
        fields = "__all__"