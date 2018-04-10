from django import forms

class UserForm(forms.Form):
	name = forms.CharField()
	email = forms.CharField()
	contact = forms.CharField()
	locality = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)
	re_password = forms.CharField(widget=forms.PasswordInput)

	def clean_name(self):
		return self.cleaned_data.get("name")

	def clean_email(self):
		return self.cleaned_data.get("email")

	def clean_contact(self):
		return self.cleaned_data.get("contact")

	def clean_locality(self):
		return self.cleaned_data.get("locality")

	def clean_password(self):
		return self.cleaned_data.get("password")

	def clean_re_password(self):
		return self.cleaned_data.get("re_password")
	