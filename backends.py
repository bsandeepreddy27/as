from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User

class UsernameOrEmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            # Try finding the user by username
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            try:
                # If not found, try finding by email
                user = User.objects.get(email=username)
            except User.DoesNotExist:
                return None
        # Check if the password is valid
        if user.check_password(password) and self.user_can_authenticate(user):
            return user
        return None
