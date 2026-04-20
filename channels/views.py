from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Channel, Programme

class ChannelList(ListView):
    model = Channel
    template_name = 'channels/channel_list.html'

class ChannelDetail(DetailView):
    model = Channel
    template_name = 'channels/channel_detail.html'

class ChannelCreate(LoginRequiredMixin, CreateView):
    model = Channel
    template_name = 'channels/channel_create_form.html'
    fields = ['name', 'description', 'genre', 'country']
