from django.shortcuts import render
from .models import Album
from django.http import HttpResponse

def index(request):
	all_albums = Album.objects.all()
	html=''
	for album in all_albums:
		url = '/music/' + str(album.id) + '/'
		html += '<a href =" ' + url + '">' + album.album_title + '</a></br>'
	return HttpResponse(html)

def detail(request,album_id):#album_id is like a variable
	return HttpResponse("<h1>Details for album id:" +str(album_id)+ "</h1>")
