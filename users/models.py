from django.db import models
from django.contrib.auth.models import User, AnonymousUser


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    following = models.ManyToManyField(User, related_name="following", blank=True)
    bio = models.CharField(default="", blank=True, null=True, max_length=200)
    date_of_birth = models.DateField(blank=False, null=False)
    updated_at = models.DateField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(
        default="user-default.png",
        upload_to="profile-pic",
        blank=True,
        null=True,
        height_field=None,
        width_field=None,
        max_length=None,
    )

    def __str__(self):
        return self.user.username
