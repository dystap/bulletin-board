from django.shortcuts import render, redirect, get_object_or_404
from datetime import datetime
from .forms import PostForm
from .forms import TopicForm
from .forms import UserForm
from .forms import UserProfileForm
from .forms import CommentForm
from django.contrib.auth import login, logout, authenticate
from .models import Post
from .models import Topic
from .models import Comments
from .models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required


def home(request):
   
    return render(request, "index/home.html", {
       
    })

def post_list(request):
    posts = Post.objects.all().order_by('post_date').select_related('user', 'user__user_profile',)

    selected_topic = request.GET.get('topic')
    if selected_topic:
        posts = posts.filter(topic_id=selected_topic)

    all_topics = Topic.objects.all()
    context = { 
        "posts" : posts,
        "all_topics" : all_topics,
        "selected_topic": selected_topic
    }
    return render(request, 'index/post_list.html', context)


def thepost(request, id):
    post_queryset = Post.objects.select_related('user__user_profile')
    ThePost = get_object_or_404(post_queryset, id=id)
    comments = ThePost.postmadecomment.filter(parent__isnull=True).select_related('user__user_profile')
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = ThePost
            new_comment.user = request.user
            parent_id = request.POST.get('parent_id')
            if parent_id:
                parent_comment = get_object_or_404(Comments, id=parent_id)
                new_comment.parent = parent_comment

            new_comment.save()
            return redirect('index:thepost', id=ThePost.id)
    else:
        form = CommentForm()

    context = {'ThePost': ThePost,
               'comments': comments,
               'form': form
               }
    return render(request, 'index/thepost.html', context)

@login_required
def poster(request):
    form = PostForm()

    return render(request, "index/post.html", {
        'form': form
    })

def profile(request, id):
    TheProfile = get_object_or_404(UserProfile, id=id)
    context = {'TheProfile': TheProfile}
    return render(request, 'index/profile.html', context)


@login_required
def posterSubmit(request):
    
    if request.method == 'POST':
            form = PostForm(request.POST, request.FILES)
            if form.is_valid():
                form.save(user=request.user, post_date=datetime.now()) 
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
    if request.user.is_authenticated: 
        return redirect('index:home')
     
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(join_date=datetime.now())

            birthday = form.cleaned_data.get('birthday')

            TheProfile, created = UserProfile.objects.get_or_create(
            user=user,
            defaults={
                'birthday': birthday,
                'join_date': user.date_joined
            }
    )
            if not created:
                TheProfile.birthday = birthday
                TheProfile.join_date = user.date_joined
                TheProfile.save()

            return redirect('index:login')
    else:
        form = UserForm()

    return render(request, "index/user.html", {
        'form' : form
    })

@login_required
def edit_profile(request):
    TheProfile, created = UserProfile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=TheProfile)
        if form.is_valid:
            form.save()
            return redirect('index:home')
    else:
        form = UserProfileForm(instance=TheProfile)
        return render(request, 'index/editprofile.html', {'form': form})

def login_view(request):
    if request.user.is_authenticated: 
        return redirect('index:home')

    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect("index:home")
    else:
        form = AuthenticationForm()
    return render(request, "index/login.html", {"form": form})

@login_required
def logout_view(request):
    if request.method == 'POST':
        logout(request)
    return redirect("index:home")