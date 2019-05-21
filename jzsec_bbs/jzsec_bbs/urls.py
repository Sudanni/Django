"""jzsec_bbs URL Configuration

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
from django.contrib import admin
from django.urls import path
from django.conf.urls import include,url
from main import views as main


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('users.urls')),
    url(r'^$', main.index),
    url(r'^accounts/profile/',main.accounts_profile),
    url(r'blog/$',main.blog),
    url(r'^blog/create/$',main.create_blog),
    url(r'^createok/$',main.create_ok),
    url(r'^blog/(?P<blog_id>\d+)$',main.blog_for_id,name="comment"),
]
