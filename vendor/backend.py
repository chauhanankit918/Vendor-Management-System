from .models import Vendor


class EmailAuthentication(object):
    def authenticate(self, request, username=None, password=None):
        try:
            user = Vendor.objects.get(email=username)
            if user.check_password(password):
                return user
            return None
        except Vendor.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            user = Vendor.objects.get(id=user_id)
            return user
        except Vendor.DoesNotExist:
            return None
