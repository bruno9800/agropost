from django.contrib import admin
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('created_at','user','image')
    search_fields = ['user']

admin.site.register(Profile,ProfileAdmin)
