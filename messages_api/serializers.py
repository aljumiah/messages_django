from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from django.contrib.auth.models import User
from .models import Profile, Message, Replay


class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    token = serializers.CharField(allow_blank=True, read_only=True)

    class Meta:
        model = User
        fields = ['username',
                  'password', 'email', 'token']

    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']
        email = validated_data['email']
        new_user = User(username=username, email=email)
        new_user.set_password(password)
        new_user.save()

        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(new_user)
        token = jwt_encode_handler(payload)

        validated_data["token"] = token
        return validated_data


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
        ]


class ProfileListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'image', ]


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'content', ]


class MessageCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['user', 'content']


class ReplayAndMessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Replay
        fields = ['replay_content']


class MessageListSerializer(serializers.ModelSerializer):
    replied_message = ReplayAndMessageSerializer()

    class Meta:
        model = Message
        fields = ['id', 'content', 'replied_message']


class ProfileDetailSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Profile
        fields = ['id', 'user', 'image']


class ProfileSearchSerializer(serializers.ModelSerializer):
    profile = ProfileListSerializer()

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name',
                  'last_name', 'profile']


class ReplayMessageSerializer(serializers.ModelSerializer):
    message = MessageListSerializer()

    class Meta:
        model = Replay
        fields = ['message', 'replay_content']


class ReplayMessageCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Replay
        fields = ['replay_content', 'message']
