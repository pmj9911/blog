"""BlogApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, re_path 
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
app_name = "ArticlesApp"	
# re_path is a variable which works with regular expressions
urlpatterns = [
    path('',views.article_list, name="list"),
    path('create/', views.article_create, name="create"),
    path('articlesApi', views.ArticlesList.as_view()),
    path('delete/<int:pk>/', views.article_delete, name ="delete" ),
    re_path('update/(?P<slug>[\w-]+)/', views.article_update, name ="update" ),
    re_path('detail/(?P<slug>[\w-]+)/',views.article_detail, name="detail"),
]

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'html'])