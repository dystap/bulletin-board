from django.contrib import admin
from index.models import User, Topic, Post, Comments
# Register your models here.

admin.site.register(User)
admin.site.register(Topic)
admin.site.register(Post)
admin.site.register(Comments)
