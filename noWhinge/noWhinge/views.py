from django.shortcuts import render

# Create your views here.
def complaint_page(request):
	return render(request,"complaint_page.html",{})

def about_page(request):
	return render(request,"about.html",{})

def contact_page(request):
	return render(request,"contactform.html",{})
