from django.shortcuts import render
from .forms import ComplaintForm 
from .settings import MEDIA_ROOT

# Create your views here.
<<<<<<< HEAD
def complaint_page(request):
	return render(request,"complaint_page.html",{})

def about_page(request):
	return render(request,"about.html",{})

def contact_page(request):
	return render(request,"contactform.html",{})
=======
def complaintpage(request):

	print(MEDIA_ROOT)
	
	form = ComplaintForm(request.POST or None)
	context = {
		"form": form
	}
	# return render(request,"complaintform.html",context)
	return render(request,"complaint_page.html",context)


	
>>>>>>> d5f010d7d985c0cde01266a0ffb07f1652938cb5
