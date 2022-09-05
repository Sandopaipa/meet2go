from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import AccountData


class UserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = AccountData
        fields = (
            'email',
            'password',
            'first_name',
            'last_name',
        )

class UserChangeForm(UserChangeForm):
    class Meta:
        model = AccountData
        fields = (
            'email',
            'password',
            'first_name',
            'last_name',
        )