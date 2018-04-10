from django.shortcuts import render,redirect
from .forms import AnalysisForm 
# Create your views here.


def analysis_form(request):
	form = AnalysisForm(request.POST or None)
	context = {
		"form": form
	}
	return render(request,"analysis.html",context)

def analysis_page(request):
	# print(request)
	if request.method == "POST":
		#Get the posted form
		# print(request.POST)
		MyProfileForm = AnalysisForm(request.POST)
		print('after request')
		# print(MyProfileForm.is_valid())
		
		if MyProfileForm.is_valid():
			issue= MyProfileForm.cleaned_data['issue']        
			locality= MyProfileForm.cleaned_data['locality']
			print (issue,locality)
			# print(request.POST)

		return render(request, 'analysis.html', {})
	else:
		return render(request, 'analysis.html', {})