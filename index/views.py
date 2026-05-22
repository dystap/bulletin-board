from django.shortcuts import render, redirect
from .forms import PostForm
from django.contrib.auth import login
from .models import Post
from .models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

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
            return redirect("index:home")
    else:
        form = UserCreationForm()

    return render(request, "index/user.html", {
        'form' : form
    })

def login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect("index:home")
    else:
        form = AuthenticationForm()
    return render(request, "index/login.html", {"form": form})