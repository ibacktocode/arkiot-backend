from users.models import User

class UserAuth:

    def authenticate(self, request=None, phone_number=None, password=None):
        try:
            user = User.objects.get(phone_number=phone_number)
            if user.check_password(password) and self.user_can_authenticate(user):
                return user

        except User.DoesNotExists:
            return None

    def user_can_authenticate(self, user):
        """
        Reject users with is_active=False. Custom user models that don't have
        that attribute are allowed.
        """
        is_active = getattr(user, 'is_active', None)
        return is_active or is_active is None

    def get_user(self, user_id):
        try:
            user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
        return user if self.user_can_authenticate(user) else None