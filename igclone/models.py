from django.db import models

# Create your models here.

class Profile(models.Model):
	bio = models.CharField(max_length = 300,blank = True,default = 'Bio Will Appear Here')

	