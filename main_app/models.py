from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Message(models.Model):
	text_content = models.CharField(max_length=32)
	poster = models.ForeignKey(User, on_delete=models.CASCADE, default=99)
	timestamp = models.CharField(max_length=32)

	def get_absolute_url(self):
		return ""

	def __str__(self):
		return self.text_content