from django.shortcuts import render,redirect
from .forms import AnalysisForm
from complaintform.models import Complaints
from math import sin, cos, sqrt, atan2, radians
# [lat,lon]
dict_lat_lon = {'Model Town':[28.696423,77.194936],'IIITD':[28.545628,77.273150],'Malviya Nagar':[28.533520,77.210886]}
lat_lon_list = []
glob_center = [28.7040592, 77.1024902]
resolved = [0,0]

def cal_dist(lat1,lon1,lat2,lon2):
	
	# approximate radius of earth in km
	R = 6373.0
	lat1 = radians(lat1)
	lon1 = radians(lon1)
	lat2 = radians(lat2)
	lon2 = radians(lon2)

	dlon = lon2 - lon1
	dlat = lat2 - lat1

	a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
	c = 2 * atan2(sqrt(a), sqrt(1 - a))

	# distance in KM
	distance = R * c
	return distance

def analysis_form(request):
	form = AnalysisForm(request.POST or None)
	context = {
		"form": form
	}
	return render(request,"analysis.html",context)

def analysis_page(request):
	# print(request)
	lat_lon_list = []
	resolved = [0,0]
	if request.method == "POST":
		#Get the posted form
		# print(request.POST)
		MyProfileForm = AnalysisForm(request.POST)
		print('after request')
		# print(MyProfileForm.is_valid())
		
		if MyProfileForm.is_valid():
			issue= MyProfileForm.cleaned_data['issue']        
			locality= MyProfileForm.cleaned_data['locality']

			center = [dict_lat_lon[locality][0],dict_lat_lon[locality][1]]
			complaintsData = Complaints.objects.all()
			for entry in complaintsData:
				if issue == entry.issue and locality == entry.locality:
					if cal_dist(dict_lat_lon[entry.locality][0],dict_lat_lon[entry.locality][1],float(entry.lat),float(entry.lon)) <= 5.00:
						# print(entry.first_name,entry.last_name,entry.lat,entry.lon,entry.issue)
						lat_lon_list.append([float(entry.lat),float(entry.lon)])
						if entry.resolved == 1:
							resolved[0]+=1
						else:
							resolved[1]+=1
			print(resolved)
			# print(lat_lon_list)
			return render(request, 'analysis.html', {'lat_lon_list': lat_lon_list , 'center': center , 'zoom': 15 , 'u_resolved': resolved})
		else:
			return render(request, 'analysis.html', {'lat_lon_list': lat_lon_list , 'center': glob_center , 'zoom': 12, 'u_resolved': resolved})
	else:
		return render(request, 'analysis.html', {'lat_lon_list': lat_lon_list , 'center': glob_center , 'zoom': 12 , 'u_resolved': resolved})

