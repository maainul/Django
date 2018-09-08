from django.contrib import admin

from .models import Album,Song

admin.site.register(Album)#this is show on the admin page
admin.site.register(Song)# for the admin page
