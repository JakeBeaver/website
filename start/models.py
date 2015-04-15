from django.db import models

# Create your models here.

class tweet(models.Model):
	timestemp = models.DateTimeField('date published')
	body = models.CharField(max_length = 200)
	
	def __unicode__(self):
		result=self.body
		cut = 20
		if len(result) > cut:
			result = result[:cut] + "..."
		return result
