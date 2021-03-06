"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
   path('admin/', admin.site.urls),
    path('', views.about),
    path('readBlogs/', views.Blogs),
    path('signIn/', views.signIn),
    path('logout/', views.logout, name="log"),
    path('signUp/', views.signUp, name="signup"),
    path('profile/', views.profile, name="profile"),
    path('postsignIn/', views.postsignIn),
    path('postsignup/', views.postsignup),
    path('search/', views.search),
    path('searchnotes/', views.searchnotes),
    path('searchusers/', views.searchusers),
    path('about/', views.about),
    path('addPost/', views.addPost, name="addPost"),
    path('afterAddPost/', views.afteraAddPost),
    path('gotoedit/', views.gotoedit, name="edit"),
    path('postedit/', views.postedit, name="pedit"),
    path('reset/', views.reset),
    path('postReset/',views.postReset),
]
