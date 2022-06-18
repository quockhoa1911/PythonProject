from rest_framework import serializers

from Bill.models import Bill, DetailBill


class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = ['status', 'totalPrice', 'code', 'ListFruits']


class DetailBillSerializer(serializers.ModelSerializer):

    class Meta:
        model = DetailBill
        fields = ['__all__']
