# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import Event,Guest

class EventAdmin(admin.ModelAdmin):
    list_display = ['id','name','status','address','start_time']
    search_fields = ['name']
    list_filter = ['status']

class GuestAdmin(admin.ModelAdmin):
    list_display = ['name','phone','email','sign','create_time','event']
    search_fields = ['name','phone']
    list_filter = ['sign']

admin.site.register(Event,EventAdmin)
admin.site.register(Guest,GuestAdmin)
# Register your models here.
