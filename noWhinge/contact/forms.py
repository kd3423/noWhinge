from django import forms

class ContactForm(forms.Form):
	name = forms.CharField()
	email = forms.EmailField()
	message = forms.CharField(max_length=1500)

	def clean_name(self):
		return self.cleaned_data.get('name')

	def clean_email(self):
		return self.cleaned_data.get('email')
	
	def clean_message(self):
		return self.cleaned_data.get('message')
	