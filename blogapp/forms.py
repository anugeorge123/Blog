from django import forms
from .models import Realuser,Category, Ingredients, Recipe,Type


class Signupform(forms.Form):
    name = forms.CharField(label='Name', max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    # address = forms.CharField(label='Address', max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Email', max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    pwd = forms.CharField(label='Password', required=False, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    cpwd = forms.CharField(label='Confirm Password', required=False, widget=forms.PasswordInput(attrs={'class': 'form-control'}))

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
        if(email == ""):
            raise forms.ValidationError("This field is required!!")
        emails = Realuser.objects.filter(email=email)

        for i in emails:
            if(i.email == email):
              raise forms.ValidationError("Email Already Exist!")
            if '@' in email:
              pass
            else:
                raise forms.ValidationError("Invalid Email")
        return email

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
    uname = forms.CharField(label="Username", widget=forms.TextInput(attrs={'class': 'form-control'}))
    pwd = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}), label='Password')

    class Meta:
        model = Realuser

#
# class RecipesForm(forms.Form):
#     category = forms.CharField(label="Category Name", max_length=100)
#     # ingredients = forms.CharField(label="Ingredients", max_length=100)
#     type = forms.CharField(label="Type", max_length=100)
#     recipe = forms.CharField(label="Recipe", max_length=100)
#     # prep = forms.CharField(label="Prep", max_length=100)
#     # cook = forms.CharField(label="Cook", max_length=100)
#     # yields = forms.CharField(label="Yields", max_length=100)
#     # steps = forms.CharField(label="Steps", max_length=255)
#
#     class Meta:
#         model = Category, Ingredients, Type, Recipe
