from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from .views import sign_up

urlpatterns = [
    path('login/', LoginView.as_view(template_name='authentication/login.html'), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('sign-up/', sign_up, name='sign-up'),
]
