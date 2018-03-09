from django.shortcuts import render

# Create your views here.
def complaint_page(request):
	return render(request,"complaint_page.html",{})