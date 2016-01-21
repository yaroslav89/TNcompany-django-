from datetime import date
from django.shortcuts import render
from .forms import LoginForm
from models import *


def home(request):
	title = 'TN Company'
	form = LoginForm()
	year = date.today().year
	about = About.objects.all()[:1]
	services = Service.objects.all()
	events = Event.objects.all().order_by('-date')
	videos = Video.objects.all()
	context = {'year':year, 'title':title, 'about':about, 'services': services, 'events':events, 'videos':videos}

	return render(request,'index.html',context)
