from django.contrib import admin
from . import models
from .models import Post

# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('title' , 'status', 'slug' , 'author')
    
    
admin.site.register(models.Post, AuthorAdmin)
