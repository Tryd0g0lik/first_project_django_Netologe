from django.db import models

# Create your models here.
class firstModelPost(models.Model):
	 title_var  = models.CharField(max_length=100)
	 Description_var = models.TextField(null=True)
	 DateTime_var = models.DateTimeField(auto_now_add=True)

	 def __str__(self):
		 return  self.DateTime_var