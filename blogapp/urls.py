from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^login/$', views.Login.as_view(), name="login"),
    url(r'^email/$',views.Home.linkmail, name="email"),
    url(r'^recipes/$', views.Recipes.as_view(), name="recipe"),
    url(r'^about/$', views.Aboutus.as_view(), name="about"),
    url(r'^contact/$', views.ContactView.as_view(), name="contact"),
    url(r'^logout/$', views.Login.logout_view, name="logout"),
    url(r'^recipe_single/(?P<pk>\d+)$', views.RecipeSingle.as_view(), name="recipe_single"),
    url(r'^comment/', views.Comments.as_view(), name="comments"),
    # url(r'^recipes/', views.TotalSearch.as_view(), name="search"),


    url(r'^$', views.Home.as_view(), name="home"),
]