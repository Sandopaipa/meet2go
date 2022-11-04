from rest_framework import serializers
from .models import Profile


__USERFIELDSET__ = ('phone_number', 'bio', 'follows', 'gender',)


class ProfileSerializer(serializers.ModelSerializer):

    def update(self, instance, validated_data):
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.bio = validated_data.get('bio', instance.bio)
        #instance.follows = validated_data.get('follows', instance.follows)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.save()
        return instance

    class Meta:
        model = Profile
        fields = __USERFIELDSET__