from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .models import Channel, Programme, GENRE_CHOICES
from .forms import ContactForm

class ChannelList(ListView):
    model = Channel
    template_name = 'channels/channel_list.html'

    def get_queryset(self):
        queryset = Channel.objects.all()
        genre = self.request.GET.get('genre')
        search = self.request.GET.get('search')
        if genre:
            queryset = queryset.filter(genre=genre)
        if search:
            queryset = queryset.filter(name__icontains=search)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['genres'] = GENRE_CHOICES
        context['selected_genre'] = self.request.GET.get('genre', '')
        context['search'] = self.request.GET.get('search', '')
        return context

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

def contact(request):
    submitted = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/contact?submitted=True')
    else:
        form = ContactForm()
        if 'submitted' in request.GET:
            submitted = True
    context = {
        'form': form,
        'submitted': submitted,
    }
    return render(request, 'channels/contact.html', context)

class ProgrammeCreate(LoginRequiredMixin, CreateView):
    model = Programme
    template_name = 'channels/programme_create_form.html'
    fields = ['channel', 'title', 'description', 'air_time', 'image']

    def get_success_url(self):
        return self.object.channel.get_absolute_url()
