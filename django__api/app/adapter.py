from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from django.contrib.auth.models import User


class MySocialAccountAdapter(DefaultSocialAccountAdapter):
    def pre_social_login(self, request, sociallogin):
        user = sociallogin.user
        if user.id:
            return
        try:
            # If user exists, connect the account to the existing account and login
            user = User.objects.get(email=user.email)
            sociallogin.connect(request, user)
        except User.DoesNotExist:
            pass

