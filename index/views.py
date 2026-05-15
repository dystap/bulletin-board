from django.shortcuts import render, redirect
from .forms import PostForm
from .forms import UserForm
from .models import Post
from .models import UserProfile
from django.contrib.auth.forms import UserCreationForm

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

def makeuser(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("post:list")
    else:
        form = UserCreationForm()

    return render(request, "index/user.html", {
        'form' : form
    })

