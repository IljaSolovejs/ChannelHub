from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .models import Channel, Programme

class ChannelList(ListView):
    model = Channel
    template_name = 'channels/channel_list.html'
