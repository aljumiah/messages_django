from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=1)
    image = models.ImageField(
        upload_to='users_profile_images', null=False, blank=False)

    def __str__(self):
        return self.user.username


class Message(models.Model):
    content = models.TextField(blank=False, null=False)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_messages")

    def __str__(self):
        return "To: %s | Message:  [%s] " % (self.user.username, self.content)


class Replay(models.Model):
    replay_content = models.TextField(blank=False, null=False)
    message = models.OneToOneField(
        Message, on_delete=models.CASCADE, null=False, blank=False, related_name="replied_message")

    def __str__(self):
        return "%s has Replaied to [%s] with:  [%s]" % (self.message.user, self.message.content, self.replay_content)
