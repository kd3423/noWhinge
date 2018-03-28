from django.shortcuts import render
from .forms import ComplaintForm 

# Create your views here.
def complaint_page(request):
	
	form = ComplaintForm(request.POST or None)
	context = {
		"form": form
	}
	# return render(request,"complaintform.html",context)
	return render(request,"complaint_page.html",context)


	