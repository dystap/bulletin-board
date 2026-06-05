from django.db import models
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

import datetime
# Create your models here.


def uploaded_pfp(instance: "UserProfile", filename):
    filename_mime_type = filename[filename.rfind("."):]
    return f"User/{instance.id}/{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}{filename_mime_type}"

def uploaded_image(instance: "Post", filename):
    filename_mime_type = filename[filename.rfind("."):]
    return f"Post/{instance.id}/{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}{filename_mime_type}"

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, related_name="user_profile")
    birthday = models.DateField(blank=True, null=True)
    hobby = models.CharField(max_length=67, blank=True, null=True)
    quote = models.TextField(blank=True, null=True)
    pfp = models.FileField(
        upload_to=uploaded_pfp,
        validators=[FileExtensionValidator(['jpeg','png','jpg','webp', 'gif'])],
        blank=True, null=True
    )
    join_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        ordering = ['-join_date']

    def __str__(self):
        return f"{self.user}'s Profile"

class Topic(models.Model):
    topic = models.CharField(max_length=30)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,  related_name="topicsmade")

    def __str__(self):
        return self.topic
    

class Post(models.Model):
    post = models.CharField(max_length=30)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="postsmadeuser")
    description = models.CharField()
    image = models.FileField(
        blank=True,
        null=True,
        upload_to=uploaded_image,
        validators= [FileExtensionValidator(['jpeg','png','jpg','webp','gif'])]
    )
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True, related_name="postmadetopic")    
    post_date = models.DateTimeField()

    class Meta: 
        ordering = ['-post_date']
    
    def __str__(self):
        return f'Post by {self.user}'

class Comments(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL, null=True, related_name="usermadecomment")
    post = models.ForeignKey(Post, on_delete=models.SET_NULL, null=True, related_name="postmadecomment")
    comment = models.CharField(max_length =200)
    created_at = models.DateTimeField(auto_now_add=True)
    
    parent = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='replies'
    )
    class Meta: 
        ordering = ['-created_at']

    def __str__(self):
        return f'Comment by {self.user}'
    
