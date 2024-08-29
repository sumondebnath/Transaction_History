from rest_framework import serializers

from bank_transaction.models import BankAccount, Transaction, TransactionPurpose


class BankAccountSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = BankAccount
        fields = "__all__"
        # exclude = ["limit"]


class TransactionSerializer(serializers.ModelSerializer):

    transaction_type = serializers.StringRelatedField(read_only=True)
    current_account = serializers.StringRelatedField(read_only=True)
    transfer_account = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Transaction
        fields = "__all__"


class TransactionPurposeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionPurpose
        fields = "__all__"