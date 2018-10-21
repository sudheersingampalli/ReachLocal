from django.db import models

# Create your models here.
class News(models.Model):
	source_name = models.CharField(max_length = 300,null=True)
	author = models.CharField(max_length = 300,null=True)
	title = models.CharField(max_length = 500,null=True)
	description = models.TextField(null=True)
	url = models.URLField(max_length = 500, primary_key = True)
	published_date = models.DateTimeField(null=True)
	content = models.TextField(null=True)


	def __str__(self):
		return self.source_name +' '+self.title+' '+str(self.published_date)