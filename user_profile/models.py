from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from users.models import AccountData
from tags.models import Tag
from phonenumber_field.modelfields import PhoneNumberField


class Profile(models.Model):
    __GENDERS__ = [
        ('male', "Male"),
        ('female', "Female"),
    ]
    # add an option to set a picture
    profile_id = models.OneToOneField(AccountData, on_delete=models.CASCADE)
    phone_number = PhoneNumberField('Phone number', blank=True)
    bio = models.TextField(max_length=1500, blank=True)
    follows = models.ManyToManyField('self', blank=True, related_name='Follows', symmetrical=False)
    followers = models.ManyToManyField('self', blank=True, related_name='Followers', symmetrical=False)
    gender = models.CharField('Gender', choices=__GENDERS__, blank=True, max_length=6)

    def __str__(self):
        return '%s' % self.profile_id


class ProfileTagList(models.Model):
    profile_id = models.ForeignKey(Profile, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return '%s' % self.tag


'''class Follow(models.Model):
    # Owner's profile
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
    # Profile what Owner follows
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return '%s' % self.profile


class Follower(models.Model):
    # Owner's profile
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
    # Profile that owner follows
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return '%s' % self.profile'''


@receiver(post_save, sender=AccountData)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(profile_id=instance)


@receiver(post_save, sender=AccountData)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
