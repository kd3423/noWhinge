from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class SignUp(models.Model):
	full_name = models.CharField(max_length = 120, blank = False, null = True)
	email = models.EmailField()

	phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+91 9999999999'. Up to 15 digits allowed.")
	phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=False) # validators should be a list

	timestamp = models.DateTimeField(auto_now_add= True, auto_now = False)
	updated = models.DateTimeField(auto_now_add= False, auto_now = True)

	def __str__(self):
		return self.email