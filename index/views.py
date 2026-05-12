from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Post
from .models import User

# Create your views here.

def home(request):
   
    return render(request, "index/home.html", {
   
    })

def poster(request):
    form = PostForm()

    return render(request, "index/post.html", {
        'form': form
    })

def posterSubmit(request):
    
    print(request.POST)

    Post.objects.create(
        
    )



    return redirect("index/home.html")

    