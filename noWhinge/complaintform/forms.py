from django import forms

class ComplaintForm(forms.Form):
	OPTIONS = (("a", "A"),("b", "B"),)
	first_name = forms.CharField()
	last_name = forms.CharField()
	date = forms.DateTimeField()
	lat = forms.DecimalField()
	lon = forms.DecimalField()
	issue = forms.CharField()
	locality = forms.CharField()
	# issue = forms.MultipleChoiceField(widget=forms.CheckboxSelect,choices=OPTIONS)
	# locality = forms.MultipleChoiceField()
	problem_description = forms.CharField(max_length=1500,
        widget=forms.Textarea())
	file = forms.FileField()
	
	def clean_first_name(self):
		return first_name

	def clean_last_name(self):
		return last_name
	def clean_date(self):
		return date
	def clean_lat(self):
		return lat
	def clean_lon(self):
		return lon
	def clean_issue(self):
		return issue
	def clean_problem(self):
		return problem_description