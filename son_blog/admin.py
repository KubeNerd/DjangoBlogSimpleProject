from django.contrib import admin
from .models import Post
# Register your models here.
admin.site.register(Post)


admin.site.site_header = 'Administrator'
admin.site.site_title = 'Administração TodoApp - Black Panters Blog'
