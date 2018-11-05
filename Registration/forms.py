from django import forms
from Registration.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('firstname','lastname','email','password','address','city','profile_pic')