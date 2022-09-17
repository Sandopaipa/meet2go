from rest_framework import serializers
from .models import AccountData, UserManager


class AccountListSerializer(serializers.ModelSerializer):
    """All accounts output"""

    class Meta:
        model = AccountData
        fields = (
            'email',
            'first_name',
            'last_name',
            'birthdate',
        )


class AccountSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        account = AccountData.objects.create_user(**validated_data)
        return account

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name)', instance.last_name)
        instance.password = validated_data.get('password', instance.password)
        instance.birthdate = validated_data.get('birthdate', instance.birthdate)
        instance.set_password(instance.password)
        instance.save()
        return instance

    class Meta:
        model = AccountData
        fields = (
            'email',
            'first_name',
            'last_name',
            'password',
            'birthdate',
        )
        extra_kwargs = {
            'password': {'write_only': True}
        }
