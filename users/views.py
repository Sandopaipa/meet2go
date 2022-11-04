from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from user_profile.models import Profile
from user_profile.serializers import ProfileSerializer
from .models import AccountData
from .permissions import IsOwnerOrReadOnly
from .serializers import AccountSerializer, AccountCreateSerializer


class UserViewList(APIView):
    permission_classes = (IsAuthenticated, )
    def get(self, request):
        accounts = AccountData.objects.all()
        serializer = AccountSerializer(accounts, many=True)
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
            account = AccountData.objects.get(pk=account_id)
        except:
            return Response({'error': 'Searching object does not exists'})
        account_serializer = AccountSerializer(data=request.data, instance=account, partial=True)
        account_serializer.is_valid(raise_exception=True)
        account_serializer.save()
        return Response({"post": account_serializer.data})


class ProfileUpdateView(APIView):
    def patch(self, request, **kwargs):
        profile_id = kwargs.get('account_id', None)
        if not profile_id:
            return Response({'error': 'can not find any'})
        try:
            profile = Profile.objects.get(pk=profile_id)
        except:
            return Response({'error': 'Searching object does not exists'})
        account_serializer = ProfileSerializer(data=request.data, instance=profile, partial=True)
        account_serializer.is_valid(raise_exception=True)
        account_serializer.save()
        return Response({"post": account_serializer.data})


class UserCreateView(APIView):
    """ With stand of app's concept -
        no need to fill user's profile
        during registration """
    def post(self, request):
        serializer = AccountCreateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(status=201)
