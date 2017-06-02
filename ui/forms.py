from django import forms
from django.contrib.auth import authenticate, login, logout


class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    
    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username,password=password)
        
        if not user:
            raise forms.ValidationError('There is no such user')
        if not user.check_password:
            raise forms.ValidationError('Password is not correct')
        if not user.is_active:
            raise forms.ValidationError('User is not active')
        
        return super(UserLoginForm,self).clean(*args, **kwargs)
        
       