from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=1)
    image = models.ImageField(
        upload_to='users_profile_images', null=True, blank=True)

    def __str__(self):
        return self.user.username


class Message(models.Model):
    content = models.TextField(blank=True, null=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_messages", default=1)

    def __str__(self):
        return "To: %s | Message:  [%s] " % (self.user.username, self.content)
