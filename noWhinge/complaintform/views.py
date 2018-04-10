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

	if request.method == "POST": #Post request object
		print (request.user.is_authenticated)
		if request.user.is_authenticated: #Check if the user is logged in
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
				profile.user_name = request.user.get_username() #Get the usermane of the user
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
			return redirect('/accounts/login') #Redirect to the login page if not authenticated 
	else:
		return render(request, 'complaint_page.html', {})