from django.contrib import admin
from .models import Realuser

admin.site.register(Realuser, admin.ModelAdmin)
