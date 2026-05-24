from django.urls import path
from index import views
app_name = 'index'
urlpatterns = [
    path('', views.home, name='home'),
    path('post', views.poster, name='post'),
    path('post_list', views.post_list, name='post_list'),
    path('post/submit', views.posterSubmit , name='posterSubmit'),
    path('maketopic', views.topic_post, name='topic_post'),
    path('maketopic/submit', views.topic_post_make, name='topic_post_make'),
    path('makeuser', views.makeuser, name='makeuser'),
    path('login/', views.login_view, name="login")

]