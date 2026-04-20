from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Channel, Programme

class ChannelList(ListView):
    model = Channel
    template_name = 'channels/channel_list.html'

class ChannelDetail(DetailView):
    model = Channel
    template_name = 'channels/channel_detail.html'
