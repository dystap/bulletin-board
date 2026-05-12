from django.shortcuts import render, redirect
from .forms import PostForm

# Create your views here.

def home(request):
   
    return render(request, "index/home.html", {
   
    })

def poster(request):
    return render(request, "index/post.html", {

    })

def posterSubmit(request):
    
    form = PostForm()

    return redirect("index/home.html")

    