from django.contrib import admin
from .models import Post,Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ('title','published_at','updated_at','product','author')
    search_fields = ['title','content','product','author']

admin.site.register(Post,PostAdmin)
admin.site.register(Comment)
