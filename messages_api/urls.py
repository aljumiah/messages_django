from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token

from .views import (
    UserRegisterAPIView,
    MessageCreateView,
    MessageListView,
    ProfileDetailView,
    UserSearchView
)
urlpatterns = [

    path('login/', obtain_jwt_token, name='login'),
    path('register/', UserRegisterAPIView.as_view(), name='register'),
    path('profile/', ProfileDetailView.as_view(), name='profile'),
    path('user/<str:username>/',
         UserSearchView.as_view(), name='user-profile'),
    path('message/create/', MessageCreateView.as_view(), name='create-message'),
    path('message/list/', MessageListView.as_view(), name='list-message'),

]
