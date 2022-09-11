from rest_framework import serializers
from .models import AccountData, UserManager

class UserSerializer(serializers.ModelSerializer):
    """All accounts output"""

    class Meta:
        model = AccountData
        fields = (
            'email',
            'first_name',
            'last_name',
        )

class CreateUserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        account = AccountData.objects.create_user(**validated_data)
        return account

    class Meta:
        model = AccountData
        fields = (
            'email',
            'first_name',
            'last_name',
            'password',
        )
        extra_kwargs = {
            'password': {'write_only': True}
        }