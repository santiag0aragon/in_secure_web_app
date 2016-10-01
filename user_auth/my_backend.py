from django.conf import settings
from django.contrib.auth.models import User

class SettingsBackend(object):
    """
    Authenticate against the settings ADMIN_LOGIN and ADMIN_PASSWORD.

    Use the login name, and a hash of the password. For example:

    ADMIN_LOGIN = 'admin'
    ADMIN_PASSWORD = 'sha1$4e987$afbcf42e21bd417fb71db8c66b321e9fc33051de'
    """

    def authenticate(self, username=None, password=None):


        try:
            query = "SELECT * from auth_user WHERE username ='%s'" % username
            user = User.objects.raw(query)
            print user
            result = ""
            for u in user:
                result+="\n%s"%u
            print len(list(user))
            # user = User.objects.get(username=username)
            user_pass = user[0].weakuser.weak_pwd
            pwd_valid = (password == user_pass)
            if pwd_valid:
                return user[0]
            print("The password is valid, but the account has been disabled!")
        except User.DoesNotExist:
            return result
        return result

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
