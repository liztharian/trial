from django.db import models

# Create your models here.
from app import constants


class taskmodel(models.Model):
	title=models.CharField(max_length=200)
	description=models.TextField(null=True,blank=True)
	completion_date=models.DateTimeField()
	priority=models.CharField(max_length=200,choices=constants.task_priority)
	is_complete=models.BooleanField(default=False)
	def __str__(self): 
		return self.title
