from django.db import models

class Complaints(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	user_name = models.CharField(max_length=50,default='nowhinge@gmail.com')
	date = models.DateTimeField()
	lat = models.CharField(max_length=50)
	lon = models.CharField(max_length=50)
	issue = models.CharField(max_length=50)
	locality = models.CharField(max_length=50)
	desc=models.CharField(max_length=100)
	photo = models.ImageField(upload_to = 'pictures',default='noWhinge_Logo.png')

	class Meta:
		db_table = "Complaints"