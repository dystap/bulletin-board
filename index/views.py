from django.shortcuts import render


# Create your views here.

def home(request):
   
    return render(request, "index/home.html", {
   
    })

def poster(request):
    return render(request, "index/post.html", {

    })
