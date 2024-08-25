from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError

from bank_transaction.models import BankAccount, Transaction, TransactionPurpose
from bank_transaction.serializers import BankAccountSerializer, TransactionSerializer, TransactionPurposeSerializer

# Create your views here.

# class BankAccountViews(viewsets.ModelViewSet):
#     queryset = BankAccount.objects.all()
#     serializer_class = BankAccountSerializer


class BankAccountViews(APIView):

    def get(self, request):
        bank_accounts = BankAccount.objects.all()
        serializer = BankAccountSerializer(bank_accounts, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = BankAccountSerializer(data=request.data)
        if serializer.is_valid():
            balance = serializer.validated_data["balance"]
            print(balance)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# class TransactionViews(viewsets.ModelViewSet):
#     queryset = Transaction.objects.all()
#     serializer_class = TransactionSerializer    


class TransactionViews(APIView):
    # permission_classes = [IsAuthenticated]
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
            current_account = serializer.validated_data["current_account"]
            print(transaction_ammount)
            print(transaction_type)
            print(current_account, current_account.id)
            print(transfer_account, transfer_account.id)
            try:
                curr_acc = BankAccount.objects.get(id=current_account.id)
                trans_acc = BankAccount.objects.get(id=transfer_account.id)
                print(trans_acc.account_name, trans_acc.account_number, trans_acc.account_type, trans_acc.balance)
                print(curr_acc)
                if curr_acc.balance >= transaction_ammount:
                    trans_acc.balance += transaction_ammount
                    trans_acc.limit += (-1 * transaction_ammount)
                    curr_acc.balance -= transaction_ammount
                    curr_acc.limit += transaction_ammount
                    trans_acc.save()
                    curr_acc.save()
                else:
                    raise ValidationError("Your Current Balance Not Available!")
            except BankAccount.DoesNotExist:
                raise ValidationError("Bank Account Does Not Exists!")
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class TransactionPurposeViews(viewsets.ModelViewSet):
    queryset = TransactionPurpose.objects.all()
    serializer_class = TransactionPurposeSerializer

    def get_queryset(self):
        queryset = super().get_queryset()

        transaction_id = self.request.query_params.get("transaction_id")
        # print(transaction_id)
        if transaction_id:
            queryset = queryset.filter(transaction_id=transaction_id)
        return queryset