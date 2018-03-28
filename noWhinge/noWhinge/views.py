from django.shortcuts import render
from .forms import ComplaintForm 
from .settings import MEDIA_ROOT

# Create your views here.
def complaintpage(request):

	print(MEDIA_ROOT)
	
	form = ComplaintForm(request.POST or None)
	context = {
		"form": form
	}
	# return render(request,"complaintform.html",context)
	return render(request,"complaint_page.html",context)


	