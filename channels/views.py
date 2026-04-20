from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView

from .models import Channel, Programme

class ChannelList(ListView):
    model = Channel
    template_name = 'channels/channel_list.html'

class ChannelDetail(DetailView):
    model = Channel
    template_name = 'channels/channel_detail.html'

class ChannelCreate(CreateView):
    model = Channel
    template_name = 'channels/channel_create_form.html'
    fields = ['name', 'description', 'genre', 'country']
