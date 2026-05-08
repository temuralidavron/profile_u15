from captcha.fields import CaptchaField
from django import forms
from django.contrib.auth.models import Group

from .models import CustomUser, Profile, UserRole


class RegisterForm(forms.ModelForm):
    class Meta:
        model=CustomUser
        fields=[
            'username',
            'phone',
            'email',
            'password'
        ]


    def save(self, commit = True):
        data=super().clean()
        return CustomUser.objects.create_user(
            username=self.data.get('username'),
            phone=self.data.get('phone'),
            email=self.data.get('email'),
            password=self.data.get('password'),

        )


class LoginForm(forms.Form):
    username=forms.CharField(max_length=300)
    password=forms.CharField(max_length=300)
    captcha=CaptchaField()


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=[
            'avatar',
            'age',
            'bio',

        ]


class ChangeRoleUser(forms.Form):
    user = forms.ModelChoiceField(
        queryset=CustomUser.objects.all(),
        label="Select User",
        empty_label="-- Select User --"
    )
    role = forms.ChoiceField(
        choices=UserRole.choices,
        required=True,
        # Optional: set a default
        initial=UserRole.VIEWER
    )

class UserAddGroupForm(forms.Form):
    user = forms.ModelChoiceField(
        queryset=CustomUser.objects.all(),
        label="Select User",
        empty_label="-- Select User --"
    )
    group = forms.ModelChoiceField(
        queryset=Group.objects.all(),
        label="Select Groups",
        empty_label="-- Select Group --"
    )



class ForgetPasswordForm(forms.Form):
    username=forms.CharField(max_length=300)
    email=forms.CharField(max_length=300)


class DonePasswordForm(forms.Form):
    code=forms.CharField(max_length=6)
    password=forms.CharField(max_length=150)
    re_password=forms.CharField(max_length=150)