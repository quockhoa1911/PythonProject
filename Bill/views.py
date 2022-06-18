from django.shortcuts import render
from .serializer import BillSerializer
from .models import Bill, DetailBill
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.response import Response
from Fruitapp.models import Fruits
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class BillView(CreateAPIView):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer
    permission_classes = [IsAuthenticated]


class BillViewDetail(RetrieveAPIView):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer

    def get(self, request, id, *args, **kwargs):
        bill = Bill.objects.get(pk=id)
        serializer = BillSerializer(instance=bill)
        Dt = DetailBill.objects.filter(bill=bill)
        ls = []
        for i in Dt:
            ls.append([i.fruit.name, i.fruit.price*i.weight])
        serializer.data['ListFruits'].clear()
        serializer.data['ListFruits'].append(ls)
        return Response(serializer.data)
