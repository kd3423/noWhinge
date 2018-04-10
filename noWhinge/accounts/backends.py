from django.conf import settings
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from .models import UserCustom

User = get_user_model()

class SettingsBackend:
    """
    Authenticate against the settings ADMIN_LOGIN and ADMIN_PASSWORD.

    Use the login name and a hash of the password. For example:

    ADMIN_LOGIN = 'admin'
    ADMIN_PASSWORD = 'pbkdf2_sha256$30000$Vo0VlMnkR4Bk$qEvtdyZRWTcOsCnI/oQ7fVOu1XAURIZYoOZ3iq8Dr4M='
    """

    def authenticate(self, request, username=None, password=None):
        try:
            user = UserCustom.objects.get(username=username)
        except UserCustom.DoesNotExist:
            # Create a new user. There's no need to set a password
            # because only the password from settings.py is checked.
            user = UserCustom(username=username)
            user.is_staff = True
            user.is_superuser = True
            print("saving user from authenticate")
            user.save()
        if(user.password==password):
            return user
        else:
            return None
        return None

    def get_user(self, user_id):
        try:
            return UserCustom.objects.get(pk=user_id)
        except UserCustom.DoesNotExist:
            return None