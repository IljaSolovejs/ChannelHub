from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

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
    fields = ['name', 'description', 'genre', 'country', 'logo']

class ChannelUpdate(LoginRequiredMixin, UpdateView):
    model = Channel
    template_name = 'channels/channel_update_form.html'
    fields = ['name', 'description', 'genre', 'country', 'logo']

class ChannelDelete(LoginRequiredMixin, DeleteView):
    model = Channel
    template_name = 'channels/channel_delete_form.html'
    success_url = reverse_lazy('channel_list')

class ProgrammeCreate(LoginRequiredMixin, CreateView):
    model = Programme
    template_name = 'channels/programme_create_form.html'
    fields = ['channel', 'title', 'description', 'air_time', 'image']

    def get_success_url(self):
        return self.object.channel.get_absolute_url()
