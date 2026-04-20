from django.urls import path
from . import views

urlpatterns = [
    path('contact/', views.contact, name='contact'),
    path('', views.ChannelList.as_view(), name='channel_list'),
    path('channel/create/', views.ChannelCreate.as_view(), name='channel_create'),
    path('channel/<int:pk>/', views.ChannelDetail.as_view(), name='channel_detail'),
    path('channel/<int:pk>/update/', views.ChannelUpdate.as_view(), name='channel_update'),
    path('channel/<int:pk>/delete/', views.ChannelDelete.as_view(), name='channel_delete'),
    path('programme/create/', views.ProgrammeCreate.as_view(), name='programme_create'),
]
