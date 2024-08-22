from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT, related_name="profile")
    image = models.FileField(upload_to="accounts/media/", null=True, blank=True)
    phone_number = models.CharField(max_length=14)

    def __str__(self):
        return self.user.email