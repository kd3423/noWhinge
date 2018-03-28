from django.shortcuts import render,redirect
from .forms import ComplaintForm 
from .models import Complaints
import datetime

# Create your views here.


def complaintform(request):
	form = ComplaintForm(request.POST or None)
	context = {
		"form": form
	}
	return render(request,"complaintform.html",context)

def complaint_page(request):

	if request.method == "POST":
		#Get the posted form
		print(request.POST)
		MyProfileForm = ComplaintForm(request.POST,request.FILES)
		print('after request')
		print(MyProfileForm.is_valid())
		
		if MyProfileForm.is_valid():
			print('before Complaints')
			profile = Complaints()
			print('post Complaints')
			profile.first_name=MyProfileForm.cleaned_data['first_name']
			profile.last_name= MyProfileForm.cleaned_data['last_name']
			profile.issue= MyProfileForm.cleaned_data['issue']        
			profile.locality= MyProfileForm.cleaned_data['locality']
			profile.desc= MyProfileForm.cleaned_data['desc']
			profile.lat=MyProfileForm.cleaned_data['lat']
			profile.lon=MyProfileForm.cleaned_data['lon']
			profile.date=datetime.datetime.now()
			profile.photo=MyProfileForm.cleaned_data['photo']
			print('before save')
			profile.save()
			print('post save')
			print(request.POST)

			saved = True
			return redirect("/")
		return render(request, 'complaint_page.html', {})
	else:
		MyProfileForm = ComplaintForm()
		return render(request, 'complaint_page.html', {})

def SaveProfile(request):

	print("sup")
	saved = False


	if request.method == "POST":
		#Get the posted form
		print(request.POST)
		MyProfileForm = ComplaintForm(request.POST)
		print('after request')
		print(MyProfileForm.is_valid())

		if MyProfileForm.is_valid():
			print('before Complaints')
			profile = Complaints()
			print('post Complaints')
			profile.first_name=MyProfileForm.cleaned_data['first_name']
			profile.last_name= MyProfileForm.cleaned_data['last_name']
			profile.issue= MyProfileForm.cleaned_data['issue']        
			profile.locality= MyProfileForm.cleaned_data['locality']
			profile.desc= MyProfileForm.cleaned_data['desc']
			profile.lat=MyProfileForm.cleaned_data['lat']
			profile.lon=MyProfileForm.cleaned_data['lon']
			profile.date=datetime.datetime.now()
			print('before save')
			profile.save()
			print('post save')
			print(request.POST)

			saved = True
			return render(request, 'base.html', {})
		return render(request, 'complaint_page.html', {})
	else:
		MyProfileForm = ComplaintForm()
		return render(request, 'complaint_page.html', {})