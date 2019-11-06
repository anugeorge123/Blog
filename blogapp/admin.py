from django.contrib import admin
from .models import Realuser, Category, Type, Ingredients, Recipe, Review, Slider, Links, Contact, ImageSlider, About, AboutChild, GoogleMap, Rating

from django.conf import settings
from django.contrib import admin


@admin.register(GoogleMap)
class VenueAdmin(admin.ModelAdmin):
    list_display = ('name', 'latitude', 'longitude',)
    search_fields = ('name',)

    fieldsets = (
        (None, {
            'fields': ('name', 'latitude', 'longitude',)
        }),
    )

    class Media:
        if hasattr(settings, 'GOOGLE_MAPS_API_KEY') and settings.GOOGLE_MAPS_API_KEY:
            css = {
                'all': ('css/location_picker.css',),
            }
            js = (
                'https://maps.googleapis.com/maps/api/js?key={}'.format(settings.GOOGLE_MAPS_API_KEY),
                'js/location_picker.js',
            )


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
        ('Date information', {'fields': ['date_joined']})
    ]
class ReviewAdmin(admin.ModelAdmin):
    model = Review
    fields = ['name','email','subject','message','recipe','rate']





admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Realuser, RealuserAdmin)

admin.site.register(Type, admin.ModelAdmin)
admin.site.register(Ingredients, admin.ModelAdmin)
# admin.site.register(Recipe, admin.ModelAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Slider, admin.ModelAdmin)
# admin.site.register(Slider_child, admin.ModelAdmin)
admin.site.register(Links, admin.ModelAdmin)
admin.site.register(Contact, admin.ModelAdmin)
admin.site.register(ImageSlider, admin.ModelAdmin)
admin.site.register(About, admin.ModelAdmin)
admin.site.register(AboutChild, admin.ModelAdmin)
# admin.site.register(GoogleMap, admin.ModelAdmin)
admin.site.register(Rating, admin.ModelAdmin)