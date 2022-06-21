from lib2to3.pgen2 import token
from django.shortcuts import render
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from .models import Account, Role
from django.contrib.auth.hashers import check_password, make_password
# Create your views here.


class AccountViewSet(ModelViewSet):

    @action(detail=False, methods=['POST'], name='Login')
    def Login(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        if not username or not password:
            return Response(data={'details': 'username or password is not available'}, status=status.HTTP_204_NO_CONTENT)
        else:
            account = Account.objects.filter(username=username)
            if account.exists():
                account = account.first()
                if check_password(password, account.password):
                    token = RefreshToken.for_user(account)
                    response = {
                        "id": account.id,
                        "role": account.role.name,
                        "access": str(token.access_token),
                        "refresh": str(token)
                    }
                    return Response(data=response)
                else:
                    return Response(data={"details": "Password err"}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response(data={"details": "Not found user"}, status=status.HTTP_404_NOT_FOUND)
