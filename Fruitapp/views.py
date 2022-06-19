

from .models import Fruits
from .serializer import FruitsSerializer
# Create your views here.

from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from Account.models import Account
from Account.constants import checkpermiss
from rest_framework.decorators import action, permission_classes
from rest_framework import viewsets


class FruitsViewset(viewsets.ModelViewSet):

    serializer_class = FruitsSerializer
    check_permiss = checkpermiss()
    queryset = Fruits.objects.all()

    # def get_queryset(self):  # data
    #     frt = Fruits.objects.all()
    #     serializer = FruitsSerializer(instance=frt, many=True)
    #     return serializer.data

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @action(detail=True, methods=['GET'], name='Detail')
    def Detail(self, request, pk=None, *args, **kwargs):
        instance = Fruits.objects.get(pk=pk)
        serializer = FruitsSerializer(instance=instance)
        return Response(data=serializer.data)

    @action(detail=False, methods=['POST'], permission_classes=[IsAuthenticated], name='Add')
    def Add(self, request, *args, **kwargs):
        username = request.user.username
        user = Account.objects.get(username=username)
        if user.role.name in self.check_permiss.check_permissdb:
            serializer = FruitsSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_201_CREATED)
            else:
                return Response(status=status.HTTP_409_CONFLICT)
        else:
            return Response(status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)

    @action(detail=True, methods=['PUT'], permission_classes=[IsAuthenticated], name='Update')
    def Update(self, request, pk=None, *args, **kwargs):
        username = request.user.username
        user = Account.objects.get(username=username)
        if user.role.name in self.check_permiss.check_permissdb:
            instance = Fruits.objects.get(pk=pk)
            serializer = FruitsSerializer(instance=instance, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_409_CONFLICT)
        else:
            return Response(status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)

    @action(detail=True, methods=['DELETE'], permission_classes=[IsAuthenticated], name='Delete')
    def Dele(self, request, pk=None, *args, **kwargs):
        username = request.user.username
        user = Account.objects.get(username=username)

        if user.role.name in self.check_permiss.check_permissdb:
            instance = Fruits.objects.get(pk=pk)
            if instance:
                instance.delete()
                return Response(status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_409_CONFLICT)
        else:
            return Response(status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)

    def partial_update(self, request, *args, **kwargs):
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        return Response(status=status.HTTP_400_BAD_REQUEST)
