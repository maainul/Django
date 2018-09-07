# Django
Django is a free and open-source web framework, written in Python, which follows the model-view-template architectural pattern. It is maintained by the Django Software Foundation, an independent organization established as a 501 non-profit.

## My site
```
 1.django-admin startproject mysite
 2.django-admin startapp myapp
 3.Edit setting.py and add 'myapp'
 4.Update url and add these files 

 	  from myapp import views as v
 	  url(r'^$',v.index),

 5.Add index function in views.py 

 	from django.shortcuts import render,render_to_response
	def index(request):
		return render_to_response('index.html')

6. create templates in my app folder and create index.html inside template folder
	<h1>ANIKK</h1>
```
### Add Templates in
```



```
	
