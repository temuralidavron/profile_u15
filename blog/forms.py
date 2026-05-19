from django import forms
from .models import Blog

class BlogForm(forms.ModelForm):
    class Meta:
        model=Blog
        fields=[
            'title',
            'description',
            'image',
            # 'owner'

        ]

    # def save(self, commit = True):
    #     owner=self.cleaned_data.get('')