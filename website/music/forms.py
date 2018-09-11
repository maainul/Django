from django.contrib.auth.modles import User
from django import forms
from .models import Album,Song
class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)


	class Meta:
		model = User
		fields =['username','email','password']

