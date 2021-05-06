from django.urls import path
from . import views as v

urlpatterns = [
    path('', v.index, name="index"),
    path('passwords/', v.passwords, name="passwords"),
    path('passwords/<int:id>', v.password_view, name="password-view"),
    path('passwords/delete/<int:id>', v.password_delete, name="password-delete"),
]
