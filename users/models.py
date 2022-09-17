from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, password, first_name, last_name, birthdate, **extra_fields):
        if not email:
            raise ValueError('Введите ваш e-mail')
        if not first_name:
            raise ValueError('Введите ваше имя')
        if not last_name:
            raise ValueError('Введите вашу фамилию')
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            first_name=first_name,
            last_name=last_name,
            birthdate=birthdate,
            **extra_fields
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, first_name, last_name, birthdate, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Cannot create superuser: is_staff is not True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Cannot create superuser: is_superuser is not True')
        return self.create_user(email, password, first_name, last_name, birthdate, **extra_fields)



class AccountData(AbstractUser):
    username = None
    account_id = models.BigAutoField('id пользователя', primary_key=True)
    email = models.EmailField('e-mail', unique=True, blank=False)
    first_name = models.CharField('Имя', max_length=32, blank=False)
    last_name = models.CharField('Фамилия', max_length=32, blank=False)
    birthdate = models.DateField('Дата рождения', blank=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
        'first_name',
        'last_name',
        'birthdate',
    ]

    objects = UserManager()

    def __str__(self):
        return '%s %s'% (self.first_name, self.last_name)


