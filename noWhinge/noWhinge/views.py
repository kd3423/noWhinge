from django.shortcuts import render,render_to_response
from .forms import ComplaintForm 
from .settings import MEDIA_ROOT
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.utils.safestring import mark_safe

from complaintform.models import Complaints

# Create your views here.
def complaint_page(request):
	return render(request,"complaint_page.html",{})

def about_page(request):
	return render(request,"about.html",{})

def analysis_page(request):
	return render(request,"analysis.html",{})

def complaintpage(request):

	print(MEDIA_ROOT)
	
	form = ComplaintForm(request.POST or None)
	context = {
		"form": form
	}
	# return render(request,"complaintform.html",context)
	return render(request,"complaint_page.html",context)

def home(request):
	return render(request, 'home.html')
	
def userProfile_page(request):
	complaints_data=Complaints.objects.filter(user_name = request.user.get_username()) #This is a list of all complaints
	#for i in complaints_data: #For itereating
	#	print (i.user_name) #For getting this field data -- For checking which all fields are there check complaintform/models.py
	#	print (i.locality)
	#	print (i.resolved)
	#	print ("-------")

	complaint=json.dumps(list(complaints_data.values()),cls=DjangoJSONEncoder)
	print(complaint)
	#print (Complaints.objects.filter(user_name = request.user.get_username()))
	return render(request,"userProfile_page.html",{'complaint':mark_safe(complaint)})
	#return {"complaint":complaints_data}

	

def thankyou(request):
	return render(request,'thankYou.html',{})