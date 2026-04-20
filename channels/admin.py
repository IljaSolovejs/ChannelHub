from django.contrib import admin
from .models import Channel, Programme

class ChannelAdmin(admin.ModelAdmin):
    list_display = ('name', 'genre', 'country')
    ordering = ('name',)
    search_fields = ('name', 'genre')

class ProgrammeAdmin(admin.ModelAdmin):
    list_display = ('title', 'channel', 'air_time')
    ordering = ('title',)
    search_fields = ('title',)

admin.site.register(Channel, ChannelAdmin)
admin.site.register(Programme, ProgrammeAdmin)
