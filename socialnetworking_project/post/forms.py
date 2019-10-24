from django import forms
from django.forms import DateInput

from socialnetworking_project.post.models import User

class UserRegisterForm(forms.ModelForm):
    username = forms.EmailField(label= 'Email Address')
    email = forms.EmailField(label='Confirm Email')
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label='Last Name')
    dateofbirth = forms.DateField(label='Date of birth')

    class Meta:
        model = User
        fields =[
            'username',
            'email',
            'password',
            'password2',
            'first_name',
            'last_name',
            'dateofbirth'
        ]