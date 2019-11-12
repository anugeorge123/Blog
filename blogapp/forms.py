from django import forms
from .models import Realuser,Category, Ingredients, Recipe,Type, Newsletter, Contact, Review


class Signupform(forms.Form):
    name = forms.CharField(label='Name', max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Email', max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    pwd = forms.CharField(label='Password', required=False, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    cpwd = forms.CharField(label='Confirm Password', required=False, widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def clean_pwd(self):
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

class NewsLetterForm(forms.Form):

    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Your E-mail'}),required=False)

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if '@' in email:
            pass
        else:
            raise forms.ValidationError("Invalid Email")
        if(email == ""):
            raise forms.ValidationError("This field is required!!")
        emails = Newsletter.objects.filter(email=email)

        for i in emails:
            if(i.email == email):
              raise forms.ValidationError("Email Already Exist!")

        return email

    class Meta:
        model = Newsletter

class CommentForm(forms.Form):
    subject = forms.CharField(label='',widget=forms.TextInput(attrs={'class': 'contact-form textarea','placeholder':'Subject'}))
    message = forms.CharField(label='',widget=forms.TextInput(attrs={'class':'contact-form textarea','placeholder':'Message'}))


    def clean_subject(self):
            subject = self.cleaned_data.get('subject')
            if (subject == ""):
                raise forms.ValidationError("This field is required!!")
            return subject

    def clean_message(self):
            message = self.cleaned_data.get('message')
            if (message == ""):
                raise forms.ValidationError("This field is required!!")
            return message

    class Meta:
        model = Review

class CotactForm(forms.Form):
    name = forms.CharField(label='',widget=forms.TextInput(attrs={'class': 'contact-form textarea','placeholder':'Name'}))
    email = forms.CharField(label='',widget=forms.TextInput(attrs={'class': 'contact-form textarea','placeholder':'E-mail'}))
    subject = forms.CharField(label='',widget=forms.TextInput(attrs={'class': 'contact-form textarea','placeholder':'Subject'}))
    message = forms.CharField(label='',widget=forms.TextInput(attrs={'class':'contact-form textarea','placeholder':'Message'}))

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if (name == ""):
            raise forms.ValidationError("This field is required!!")
        return name

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if '@' in email:
            pass
        else:
            raise forms.ValidationError("Please input a valid email id !")
            return email

        if (email == ""):
            raise forms.ValidationError("This field is required!!")
        return email

    def clean_subject(self):
            subject = self.cleaned_data.get('subject')
            if (subject == ""):
                raise forms.ValidationError("This field is required!!")
            return subject

    def clean_message(self):
            message = self.cleaned_data.get('message')
            if (message == ""):
                raise forms.ValidationError("This field is required!!")
            return message

    class Meta:
        model = Contact


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
