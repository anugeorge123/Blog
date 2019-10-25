from django.shortcuts import render
from django.http import HttpResponse, request
from django.views.generic import View
from blogapp.models import Realuser
from django.contrib.auth import login, authenticate
# from django.contrib.auth.models import Realuser
from django.contrib.auth.hashers import check_password
from .forms import Signupform, LoginForm
from django.contrib.auth.decorators import login_required



import json

class Home(View):


    def get(self, request):
        form = Signupform()
        login = LoginForm()
        return render(request, "index.html",{'id':form,'log': login})

    def post(self,request):
        dict1 = {}
        form = Signupform(request.POST)
        if form.is_valid():
               try:

                    name = form.cleaned_data['name']
                    address = form.cleaned_data['address']
                    email = form.cleaned_data['email']
                    pwd = form.cleaned_data['pwd']
                    cpwd = form.cleaned_data['cpwd']

                    if pwd == cpwd :
                        obj = Realuser.objects.create_user(is_superuser="0", username=name, address=address, email=email, password=pwd)
                        obj.save()
                        dict1['val'] = "Success"

                    else:
                        dict1['val'] = "failure"
                    # return HttpResponse(json.dumps(dict1), content_type="application/json")
               except Exception as e:
                    print("Error: ", e)
                    dict1['result'] = "Error"

               # return HttpResponse(json.dumps(dict1), content_type="application/json")
        else:
            print("form eroors: ---------------->", form.errors)
            dict1['val'] = "Error in forms"
            dict1['dict1']=form.errors
        return HttpResponse(json.dumps(dict1), content_type="application/json")

class Login(View):
    # print("fjfggfytgfvyvuhguyhguhgbuhfhvvfvtgfvgyfvgvcfycfcfcfyfhgjhuytgyf")
    # def get(self, request):
    #     login = LoginForm()
    #     return render(request, "index.html",{'log': login})
    @login_required
    def post(self, request):
        dict2 = {}
        login = LoginForm(request.POST)
        if login.is_valid():
            uname = login.cleaned_data['uname']
            pwd = login.cleaned_data['pwd']
            print("uname: ", uname, "password: ", pwd)
            try:
                obj = Realuser.objects.get(username=uname)
                u = obj.username
                p = obj.password
                matchcheck = check_password(pwd, obj.password)
                if matchcheck and uname == u:
                    print("----------------------------------------->",matchcheck)
                    dict2['val'] = "success"

                else:
                    dict2['val'] = "failed"
                return HttpResponse(json.dumps(dict2), content_type="application/json")
            except Exception as e:
                print(e)
# #
#
# class Category(View):
#     def get_name(request):
#        obj = CategoryForm()
#
#         if form.is_valid():
#             return HttpResponseRedirect('/thanks/')
#
#        else:
#             form = NameForm()
#
#         return render(request, 'name.html',{'form': form})

