from django.shortcuts import render
from .forms import ComplaintForm 
# Create your views here.
def complaintform(request):
	form = ComplaintForm(request.POST or None)
	context = {
		"form": form
	}
	return render(request,"complaintform.html",context)