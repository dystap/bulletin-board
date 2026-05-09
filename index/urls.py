from django.urls import path
from index import views
app_name = 'index'
urlpatterns = [
    path('', views.home, name='home'),
    path('post', views.poster, name='post')
    
]