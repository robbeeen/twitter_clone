from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter

from core import views
from core.views import *
# urlpatterns = [
#     path('users/', UserRegistration.as_view(), name="users"),
#     path('posts/', PostCreation.as_view(), name="posts")
# ]
#
# routes = DefaultRouter()
# routes.register('user', UserController, basename='user')
#
# urlpatterns = routes.urls + urlpatterns
urlpatterns = [
    path('users/', views.UserAPIView.as_view(), name='user-list-create'),
    path('users/<int:pk>/', views.UserAPIView.as_view(), name='user-retrieve-update'),
    path('posts/', views.PostAPIView.as_view(), name='post-list-create'),
    path('posts/<int:pk>/', views.PostAPIView.as_view(), name='post-retrieve-update-delete'),
    path('posts/all/', views.PostListAPIView.as_view(), name='post-list'),
]
