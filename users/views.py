from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import AccountData
from .serializers import AccountSerializer, AccountListSerializer

class UserViewList(APIView):
    def get(self, request):
        accounts = AccountData.objects.all()
        serializer = AccountListSerializer(accounts, many=True)
        return Response(serializer.data)


class UserAccountView(APIView):
    def get(self, request, account_id):
        try:
            account = AccountData.objects.get(pk=account_id)
        except:
            return Response({'error': 'account does not exists'})
        serializer = AccountSerializer(account, many=False)
        return Response(serializer.data)


class UserAccountUpdateView(APIView):
    def patch(self, request, **kwargs):
        account_id = kwargs.get('account_id', None)
        if not account_id:
            return Response({'error': 'can not find any'})
        try:
            instance = AccountData.objects.get(pk=account_id)
        except:
            return Response({'error': 'Searching object does not exists'})
        serializer = AccountSerializer(data=request.data, instance=instance, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"post": serializer.data})


"""class UserAccountPasswordUpdateView(APIView):
    def patch(self, request, **kwargs):
        account_id = kwargs.get('account_id', None)
        if not account_id:
            return Response({'error': 'can not find any'})
        try:
            instance = AccountData.objects.get(pk=account_id)
        except:
            return Response({'error': 'Searching object does not exists'})
        serializer = AccountSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'post': serializer.data})"""


class UserCreateView(APIView):
    def post(self, request):
        serializer = AccountSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(status=201)
