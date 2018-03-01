from django.shortcuts import render
from .forms import SignUpForm

# Create your views here.
def home(request):

	title = 'Welcome'

	# Adding form
	form = SignUpForm(request.POST or None)
	context = {
		"title":title,
		"form":form
	}

	# if form.is_valid():
	# 	instance = form.save(commit = False)
	# 	email = form._email.get('email')
	# 	phone = form._phone.get('phone_number')

	# 	existing_user_email = User.objects.filter(email=form._email.get('email')).first()
	# 	existing_user_phone = User.objects.filter(phone_number=form._phone.get('phone_number')).first()

	# 	if existing_user_phone and existing_user_email:
	# 		pass
	# 	else:
	# 		instance.save()
	# 		context = {
	# 			"title": "Thank YOU"
	# 		}
	return render(request,"base.html",context)
