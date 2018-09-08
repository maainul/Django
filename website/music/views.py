from django.shortcuts import render
from .models import Album
from django.http import HttpResponse
from django.shortcuts import HttpResponse

def index(request):
	all_albums = Album.objects.all()
	#we use shortcuts so remove this line and return line also
	#template = loader.get_template('music/index.html')
	context ={'all_albums':all_albums}
	return render(request,'music/index.html',context)
	#return HttpResponse(template.render(context,request))

def detail(request,album_id):#album_id is like a variable
	return HttpResponse("<h1>Details for album id:" +str(album_id)+ "</h1>")
