from django.contrib import admin
from .models import AccountData
from .forms import UserCreationForm, UserChangeForm
from django.contrib.auth.admin import UserAdmin


class UserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = AccountData
    list_display = (
        'account_id',
        'email',
        'first_name',
        'last_name',
        'birthdate',
        'is_staff',
        'is_active',
    )
    list_filter = ('email', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password', 'first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    search_fields = ('email',)
    ordering = ('email',)

admin.site.register(AccountData, UserAdmin)
