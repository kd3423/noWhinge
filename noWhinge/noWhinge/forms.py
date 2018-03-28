from django import forms

class ComplaintForm(forms.Form):
	# OPTIONS = (("a", "A"),("b", "B"),)
	first_name = forms.CharField(max_length = 25)
	last_name = forms.CharField(max_length = 25)
	date = forms.DateTimeField()
	lat = forms.DecimalField()
	lon = forms.DecimalField()
	issue = forms.CharField()
	locality = forms.CharField()
	# issue = forms.MultipleChoiceField(widget=forms.CheckboxSelect,choices=OPTIONS)
	# locality = forms.MultipleChoiceField()
	problem_description = forms.CharField(max_length=600,widget=forms.Textarea())

	file = forms.FileField()
	
	# def clean_first_name(self):
	# 	return first_name

	# def clean_last_name(self):
	# 	return last_name
	# def clean_date(self):
	# 	return date
	# def clean_lat(self):
	# 	return lat
	# def clean_lon(self):
	# 	return lon
	# def clean_issue(self):
	# 	return issue
	# def clean_problem(self):
	# 	return problem_description

	# email = forms.CharField(max_length=150,widget=forms.HiddenInput())

	def clean(self):
	    cleaned_data = super(ComplaintForm, self).clean()
	    first_name = cleaned_data.get('first_name')
	    last_name = cleaned_data.get('last_name')
	    # email = cleaned_data.get('email')
	    issue = cleaned_data.get('issue')
	    locality = cleaned_data.get('locality')
	    problem_description = cleaned_data.get('problem_description')
	    if not first_name and not last_name and not problem_description and not issue and not locality:
	        raise forms.ValidationError('You have to fill something!')