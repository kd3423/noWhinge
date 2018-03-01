from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from .forms import ContactForm 
# Create your views here.
def contact(request):
	form = ContactForm(request.POST or None)
	context = {
		"form": form
	}

	if form.is_valid():
		form_email = form.cleaned_data.get("email")
		form_message = form.cleaned_data.get("message")
		form_full_name = form.cleaned_data.get("full_name")

		subject = "noWhinge Team Responding"
		from_email = settings.EMAIL_HOST_USER
		to_email = [form_email]
		contact_message = "%s: %s via %s"%(form_full_name,form_message,form_email)

		some_html_message = """
		We are here to help
		"""
		send_mail(subject,contact_message,from_email,to_email,html_message = some_html_message,fail_silently = True)

	return render(request, "contactform.html", context)