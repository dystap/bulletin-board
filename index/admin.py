from django.contrib import admin
from index.models import UserProfile, Topic, Post, Comments
# Register your models here.

admin.site.register(UserProfile)
admin.site.register(Topic)
admin.site.register(Post)
admin.site.register(Comments)
