from django.contrib import admin

# Register your models here.
from .models import Post
# user id= admin, pw=123_PassWort
admin.site.register(Post)
