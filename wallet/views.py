from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .serializers import TransactionHistorySerializer, WalletSerializer

class AccountWalletView(APIView):
    serializer_class = serializers.WalletSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request):
        wallet_data = models.Wallet.objects.filter(
            account=request.user).values()[0]

        if wallet_data["is_disabled"] == True:
            return Response({
                "account status": "blocked",
                "wallet id": wallet_data['wallet_id'],
                "message": "Your account has been disabled, contact support"
            })

        else:
            return Response({
                "account status": "enabled",
                "wallet id": wallet_data['wallet_id'],
                "balance": float(wallet_data['balance'])
            })

class TransactionsListView(ListAPIView):
    serializer_class = serializers.TransactionHistorySerializer
    queryset = models.Transaction.objects.all()
    permission_classes = [IsAuthenticated]

    def list(self, request):
        account_transactions = models.Transaction.objects.filter(account=self.request.user)
        serializer = serializers.TransactionHistorySerializer(account_transactions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)