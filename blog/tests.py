from django.test import TestCase

from accounts.models import CustomUser


# Create your tests here.


class UserDetail:

    def get_user(self,id):
        return CustomUser.objects.get(pk=id)