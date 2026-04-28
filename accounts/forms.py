from django import forms
from .models import CustomUser,Profile

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


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=[
            'avatar',
            'age',
            'bio',

        ]
