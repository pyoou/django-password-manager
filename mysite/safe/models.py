from django.db import models
from django.contrib.auth.models import User


class Safe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, to_field='id')
    purpose = models.CharField(max_length=300)
    content = models.CharField(max_length=300)

    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return str(self.id)
