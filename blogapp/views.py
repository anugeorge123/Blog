from django.shortcuts import render, redirect
from django.http import HttpResponse, request
from django.views.generic import View, DetailView
from blogapp.models import Realuser, Category, Ingredients, Type,Recipe, Slider,  Review,  Links, Contact, ImageSlider, About, AboutChild, GoogleMap, Rating
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
        star_dict = {}
        form = Signupform()
        login = LoginForm()
        query_img = Recipe.objects.all().order_by('-date')[:6]
        for i in query_img:
            print("\n ******* => ", i.img)

        query_background = Slider.objects.all()

        # query_captions = Slider_child.objects.all()
        query_icons = Links.objects.all()
        query_imageslider = ImageSlider.objects.all()
        query_toprated = Rating.objects.all().order_by('-average')[:5]

        for i in query_toprated:
            star_average = i.average
            star_dict[i] = range(i.average)
            print("dict-------------->", star_dict)
            # print("--------------------iiii",i,range(i.average))
        return render(request, "index.html",
                      {'id': form, 'log': login, 'product_images': query_img, 'slider_details': query_background,
                       'socialicon': query_icons, 'sliderimage': query_imageslider, 'toprated': query_toprated,
                       'starrating': star_dict})

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
        sign = {}
        form = Signupform(request.POST)
        if form.is_valid():
            try:
                print(self.request.POST)
                name = form.cleaned_data['name']
                email = form.cleaned_data['email']
                pwd = form.cleaned_data['pwd']
                cpwd = form.cleaned_data['cpwd']
                print("name----->", name, "email------>", email)


                if pwd == cpwd:
                    # timestamp = datetime.datetime.timestamp(datetime.datetime.now())
                    obj = Realuser.objects.create_user(is_superuser="0", username=name, email=email, password=pwd)
                    # token = account_activation_token._make_hash_value(obj, timestamp)
                    # obj.token = token
                    # msg = "http://127.0.0.1:8000/email/?token=" + token + "&email=" + email
                    # send_mail('Please confirm your mail id', msg, 'anugeorge.cst@gmail.com', [email], fail_silently=False)
                    obj.save()
                    sign['val'] = "Success"

                else:
                    sign['val'] = "failure"

            except Exception as e:
                print("Error:================================== ", e)
                sign['result'] = "Error"


        else:
            print("form eroors: ---------------->", form.errors)
            sign['val'] = "Error in forms"
            sign['dict1'] = form.errors
            # print("non field-----------", form.non_field_errors())
                # dict1['nonfield'] = form.non_field_errors()
        return HttpResponse(json.dumps(sign), content_type="application/json")


class Login(View):

    def post(self, request):

        log = {}
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
                    log['val'] = "success"
                    return HttpResponse(json.dumps(log), content_type="application/json")
                else:
                    log['val'] = "failed"
                    return HttpResponse(json.dumps(log), content_type="application/json")
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

        return render(request, "index.html",{'id': form, 'log': login, 'product_images': query_img, 'slider_details': query_background})


class Recipes(View):

    def get(self, request):
        rate_list =[]
        queryset = Category.objects.all()
        query_type = Type.objects.all()
        query_recipe = Recipe.objects.order_by('-id')
        query_icons = Links.objects.all()


        paginator = Paginator(query_recipe, 9)
        page = request.GET.get('page')
        recipes = paginator.get_page(page)
        print("*******************************************************", recipes)
        query_rating = Rating.objects.all()
        for i in query_rating:
            reci = i.recipe_name
            recipee = Recipe.objects.get(recipe=reci)
            print("request---",recipee.recipe)
            rate_list.append(recipee)
        print("rate list:",rate_list)
        return render(request, "recipes.html", {'cat': queryset, 'type': query_type,'recipe': recipes, 'socialicon':query_icons,'rate':query_rating})

    def post(self, request):
        try:
            category = request.POST.get('sel_category', '')
            type = request.POST['sel_type']
            recipename = request.POST['txt_recipename']
            print(type)
            queryset = Category.objects.all()
            query_type = Type.objects.all()
            query_recipe = Recipe.objects.filter(Q(category_name__category_name__icontains=category)).filter(Q(type_name__type_name__contains=type)).filter(Q(recipe__contains=recipename))
            print("======================query recipe   ", query_recipe)
            count=query_recipe.count()
            print("count=", count)
            if(query_recipe is not None):
                return render(request, "recipes.html", {'recipe': query_recipe,'cat': queryset, 'type': query_type,'count':count})
            else:
                return render(request, "recipes.html",{'error':"not found"})
        except Exception as e:
            print("error----------------------------->", e)


class Aboutus(View):
    def get(self, request):
        query_icons = Links.objects.all()
        query_about = About.objects.all()
        query_aboutas = AboutChild.objects.all()
        query_map = GoogleMap.objects.all()
        print("-------------------------------------------------------------------------------", query_map)
        return render(request, "about.html", {'socialicon': query_icons, 'about': query_about,'aboutas':query_aboutas,'map':query_map})


class ContactView(View):

    def get(self, request):
        form = Signupform()
        login = LoginForm()
        query_icons = Links.objects.all()
        return render(request, "contact.html", {'socialicon': query_icons,'id': form, 'log': login})

    def post(self, request):
        conta = {}
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
                conta["val"] = "success"
                return HttpResponse(json.dumps(conta), content_type="application/json")
        except Exception as e:
            print("error----->", e)
            conta["val"] = "failure"
            return HttpResponse(json.dumps(conta), content_type="application/json")


class RecipeSingle(DetailView):
    model = Recipe
    template_name = 'recipe_single.html'
    context_object_name = 'single_recipe'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['recipe'] = Recipe.objects.all()
        data['type'] = Type.objects.all()
        data['category'] = Category.objects.all()
        data['comments'] = Review.objects.all()
        data['count'] = Review.objects.all().count()

        return data

class Comments(View):
    # def get(self, request):
    #     query_icons = Links.objects.all()
    #     query_comments = Review.objects.all()
    #     print("commentssssssssssssssssssssssssss",query_comments)
    #     print("haiiiiiiiiiiii")
    #     return render(request, "recipe_single.html", {'socialicon': query_icons,'comments': query_comments})

    def post(self, request):
        n=0
        comm = {}
        print(self.request.POST)
        recipe_id =request.POST.get('txt_recipe', None)
        recipe_name= Recipe.objects.get(id=recipe_id)
        print("----------------------------", recipe_name)
        name = request.user
        print("name",name)
        query_email = Realuser.objects.get(username=name)
        print("query email",query_email.email)
        email =query_email.email
        # n ame = request.POST['txt_name']
        # email= request.POST['txt_email']
        subject = request.POST['txt_subject']
        message = request.POST['txt_message']
        rate = request.POST['txt_rate']


        print("rate",rate)
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>", name, email, subject, message)
        try:
            if name != "" and email != "" and subject != "" and message != "":
                query_save = Review(recipe=recipe_name, name=name, email=email, subject=subject, message=message, rate=rate)
                print("query ========================================", query_save.name, query_save.email)
                query_save.save()

                query_rate = Review.objects.filter(recipe=recipe_name)
                print("*****************************************************************", query_rate)
                query_image = Recipe.objects.get(recipe = recipe_name)
                image = query_image.img
                print("image",image)
                c=query_rate.count()
                print("count=", c)
                for i in query_rate:
                    n = n + int(i.rate)
                    if(c==1):
                        avgRate= n
                        query_rating = Rating(recipe_name=recipe_name, total=n, average=avgRate, image=image)
                        query_rating.save()
                        print("average", avgRate)
                    elif(c>1):
                        avgRate = n/c
                        print("avearge",avgRate)
                        query_rating = Rating.objects.get(recipe_name=recipe_name)
                        print("query rating", query_rating)
                        query_rating.total = n
                        query_rating.average = avgRate
                        query_rating.image = image
                        query_rating.save()
                        print("average", avgRate)
                        comm["val"] = "success"
                        return HttpResponse(json.dumps(comm), content_type="application/json")

        except Exception as e:
            comment_email = Realuser.objects.all()
            for i in comment_email:
                if email in i.email :
                     comm["val"] = "Already exist"
                else:
                    comm["val1"] = "failure"
            return HttpResponse(json.dumps(comm), content_type="application/json")



