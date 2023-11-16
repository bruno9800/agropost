from django.contrib import admin
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user','created_at','updated_at','image')
    search_fields = ['user']
    

admin.site.register(Profile,ProfileAdmin)
