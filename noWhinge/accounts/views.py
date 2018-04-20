from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from .models import UserCustom
from .forms import UserForm


User = get_user_model()

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


def SignUp_test(request):

	if request.method == "POST":
		#Get the posted form
		print(request.POST)
		MyProfileForm = UserForm(request.POST)
		print('after signup')
		print(MyProfileForm.is_valid())
		
		if MyProfileForm.is_valid():
			
			profile = UserCustom()
			profile.first_name=MyProfileForm.cleaned_data['name']
			profile.locality= MyProfileForm.cleaned_data['locality']
			profile.contact= MyProfileForm.cleaned_data['contact']
			profile.email= MyProfileForm.cleaned_data['email']
			profile.username= profile.email
			profile.password= MyProfileForm.cleaned_data['password']


			print(' before user save')
			# profile.save()
			tt = UserCustom.objects.filter(username=profile.username)

			print(tt) 
			if(len(tt)>0):
				#user exists
				return render(request,'signup.html',{'submit':1})
			elif(profile.password != MyProfileForm.cleaned_data['re_password']):
				#password not same
				return render(request,'signup.html',{'submit':2})
			else:
				profile.save()
			print('post user save')

			# t=authenticate_test(profile.username,profile.password)
			t=authenticate(username=profile.username,password=profile.password)
			if(t is not None):
				print('authenticate worked')
				login(request,t)

				return redirect("/")
			else:
				print('authenticate failed')
				return render(request, 'signup.html', {'submit':0})		
		return render(request, 'signup.html', {'submit':4})
	else:
		
		return render(request, 'signup.html', {'submit':0})

def authenticate_test(usr,pas):
	tt=UserCustom.objects.get(username=usr)
	if(tt is not None):
		if(tt.password==pas):
			return True
		else:
			return False
	else:
		print('No user')
		return False
