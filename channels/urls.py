from django.urls import path
from . import views

urlpatterns = [
    path('', views.ChannelList.as_view(), name='channel_list'),
    path('channel/<int:pk>/', views.ChannelDetail.as_view(), name='channel_detail'),
]
