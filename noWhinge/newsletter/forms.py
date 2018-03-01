from django import forms
from .models import SignUp

class SignUpForm(forms.ModelForm):
	class Meta:
		model = SignUp
		fields = ['full_name','email','phone_number']

	def _email(self):
		return email

	def _phone(self):
		return phone_number