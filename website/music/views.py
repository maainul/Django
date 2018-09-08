from django.shortcuts import render
from .models import Album
from django.http import HttpResponse
from django.shortcuts import HttpResponse
from django.http import Http404

def index(request):
	all_albums = Album.objects.all()
	#we use shortcuts so remove this line and return line also
	#template = loader.get_template('music/index.html')
	return render(request,'music/index.html',{'all_albums':all_albums})
	#return HttpResponse(template.render(context,request))

def detail(request,album_id):#album_id is like a variable
	#return HttpResponse("<h1>Details for album id:" +str(album_id)+ "</h1>")
	try:
		album = Album.objects.get(pk =album_id)
	except Album.DoesNotExist:
		raise Http404("Album does not exists")
	return render(request,'music/detail.html',{'album':album})
