from django.shortcuts import render
from django.shortcuts import redirect
from .models import Profile, Message
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
    DestroyAPIView,
    CreateAPIView,
)
from .serializers import (
    UserRegisterSerializer,
    MessageCreateUpdateSerializer,
    ProfileListSerializer,
    MessageListSerializer,
    ProfileDetailSerializer,
    ProfileSearchSerializer,
    UserSerializer
)
from .permissions import IsOwner

# Create your views here.


class UserRegisterAPIView(CreateAPIView):
    serializer_class = UserRegisterSerializer
    permission_classes = [AllowAny]


class MessageCreateView(CreateAPIView):
    serializer_class = MessageCreateUpdateSerializer
    permission_classes = [AllowAny]


class MessageListView(ListAPIView):
    permission_classes = [IsAuthenticated, IsOwner]
    serializer_class = MessageListSerializer

    def get_queryset(self):
        return Message.objects.filter(user=self.request.user)


class ProfileDetailView(ListAPIView):
    serializer_class = ProfileDetailSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        return Profile.objects.filter(user=self.request.user)


class ProfileSearchView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'
    lookup_url_kwarg = 'username'
    permission_classes = [AllowAny]

    # def get_queryset(self, request):
    #     print(request.user)
    #     # username = self.kwargs['username']
    #     return Profile.objects.filter(user__username=request.user.username)
