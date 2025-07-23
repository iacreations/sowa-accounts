from django.urls import path
from . import views
appname='sowaAuth'
urlpatterns = [
    path('login', views.login_user, name='login'),
    path('register', views.register_user, name='register'),
]
