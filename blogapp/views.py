from django.shortcuts import render, redirect
from django.http import HttpResponse, request
from django.views.generic import View, DetailView
from blogapp.models import Realuser, Category, Ingredients, Type,Recipe, Slider,  Review,  Links, Contact, ImageSlider
from django.contrib.auth import login, authenticate, logout
# from django.contrib.auth.models import Realuser
from django.contrib.auth.hashers import check_password
from .forms import Signupform, LoginForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView

from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from .tokens import account_activation_token
import datetime
import json
from django.db.models import Q
from django.core.paginator import Paginator


class Home(View):

    def get(self, request):
        form = Signupform()
        login = LoginForm()
        query_img = Recipe.objects.all().order_by('-date')[:6]
        for i in query_img:
            print("\n ******* => ", i.img)

        query_background = Slider.objects.all()
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>.",query_background)
        # query_captions = Slider_child.objects.all()
        query_icons = Links.objects.all()
        query_imageslider = ImageSlider.objects.all()
        print("=========================================================================================",query_imageslider)
        return render(request, "index.html", {'id': form, 'log': login, 'product_images': query_img,'slider_details': query_background, 'socialicon': query_icons,'sliderimage':query_imageslider})

    def linkmail(request):
        token = request.GET['token']
        mail = request.GET['email']
        ob = Realuser.objects.get(email=mail)
        if ob.token == token:
            ob.is_active = True
            ob.save()
            return redirect("/")
        else:
            return HttpResponse("Invalid Token")
        # return HttpResponse("token="+token+" email="+mail)

    def post(self, request):
        dict1 = {}
        form = Signupform(request.POST)
        if form.is_valid():
            try:
                print(self.request.POST)
                name = form.cleaned_data['name']
                # address = form.cleaned_data['address']
                email = form.cleaned_data['email']
                pwd = form.cleaned_data['pwd']
                cpwd = form.cleaned_data['cpwd']
                print("name----->", name, "email------>", email)

                if pwd == cpwd:
                    timestamp = datetime.datetime.timestamp(datetime.datetime.now())
                    obj = Realuser.objects.create_user(is_superuser="0", username=name, email=email, password=pwd)
                    token = account_activation_token._make_hash_value(obj, timestamp)
                    obj.token = token
                    msg = "http://127.0.0.1:8000/email/?token=" + token + "&email=" + email
                    send_mail('Please confirm your mail id', msg, 'anugeorge.cst@gmail.com', [email], fail_silently=False)
                    obj.save()
                    dict1['val'] = "Success"

                else:
                    dict1['val'] = "failure"

            except Exception as e:
                print("Error:================================== ", e)
                dict1['result'] = "Error"


        else:
            print("form eroors: ---------------->", form.errors)
            dict1['val'] = "Error in forms"
            dict1['dict1'] = form.errors
            # print("non field-----------", form.non_field_errors())
                # dict1['nonfield'] = form.non_field_errors()
        return HttpResponse(json.dumps(dict1), content_type="application/json")


class Login(View):

    def post(self, request):

        dict2 = {}
        login1 = LoginForm(request.POST)
        if login1.is_valid():
            uname = login1.cleaned_data['uname']
            pwd = login1.cleaned_data['pwd']
            print("uname: ", uname, "password: ", pwd)

            try:

                obj = Realuser.objects.get(username=uname)
                auth1 = authenticate(request, username=uname, password=pwd)
                print(auth1)
                if auth1:
                    login(request, auth1, backend='django.contrib.auth.backends.ModelBackend')
                    dict2['val'] = "success"
                    return HttpResponse(json.dumps(dict2), content_type="application/json")
                else:
                    dict2['val'] = "failed"
                    return HttpResponse(json.dumps(dict2), content_type="application/json")
            except Exception as e:
                print(e)

    def logout_view(request):
        logout(request)
        form = Signupform()
        login = LoginForm()
        query_img = Recipe.objects.all().order_by('-id')[:6]
        for i in query_img:
            print("\n ******* => ", i.img)

        query_background = Slider.objects.all()
        query_captions = Slider_child.objects.all()
        return render(request, "index.html",{'id': form, 'log': login, 'product_images': query_img, 'slider_details': query_background, 'slider_captions': query_captions})


class Recipes(View):

    def get(self, request):
        # print("get view")
        queryset = Category.objects.all()
        query_type = Type.objects.all()
        query_recipe = Recipe.objects.order_by('-id')
        query_icons = Links.objects.all()


        paginator = Paginator(query_recipe, 6)
        page = request.GET.get('page')
        recipes = paginator.get_page(page)
        print("*******************************************************", recipes)
        return render(request, "recipes.html", {'cat': queryset, 'type': query_type,'recipe': recipes, 'socialicon':query_icons})

    def post(self, request):
        try:
            category = request.POST.get('sel_category', '')
            type = request.POST['sel_type']
            recipename = request.POST['txt_recipename']
            print(type)
            query_recipe = Recipe.objects.filter(Q(category_name__category_name__icontains=category)).filter(Q(type_name__type_name__contains=type))
            print("======================", query_recipe)

            if(query_recipe is not None):
                return render(request, "recipes.html", {'recipe': query_recipe})
            else:
                HttpResponse("Not found!!")
        except Exception as e:
            print("error----------------------------->", e)


class About(View):
    def get(self, request):
        query_icons = Links.objects.all()
        return render(request, "about.html", {'socialicon':query_icons})


class ContactView(View):

    def get(self, request):
        query_icons = Links.objects.all()
        return render(request, "contact.html", {'socialicon': query_icons})

    def post(self, request):
        dict4 = {}
        name = request.POST['txt_name'] if request.POST['txt_name'] else None
        email = request.POST['txt_email'] if request.POST['txt_email'] else None
        subject = request.POST['txt_subject'] if request.POST['txt_subject'] else None
        message = request.POST['txt_message'] if request.POST['txt_message'] else None
        try:
            if name and email and subject and message:
                print("name:", name, "email:", email, "subject", subject, "message:", message)
                query_contact = Contact.objects.create(contact_name = name, contact_email = email, contact_subject = subject, contact_message = message)
                print(query_contact)
                # query_contact.save()
                dict4["val"] = "success"
            else:
                dict4["val"] = "failure"
                dict4["errors"] = "This Field is required"
            return HttpResponse(json.dumps(dict4), content_type="application/json")
        except Exception as e:
            print("error----->", e)
            return HttpResponse("success")


class RecipeSingle(DetailView):
    model = Recipe
    template_name = 'recipe_single.html'
    context_object_name = 'single_recipe'


class Comments(View):
    def get(self, request):
        query_icons = Links.objects.all()
        return render(request, "recipe_single.html", {'socialicon': query_icons})

    def post(self, request):
        dict3 = {}
        print(self.request.POST)
        recipe_id =request.POST.get('txt_recipe', None)
        recipe_name= Recipe.objects.get(id=recipe_id)
        print("----------------------------", recipe_name)
        name = request.POST['txt_name']
        email= request.POST['txt_email']
        subject = request.POST['txt_subject']
        message = request.POST['txt_message']
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>", name, email, subject, message)
        try:
            if name != "" and email != "" and subject != "" and message != "":
                query_save = Review(recipe=recipe_name, name=name, email=email, subject=subject, message=message)
                print("query ========================================", query_save.name, query_save.email)
                query_save.save()
                dict3["val"] = "success"
            else:
                dict3["val"] = "failure"
                dict3["errors"] = "This Field is required"
            return HttpResponse(json.dumps(dict3), content_type="application/json")

        except Exception as e:
            print("error-----",e)
        # return render(request, "index.html")


