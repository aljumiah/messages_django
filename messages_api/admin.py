from django.contrib import admin
from .models import Profile, Message, Replay
# Register your models here.

admin.site.register(Profile)
admin.site.register(Message)
admin.site.register(Replay)
