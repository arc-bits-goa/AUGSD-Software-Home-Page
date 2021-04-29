from django.db import models

# Create your models here.

class Portal(models.Model):
	name = models.CharField(max_length=200)
	link = models.CharField(max_length=200)
	description = models.CharField(max_length=1000 , default = 'nothing has been added here')
	repo_link = models.CharField(max_length=1000 , default = '#')
	repo_link2 = models.CharField(max_length=1000 , default="NA")
	Add_repo_link  = models.BooleanField(default=False)

	def __str__(self):
		return self.name

class Script(models.Model):
	name = models.CharField(max_length=200)
	link = models.CharField(max_length=200)
	description = models.CharField(max_length=1000 , default = 'nothing has been added here')
	repo_link = models.CharField(max_length=1000 , default = '#')
	repo_link2 = models.CharField(max_length=1000 , default="NA")
	Add_repo_link  = models.BooleanField(default=False)

	def __str__(self):
		return self.name