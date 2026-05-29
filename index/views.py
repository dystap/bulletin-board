from django.shortcuts import render, redirect
from .forms import PostForm
from .forms import TopicForm
from django.contrib.auth import login
from .models import Post
from .models import Topic
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Create your views here.

def home(request):
   
    return render(request, "index/home.html", {
   
    })

def post_list(request):
    posts = Post.objects.all().order_by('post_date')
    return render(request, 'index/post_list.html', {"posts" : posts})

def poster(request):
    form = PostForm()

    return render(request, "index/post.html", {
        'form': form
    })

def posterSubmit(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()

    return redirect("index:home")


def topic_post(request):
    form = TopicForm()

    return render(request, "index/topics.html", {
        'form': form
    })

def topic_post_make(request):
    print(request.POST)

    Topic.objects.create(
        topic = request.POST.get("topic"),
        user = request.POST.get("user"),
    )

    return redirect("index:home")

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

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect("index:home")
    else:
        form = AuthenticationForm()
    return render(request, "index/login.html", {"form": form})