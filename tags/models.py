from django.db import models
import datetime


class Tag(models.Model):
    tag_id = models.BigAutoField(primary_key=True)
    tag_name = models.CharField(max_length=32, blank=False, unique=True)
    tag_creation_date = models.DateTimeField(auto_created=True, default=datetime.datetime.now())

    def __str__(self):
        return '%s' % self.tag_name
