from django.db import models
from users.models import AccountData
from django.db.models.signals import post_save
from django.dispatch import receiver
from users.models import AccountData
from phonenumber_field.modelfields import PhoneNumberField


class Profile(models.Model):
    __GENDERS__ = [
        ('male', "Male"),
        ('female', "Female"),
    ]
    profile_id = models.OneToOneField(AccountData, on_delete=models.CASCADE)
    phone_number = PhoneNumberField('Phone number', unique=True, blank=True)
    bio = models.TextField(max_length=1500, blank=True)
    follows = models.ManyToManyField('self', blank=True, related_name='Followers', symmetrical=False)
    gender = models.CharField('Gender', choices=__GENDERS__, blank=True, max_length=6)


@receiver(post_save, sender=AccountData)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(profile_id=instance)

@receiver(post_save, sender=AccountData)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()