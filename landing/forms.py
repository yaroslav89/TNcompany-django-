from django.contrib.auth.models import User
from django import forms

class LoginForm(forms.ModelForm):
	class Meta:
		model = User
		fields = '__all__'