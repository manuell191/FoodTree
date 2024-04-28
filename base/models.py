from django.db import models
from django.contrib.auth.models import User

CATEGORY = (
	("SINGLE", "Signle"),
	("BUNDLE", "Bundle")
)

# Create your models here.
class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE) # username and password

class Event(models.Model):
	start_time = models.TimeField()
	end_time = models.TimeField()
	items = models.CharField(max_length=256)
	category = models.CharField(
		max_length=20,
		choices=CATEGORY,
		default='SINGLE'
	)
	amount = models.IntegerField()
	user = models.ManyToManyField(Profile)
	code = models.IntegerField()

class Service(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE) # username and password
	address = models.CharField(max_length=1024)
	event = models.ManyToManyField(Event, null=True, default=None)