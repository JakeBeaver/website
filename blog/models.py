from django.db import models

# Create your models here.
class posts(models.Model):
	title = models.CharField(max_length = 100)
	body = models.TextField()
	timestamp = models.DateTimeField('timestamp')
	
	def __unicode__(self):
		return self.title
