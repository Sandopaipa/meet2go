from rest_framework import serializers
from .models import AccountData


__USERFIELDSET__ = (
            'email',
            'first_name',
            'last_name',
            'birthdate',
            'phone_number',
            'bio',
            'follows',
            'gender',
        )


class AccountListSerializer(serializers.ModelSerializer):
    """All accounts output"""
    phone_number = serializers.CharField(source='profile.phone_number')
    bio = serializers.CharField(source='profile.bio')
    follows = serializers.StringRelatedField(source='profile.follows', many=True)
    gender = serializers.CharField(source='profile.gender')
    class Meta:
        model = AccountData
        fields = __USERFIELDSET__


class AccountSerializer(serializers.ModelSerializer):
    phone_number = serializers.CharField(source='profile.phone_number')
    bio = serializers.CharField(source='profile.bio', allow_null=True)
    follows = serializers.StringRelatedField(source='profile.follows', many=True)
    gender = serializers.CharField(source='profile.gender')

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
        fields = __USERFIELDSET__
        extra_kwargs = {
            'password': {'write_only': True}
        }
