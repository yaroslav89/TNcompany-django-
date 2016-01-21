from django.contrib import admin
from models import *

class EventModelAdmin(admin.ModelAdmin):
	list_display = ['__unicode__', 'date']
	class Meta:
		model = Event



admin.site.register(About)
admin.site.register(Service)
admin.site.register(Event, EventModelAdmin)
admin.site.register(Photo)
admin.site.register(Video)
