from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title','published_at','updated_at','product','author')
    search_fields = ['title','content','product','author']

admin.site.register(Post,PostAdmin)