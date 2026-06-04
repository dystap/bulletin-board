from django.shortcuts import render, redirect
from .forms import PostForm
from .forms import TopicForm
from .forms import UserForm
from django.contrib.auth import login
from .models import Post
from .models import Topic
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required

# Create your views here.

# @login_required
def home(request):
    # username = None
    # if request.user.is_authenticated:
    #     username = request.user.username
    return render(request, "index/home.html", {
        # 'user' : username
    })

def post_list(request):
    posts = Post.objects.all().order_by('post_date')
    return render(request, 'index/post_list.html', {"posts" : posts})

@login_required
def poster(request):
    form = PostForm()

    return render(request, "index/post.html", {
        'form': form
    })

@login_required
def posterSubmit(request):
    
    if request.method == 'POST':
            form = PostForm(request.POST, request.FILES)
            if form.is_valid():
                form.save(user=request.user) 
                return redirect('index:home')
            else:
                print("form_errors:", form.errors)
    else:
        form = PostForm()
            
    return render(request, 'post.html', {'form': form})
        

@login_required
def topic_post(request):
    form = TopicForm()

    return render(request, "index/topics.html", {
        'form': form
    })

@login_required
def topic_post_make(request):
    if request.method == 'POST':
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save(user=request.user)
            return redirect('index:home')
        else:
            print("form_errors:", form.errors)
    else:
        form = TopicForm()
    return render(request, "index/topics.html", {
        'form' : form
    })

   

def makeuser(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index:login')
    else:
        form = UserForm()
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