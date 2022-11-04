from django.db import models
from user_profile.models import Profile
from tags.models import Tag
from django.dispatch import receiver


class Event(models.Model):

    EVENT_STATUS = (
        ("coming", "Coming soon"),
        ("ongoing", "Ongoing"),
        ("completed", "Completed"),
        ("denied", "Denied"),
        ("draft", "Draft"),
    )

    event_id = models.BigAutoField('event id', primary_key=True)
    event_name = models.CharField('Event name', max_length=150, blank=True, default='Draft_event')
    event_description = models.TextField(max_length=1500, blank=True)
    """Event datetime info"""
    event_begins = models.DateTimeField(blank=True, null=True)
    event_ends = models.DateTimeField(blank=True, null=True)
    """Event status info (include draft status)"""
    event_status = models.CharField(choices=EVENT_STATUS, default='Draft', max_length=15)
    """Event author id"""
    event_creator_id = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s %s' % (self.event_name, self.event_begins, self.event_status)

    def get_event_id(self):
        return '%d' % self.event_id


class EventGuest(models.Model):
    """Guestlist"""
    __GUESTSTATUS__ = (
        ('invited', 'Invited'),
        ('accepted', 'Accepted'),
        ('denied', 'Denied')
    )
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE)
    profile_id = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True)
    guest_status = models.CharField(choices=__GUESTSTATUS__, blank=True, default='invited', max_length=15)
    join_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s' % self.profile_id


class EventTag(models.Model):
    """Event tag set"""
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE)
    tag_id = models.ForeignKey(Tag, on_delete=models.CASCADE)