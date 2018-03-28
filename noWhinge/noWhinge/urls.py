"""noWhinge URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static 
from django.contrib import admin
from django.urls import path, include
from newsletter import views
import newsletter
from contact import views
import contact
from noWhinge import views
import noWhinge
from complaintform import views
import complaintform


urlpatterns = [
	path('', newsletter.views.home, name='home'),
	path('contact/', contact.views.contact, name='contact'),
    path('complaint_page/', complaintform.views.complaint_page, name='complaint_page'),
    path('admin/', admin.site.urls),
	path('accounts/', include('accounts.urls')),
	path('accounts/', include('django.contrib.auth.urls')),
    # path('test/',noWhinge.views.complaintpage,name='test')
    # path('l/', complaintform.views.SaveProfile, name='SaveProfile'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)