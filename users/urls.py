from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from .views import UserCreateView, UserAccountView, UserAccountUpdateView, UserViewList
from django.urls import path


urlpatterns = [
    path('user/<int:account_id>', UserAccountView.as_view()),
    path('user/list', UserViewList.as_view()),
    path('user/create', UserCreateView.as_view()),
    path('user/update/<int:account_id>', UserAccountUpdateView.as_view()),
]
