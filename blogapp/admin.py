from django.contrib import admin
from .models import Realuser, Category, Type, Ingredients, Recipe, Review, Slider, Links, Contact, ImageSlider, About, AboutChild, GoogleMap, Rating, Newsletter

from django.conf import settings


from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage



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

                'all': ('css/location_picker.css', ),
            }
            js = (
                'https://maps.googleapis.com/maps/api/js?key={}'.format(settings.GOOGLE_MAPS_API_KEY),
                'js/location_picker.js',
            )


class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    search_fields = ['recipe']
    list_display = ('recipe', 'category_name', 'type_name')


class CategoryAdmin(admin.ModelAdmin):
    model = Category
    fields = ['category_name']


class RealuserAdmin(admin.ModelAdmin):
     list_display = ('username', 'email')

class ReviewAdmin(admin.ModelAdmin):
    model = Review
    fields = ['name', 'email', 'subject', 'message', 'recipe', 'rate']


class SliderAdmin(admin.ModelAdmin):
    model = Slider
    search_display  = ['slider_caption1', 'slider_caption2', 'slider_caption3']

    list_editable = ('slider_caption1', 'slider_caption2', 'slider_caption3')
    list_display = ('slider_image', 'slider_caption1', 'slider_caption2', 'slider_caption3')



# class FlatPageAdmin(FlatPageAdmin):
#     fieldsets = (
#         (None, {'fields': ('url', 'title', 'content', 'sites')}),
#         (_('Advanced options'), {
#             'classes': ('collapse',),
#             'fields': (
#                 'enable_comments',
#                 'registration_required',
#                 'template_name',
#             ),
#         }),
#     )

class AboutChild(admin.TabularInline):
   model = AboutChild


class AboutAdmin(admin.ModelAdmin):
   fields = ('about_caption', 'about_content','about_image','about_text')
   inlines = [AboutChild]


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Realuser, RealuserAdmin)
admin.site.register(Type, admin.ModelAdmin)
admin.site.register(Ingredients, admin.ModelAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Slider, SliderAdmin)
admin.site.register(Links, admin.ModelAdmin)
admin.site.register(Contact, admin.ModelAdmin)
admin.site.register(ImageSlider, admin.ModelAdmin)
# admin.site.register(About, admin.ModelAdmin)
admin.site.register(About, AboutAdmin)
# admin.site.register(GoogleMap, admin.ModelAdmin)
admin.site.register(Rating, admin.ModelAdmin)
admin.site.register(Newsletter, admin.ModelAdmin)