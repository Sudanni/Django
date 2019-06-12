from django.shortcuts import render
import json
from users.models import User
from .models import *
from .form import *


#导入分页模块
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.http import HttpResponseRedirect
from django.db import connection
# Create your views here.
#首页
def index(request):
    return render(request, 'entry_jzsec.html')

#注册
def accounts_profile(request):
    if request.method == 'POST':
        info = json.loads(request.body)
        print(info)
        info_user = User.objects.get(email=request.user.email)
        info_user.name = info['name']
        info_user.save()

        #info_job = User.objects.get(job=request.user.job)
        info_user.job = info['job']
        info_user.save()

    return render(request, 'main/accounts_profile.html')
#帖子
def blog(request):
    blog_info = Blog.objects.all().order_by('-blog_id')
    #3 blog in each page
    pagenator = Paginator(blog_info,3)
    page = request.GET.get('page')
    try:
        pages = pagenator.page(page)
    except PageNotAnInteger:
        #if page is not an integer deliver the first page
        pages = pagenator.page(1)
    except EmptyPage:
        #if page is out of range deliver last page or results
        pages = pagenator.page(pagenator.num_pages)
    return render(request,'main/blog.html',{'blogs':pages,'page':page})

#写帖子
def create_blog(request):
    blog_id = Blog.objects.all().count() + 1
    if request.method == 'GET':
        return render(request, 'main/create_blog.html',{"blog_id":blog_id})
    elif request.method == 'POST':
        #form = Blog(request.POST)
        #global blog_id
        #blog_id = 99999
        #if form.is_valid():
            #info_blog = Blog.objects.get(name=request.Blog.name)
            #info_blog.name, info_blog.blog_id ,info_blog.user_id,info_blog.user_name,info_blog.content = \
            #info['name'],info['blog_id'],info['user_id'],info['user_name'],info['content']

        name = request.POST.get('name')
        user_id = request.POST.get('user_id')
        content = request.POST.get('content')
        blog_info = Blog(name=name,blog_id=blog_id,user_name=request.user.name,user_id=user_id,content=content)
        blog_info.save()
        return HttpResponseRedirect('/createok/')

    #return render(request, 'create_blog.html')

def create_ok(request):
    return render(request,'main/createok.html')

def blog_for_id(request,blog_id):
    if request.method == 'GET':
    #cursor = connection.cursor()
    #run_sql = "select content from main_blog where blog_id = {}".format(blog_id)
    #cursor.execute(run_sql)
    #result = cursor.fetchone()
        blog_for_id = Blog.objects.get(blog_id=blog_id)

        return render(request,'main/blog_for_id.html',{"blog_for_id":blog_for_id,"blog_id":blog_id})
    if request.method == 'POST':
        form = DiscussForm(request.POST)
        if form.is_valid():
            blog = Blog.objects.get(blog_id=blog_id)
            #newcomment = request.POST.get('content')
            newcomment = form.cleaned_data['content']
            #oldcomment = Discuss.objects.get(blog_id=blog_id)
            comment_info = Discuss(to_blog_id=blog,to_user=blog.user_name,comment_user=request.user,content=newcomment)
            comment_info.save()
            redirect_url = "/blog/"+blog_id
            return HttpResponseRedirect(redirect_url,{"form":form})
        return HttpResponseRedirect("/blog/"+blog_id)
def developing(request):
     return render(request,'sys_version/developing.html')

