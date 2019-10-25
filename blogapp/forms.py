from django import forms
from .models import Realuser


class Signupform(forms.Form):
    name = forms.CharField(label='Name', max_length=100, required=False)
    address = forms.CharField(label='Address', max_length=100, required=False)
    email = forms.EmailField(label='Email', max_length=100, required=False)
    pwd = forms.CharField(widget=forms.PasswordInput, label='Password', required=False)
    cpwd = forms.CharField(widget=forms.PasswordInput, label='Confirm Password', required=False)

    def clean_pwd(self):
        print("clean data--------------->pasworddd")

        password = self.cleaned_data.get('pwd')
        if(password == ""):
            raise forms.ValidationError("This field is required!!")
        if len(password) < 4:
            raise forms.ValidationError("password is too short")
        return password

    def clean_email(self):

        email = self.cleaned_data.get('email')

        if(email ==""):
            raise forms.ValidationError("This field is required!!")
        emails = Realuser.objects.filter(email=email)

        for i in emails:
            if(i.email==email):
              raise forms.ValidationError("Email Already Exist!")
            if '@' in email:
              pass
            else:
                raise forms.ValidationError("Invalid Email")
        return email
    #
    def clean_name(self):

            uname = self.cleaned_data.get('name')
            if (uname == ""):
                raise forms.ValidationError("This field is required!!")

            for i in uname:

                if i.isdigit():
                   raise forms.ValidationError("Username must be a string !!!")

            print("uname ---------->", uname)
            names = Realuser.objects.filter(username=uname)
            for j in names:

                if uname == j.username :
                    raise forms.ValidationError("Username Already Exist!")
            return uname

    def clean_cpwd(self):
        cpassword = self.cleaned_data.get('cpwd')
        if (cpassword == ""):
            raise forms.ValidationError("This field is required!!")
        return cpassword

    def clean_address(self):
        address = self.cleaned_data.get('address')
        if (address == ""):
            raise forms.ValidationError("This field is required!!")
        return address

    class Meta:
        model = Realuser


class LoginForm(forms.Form):
    uname = forms.CharField(label='Username', max_length=100)
    pwd = forms.CharField(widget=forms.PasswordInput, label='Password')


    class Meta:
        model = Realuser

# class CategoryForm(forms.Form):
#     cat_name = forms.CharField(label='Category name', max_length=100)