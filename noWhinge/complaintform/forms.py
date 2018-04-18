from django import forms

class ComplaintForm(forms.Form):
	first_name = forms.CharField()
	last_name = forms.CharField()
	lat = forms.DecimalField()
	lon = forms.DecimalField()
	issue = forms.CharField()
	locality = forms.CharField()
	# issue = forms.MultipleChoiceField(widget=forms.CheckboxSelect,choices=OPTIONS)
	# locality = forms.MultipleChoiceField()
	desc = forms.CharField(max_length=1500,required=False)
	photo = forms.ImageField(required=False)
	ref_no = forms.CharField()
	# file = forms.FileField()
	
	def clean_first_name(self):
		return self.cleaned_data.get("photo")

	def clean_first_name(self):
		return self.cleaned_data.get("first_name")

	def clean_last_name(self):
		return self.cleaned_data.get("last_name")
	
	def clean_lat(self):
		return self.cleaned_data.get("lat")
	def clean_lon(self):
		return self.cleaned_data.get("lon")

	def clean_issue(self):
		return self.cleaned_data.get("issue")

	def clean_desc(self):
		return self.cleaned_data.get("desc")

	def clean_locality(self):
		return self.cleaned_data.get("locality")

