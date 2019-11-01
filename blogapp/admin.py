from django.contrib import admin
from .models import Realuser, Category, Type, Ingredients, Recipe, Review, Slider, Slider_child, Links, Contact


class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    search_fields = ['recipe']
    list_display = ('recipe','category_name', 'type_name')


class CategoryAdmin(admin.ModelAdmin):
    model = Category
    fields = ['category_name']

#
# class RealuserAdmin(admin.ModelAdmin):
#     model = Realuser
#     fields = ['username', 'address', 'email']

class RealuserAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['username']}),
        ('Email', {'fields':['email']}),
        ('Address', {'fields': ['address']}),
        ('Date information', {'fields': ['date_joined']})
    ]
class ReviewAdmin(admin.ModelAdmin):
    model = Review
    fields = ['name','email','subject','message','recipe']


# class Contact(admin.ModelAdmin):
#     model = Contact
#     list_display = ('contact_name', 'contact_email', 'contact_subject','contact_message')

admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Realuser, RealuserAdmin)

admin.site.register(Type, admin.ModelAdmin)
admin.site.register(Ingredients, admin.ModelAdmin)
# admin.site.register(Recipe, admin.ModelAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Slider, admin.ModelAdmin)
admin.site.register(Slider_child, admin.ModelAdmin)
admin.site.register(Links, admin.ModelAdmin)
admin.site.register(Contact, admin.ModelAdmin)