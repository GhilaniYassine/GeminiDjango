from django.urls import path
from . import views

urlpatterns = [
    path('', views.chat_home, name='chat_home'),
    path('api/chat/', views.ChatAPIView.as_view(), name='chat_api'),
]