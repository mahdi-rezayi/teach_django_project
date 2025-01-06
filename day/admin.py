from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'content')
    list_filter = ('author','title')
    search_fields = ('title', 'content')