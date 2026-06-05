from django.urls import path, include
from index import views
from django.conf import settings
from django.conf.urls.static import static
app_name = 'index'
urlpatterns = [
    path('', views.home, name='home'),
    path('post', views.poster, name='post'),
    path('post_list', views.post_list, name='post_list'),
    path('post/submit', views.posterSubmit , name='posterSubmit'),
    path('maketopic', views.topic_post, name='topic_post'),
    path('maketopic/submit', views.topic_post_make, name='topic_post_make'),
    path('makeuser', views.makeuser, name='makeuser'),
    path('login', views.login_view, name="login"),
    path('logout', views.logout_view, name="logout"),
    path('users/<int:id>', views.profile, name="profile"),
    path('editprofile', views.edit_profile, name="editprofile"),
    path('post_list/<int:id>', views.thepost, name="thepost"),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)