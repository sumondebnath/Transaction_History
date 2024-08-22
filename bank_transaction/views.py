from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError

from bank_transaction.models import BankAccount, Transaction, TransactionPurpose
from bank_transaction.serializers import BankAccountSerializer, TransactionSerializer, TransactionPurposeSerializer

# Create your views here.

class BankAccountViews(viewsets.ModelViewSet):
    queryset = BankAccount.objects.all()
    serializer_class = BankAccountSerializer
    

class TransactionViews(APIView):
    def get(self, request):
        transactions = Transaction.objects.all()
        serializer = TransactionSerializer(transactions, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid():
            transaction_type = serializer.validated_data["transaction_type"]
            transaction_ammount = serializer.validated_data["transaction_ammount"]
            transfer_account = serializer.validated_data["transfer_account"]
            print(transaction_ammount)
            print(transaction_type)
            # print(transfer_account.id)
            # my_num = BankAccount.objects.get(pk=request.user.id)
            # print("my Num", my_num)
            try:
                bank_acc = BankAccount.objects.get(id=transfer_account.id)
                print(bank_acc.account_name, bank_acc.account_number, bank_acc.account_type, bank_acc.balance)
                print(bank_acc)
            except BankAccount.DoesNotExist:
                raise ValidationError("Bank Account Does Not Exists!")
            # serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class TransactionPurposeViews(viewsets.ModelViewSet):
    queryset = TransactionPurpose.objects.all()
    serializer_class = TransactionPurposeSerializer