from __future__ import unicode_literals
from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver

class About(models.Model):
	title = models.CharField(max_length=140, blank=False)
	description = models.TextField(blank=False)

	def __unicode__(self):
		return self.title


class Service(models.Model):
	title = models.CharField(max_length=140, blank=False)
	description = models.TextField(blank=False)
	image = models.ImageField(upload_to='services')

	def __unicode__(self):
		return self.title


class Event(models.Model):
	title = models.CharField(max_length=140, blank=False)
	description = models.TextField(blank=False)
	date = models.DateField(auto_now=False, auto_now_add=True)

	def __unicode__(self):
		return self.title


class Photo(models.Model):
	event_id = models.ForeignKey(Event, on_delete=models.CASCADE)
	image = models.ImageField(upload_to='events')
	
	def __unicode__(self):
		return self.image.url


class Video(models.Model):
	iframe = models.CharField(max_length=250)

	def __unicode__(self):
		return str(self.pk)


@receiver(pre_delete, sender=Photo)
def photo_delete(sender, instance, **kwargs):
	instance.image.delete(False)

@receiver(pre_delete, sender=Service)
def service_delete(sender, instance, **kwargs):
	instance.image.delete(False)