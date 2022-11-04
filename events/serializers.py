from rest_framework import serializers

from tags.models import Tag
from .models import Event
from user_profile.models import Profile


__EVENTFIELDSET__ = (
    'event_name',
    'event_description',
    'event_begins',
    'event_ends',
    'event_status',
    'event_draft',
    'event_creator_id',
)


class EventSerializer(serializers.ModelSerializer):

    def update(self, instance, validated_data):
        instance.event_name = validated_data.get('event_name', instance.event_name)
        instance.event_description = validated_data.get('event_description', instance.event_description)
        instance.event_begins = validated_data.get('event_begins', instance.event_begins)
        instance.event_ends = validated_data.get('event_ends', instance.event_ends)
        instance.event_status = validated_data.get('event_status', instance.event_status)
        instance.event_creator_id = validated_data.get('event_creator_id', instance.event_creator_id)
        return instance

    class Meta:
        model = Event
        fields = __EVENTFIELDSET__


class EventGuestSerializer(serializers.ModelSerializer):
    def update(self, instance, validated_data):
        instance.profile_id = validated_data('profile_id', instance.profile_id)
        return instance

    class Meta:
        model = Profile
        fields = ('profile_id', )


class EventTagSerializer(serializers.ModelSerializer):

    def update(self, instance, validated_data):
        instance.tag_id = validated_data.get('tag_id', instance.tag_id)
        return instance

    class Meta:
        model = Tag
        fields = ('tag_id')
