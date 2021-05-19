from django import forms
from .models import Video
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = '__all__'


class SinupForm(forms.ModelForm):
    rpassword=forms.CharField(max_length=30)
    class Meta:
        model=User
        fields=['username','first_name','last_name','email' ,"password",'rpassword']


    def clean(self):
        total_data=super().clean()
        password=total_data['password']
        rpassword=total_data['rpassword']
        if password !=rpassword:
            raise ValidationError("password and rpassword should be same")
