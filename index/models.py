from django.db import models
from django.core.validators import FileExtensionValidator
import datetime
# Create your models here.


def uploaded_pfp(instance: "User", filename):
    filename_mime_type = filename[filename.rfind("."):]
    return f"User/{instance.id}/{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}{filename_mime_type}"


class User(models.Model):
    email = models.EmailField()
    username = models.CharField(max_length=67)
    birthday = models.DateField()
    hobby = models.CharField(max_length=67)
    quote = models.TextField(blank=True, null=True)
    pfp = models.FileField(
        upload_to=uploaded_pfp,
        validators=[FileExtensionValidator(allowed_extentions=['jpeg','png','jpg','webp'])],
        blank=True, null=True
    )

class Topic(models.Model):
    title = models.CharField(max_length=30)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, NULL=True, related_name="topicsmade")
    

class Post(models.Model):
    title = models.CharField()
    user = models.ForeignKey(User, on_delete=models.SET_NULL, NULL=True, related_name="topicsmade")
    desciption = 

