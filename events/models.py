from django.db import models
from user_profile.models import Profile


class Event(models.Model):
    EVENT_STATUS = (
        ("coming", "Coming soon"),
        ("ongoing", "Ongoing"),
        ("completed", "Completed"),
        ("denied", "Denied")
    )

    event_id = models.BigAutoField('event id', primary_key=True)
    event_name = models.CharField('Event name', max_length=150, blank=True)
    event_description = models.TextField(max_length=1500, blank=True)
    """Event datetime info"""
    event_begins = models.DateTimeField(blank=True, null=True)
    event_ends = models.DateTimeField(blank=True, null=True)
    """Event status info (include draft status)"""
    event_status = models.CharField(choices=EVENT_STATUS, blank=True, max_length=9)
    event_draft = models.BooleanField(default=True, blank=True)
    """Event author id"""
    event_creator_id = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s %s' % (self.event_id, self.event_begins, self.event_status)
