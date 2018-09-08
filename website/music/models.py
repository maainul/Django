from django.db import models

class Album(models.Model):
	artist = models.CharField(max_length=250)
	album_title = models.CharField(max_length=500)
	genre = models.CharField(max_length=100)
	album_logo = models.CharField(max_length=1000)

	# For show album title, artist and genere in the homepage
	def __str__(self):
		return self.album_title + ' - ' + self.artist+ ' - '+self.genre

class Song(models.Model):
	album = models.ForeignKey(Album, on_delete = models.CASCADE)
	file_type = models.CharField(max_length=10)
	song_title = models.CharField(max_length=250)

