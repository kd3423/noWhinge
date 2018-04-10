
from django import forms

class AnalysisForm(forms.Form):
	issue = forms.CharField()
	locality = forms.CharField()

	def clean_issue(self):
		return self.cleaned_data.get("issue")

	def clean_locality(self):
		return self.cleaned_data.get("locality")
	