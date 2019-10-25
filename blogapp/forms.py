from django import forms
from .models import Realuser


class Signupform(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    address = forms.CharField(label='Address', max_length=100)
    email = forms.CharField(label='Email', max_length=100)
    pwd = forms.CharField(widget=forms.PasswordInput, label='Password')
    cpwd = forms.CharField(widget=forms.PasswordInput, label='Confirm Password')

    def clean_pwd(self):
        print("clean data--------------->")
        password = self.cleaned_data.get('pwd')
        if len(password) < 4:
            raise forms.ValidationError("password is too short")
        return password

    # def clean_email(self):
    #     print("clean data--------------->")
    #     email = self.cleaned_data.get('email')
    #     if len(email) < 4:
    #         raise forms.ValidationError("password is too short")
    #     return password

    class Meta:
        model = Realuser

class LoginForm(forms.Form):
    uname = forms.CharField(label='Username', max_length=100)
    pwd = forms.CharField(widget=forms.PasswordInput, label='Password')

    class Meta:
        model = Realuser

# class CategoryForm(forms.Form):
#     cat_name = forms.CharField(label='Category name', max_length=100)