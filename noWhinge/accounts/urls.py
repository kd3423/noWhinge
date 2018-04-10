from django.urls import path

from . import views


urlpatterns = [
    path('signup/', views.SignUp_test, name='signup'),
]