from django.shortcuts import render
import json
from users.models import User
from .models import *
from .form import *
from django.db import connection
#导入分页模块
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.http import HttpResponseRedirect,HttpResponse
# Create your views here.
#def create_repostory(request):
#主页
def sys_display(request):
    cursor = connection.cursor()
    sql = "select a.sys_name,a.ope_director,a.ser_ip,a.process_name,a.version as sys_version,a.md5,b.version as rep_version,b.md5 from ser_version a  \
           left join ver_repostory b on a.sys_name=b.sys_name and a.mod_name = b.mod_name;"
    cursor.execute(sql)
    ver_monitor_list = cursor.fetchall()
    ver_monitor_count = ser_version.objects.all().count()
    test1_md5 = 1
    test2_md5 = 1
    if test1_md5 == test2_md5:
        status = "正常"
    else:
        status = "异常"
    return render(request,'sys_version/ver_info.html',{"status":status,"ver_monitor_list":ver_monitor_list})


#版本库页面
def get_ver_repostory(request,*page_count,page_flag=True):
    ver_repostory_list = ver_repostory.objects.all()
    ver_repostory_count = ver_repostory.objects.all().count()
    page_count = 10
    pagenator = Paginator(ver_repostory_list, page_count)
    page = request.GET.get('page')
    try:
        pages = pagenator.page(page)
    except PageNotAnInteger:
        #if page is not an integer deliver the first page
        pages = pagenator.page(1)
    except EmptyPage:
        #if page is out of range deliver last page or results
        pages = pagenator.page(pagenator.num_pages)
    return render(request,'sys_version/ver_repostory.html',{'ver_repostory_list':pages,'page':page,'page_count':page_count,'ver_repostory_count':ver_repostory_count,'page_flag':page_flag})

def query_rep(request,sys_name="",page_flag=False):
    if request.method == 'GET':
        sys_name = request.GET.get("sys_name")
        if sys_name == "":
            return HttpResponseRedirect("/ver_repostory/")
        else:
            ver_repostory_list = ver_repostory.objects.filter(sys_name=sys_name)
            ver_repostory_count = ver_repostory_list.count()


        page_count = 10
        pagenator = Paginator(ver_repostory_list, page_count)
        page = request.GET.get('page')
        try:
            pages = pagenator.page(page)
        except PageNotAnInteger:
            # if page is not an integer deliver the first page
            pages = pagenator.page(1)
        except EmptyPage:
            # if page is out of range deliver last page or results
            pages = pagenator.page(pagenator.num_pages)
        return render(request, 'sys_version/ver_repostory.html', {'ver_repostory_list': ver_repostory_list,'page': page, 'page_count': page_count,'ver_repostory_count': ver_repostory_count,'vir_ip':sys_name,'page_flag':page_flag})
    else:
        return HttpResponseRedirect("/ver_repostory/")

def add_sys(request):
    if request.method == 'GET':
        form = VerRepostoryForm()
        return render(request, 'sys_version/add_sysversion.html',{"form":form})
    elif request.method == 'POST':
        form = VerRepostoryForm(request.POST)
        backpath = request.path.split('/')[1]
        if form.is_valid():
            '''sys_name = form('sys_name')
            #sys_name = request.POST.get("sys_name")
            mod_name = form.cleaned_data('mod_name')
            process_name = form.cleaned_data('process_name')
            version = form.cleaned_data('version')
            process_path = form.cleaned_data('process_path')
            md5 = form.cleaned_data('md5')
            remark = form.cleaned_data('remark')
            repostory = ver_repostory(sys_name=sys_name,mod_name=mod_name,process_name=process_name,version=version,process_path=process_path, \
                    md5=md5,remark=remark)'''
            form.save()
            return render(request,"sys_version/createok.html",{"backpath":backpath})
        else:
            return HttpResponse('信息不全')

def edit_sys(request,ver_rep_id):
    if request.method == "GET":
        ver_rep = ver_repostory.objects.get(id=ver_rep_id)
        form = VerRepostoryForm(instance=ver_rep)

        #return HttpResponse('信息不全')
        return render(request, 'sys_version/edit_sysversion.html', {"form": form,"ver_rep_id":ver_rep_id})
    elif request.method == "POST":
        backpath = request.path.split('/')[1]
        print(backpath)
        form = VerRepostoryForm(request.POST)
        try:
            form.is_valid()
            '''sys_name = form('sys_name')
            #sys_name = request.POST.get("sys_name")
            mod_name = form.cleaned_data('mod_name')
            process_name = form.cleaned_data('process_name')
            version = form.cleaned_data('version')
            process_path = form.cleaned_data('process_path')
            md5 = form.cleaned_data('md5')
            remark = form.cleaned_data('remark')
            repostory = ver_repostory(sys_name=sys_name,mod_name=mod_name,process_name=process_name,version=version,process_path=process_path, \
                    md5=md5,remark=remark)'''
            ver_repostory.objects.filter(id=ver_rep_id).update(**form.cleaned_data)
            return render(request, "sys_version/editok.html",{"backpath":backpath})
        except Exception as e:
            print(e)
            return HttpResponse('信息不全')
        #else:
        #   return HttpResponse('信息不全')
    else:
        return HttpResponseRedirect('/ver_repostory/')

def del_sys(request):
    if request.method == "POST":
        id = request.POST.get('id')
        print("id = %s" % id)
        status = "删除成功！"
        result = "Error!"
        deletesql = ver_repostory.objects.filter(id=id)  # 执行删除操作
        if deletesql.delete():
            return HttpResponse(json.dumps({
                "status": status
            }))
        else:
            return HttpResponse(json.dumps({
                "result": result
            }))
    else:
        return HttpResponse("系统错误")



#系统版本页面
def get_ser_version(request,*page_count,page_flag=True):
    ser_version_list = ser_version.objects.all()
    ser_version_count = ser_version.objects.all().count()
    page_count = 10
    pagenator = Paginator(ser_version_list, page_count)
    page = request.GET.get('page')
    try:
        pages = pagenator.page(page)
    except PageNotAnInteger:
        #if page is not an integer deliver the first page
        pages = pagenator.page(1)
    except EmptyPage:
        #if page is out of range deliver last page or results
        pages = pagenator.page(pagenator.num_pages)
    return render(request,'sys_version/ser_version.html',{'ser_version_list':pages,'page':page,'page_count':page_count,'ser_version_count':ser_version_count,'page_flag':page_flag})

def query_ser(request,sys_name="",page_flag=False):
    if request.method == 'GET':
        sys_name = request.GET.get("sys_name")
        if sys_name == "":
            return HttpResponseRedirect("/ser_version/")
        else:
            ser_version_list = ser_version.objects.filter(sys_name=sys_name)
            ser_version_count = ser_version_list.count()


        page_count = 10
        pagenator = Paginator(ser_version_list, page_count)
        page = request.GET.get('page')
        try:
            pages = pagenator.page(page)
        except PageNotAnInteger:
            # if page is not an integer deliver the first page
            pages = pagenator.page(1)
        except EmptyPage:
            # if page is out of range deliver last page or results
            pages = pagenator.page(pagenator.num_pages)
        return render(request, 'sys_version/ser_version.html', {'ser_version_list': ser_version_list,'page': page, 'page_count': page_count,'ser_version_count': ser_version_count,'vir_ip':sys_name,'page_flag':page_flag})
    else:
        return HttpResponseRedirect("/ser_version/")

def add_ser(request):
    if request.method == 'GET':
        form = SerVersionForm()
        return render(request, 'sys_version/add_serversion.html',{"form":form})
    elif request.method == 'POST':
        form = SerVersionForm(request.POST)
        backpath = request.path.split('/')[1]
        if form.is_valid():
            '''sys_name = form('sys_name')
            #sys_name = request.POST.get("sys_name")
            mod_name = form.cleaned_data('mod_name')
            process_name = form.cleaned_data('process_name')
            version = form.cleaned_data('version')
            process_path = form.cleaned_data('process_path')
            md5 = form.cleaned_data('md5')
            remark = form.cleaned_data('remark')
            repostory = ver_repostory(sys_name=sys_name,mod_name=mod_name,process_name=process_name,version=version,process_path=process_path, \
                    md5=md5,remark=remark)'''
            form.save()
            return render(request,"sys_version/createok.html",{"backpath":backpath})
        else:
            return HttpResponse('信息不全')

def edit_ser(request,ser_ver_id):
    if request.method == "GET":
        print(ser_ver_id)
        ser_ver = ser_version.objects.get(id=ser_ver_id)
        form = SerVersionForm(instance=ser_ver)

        #print(backpath)
        #return HttpResponse('信息不全')
        return render(request, 'sys_version/edit_serversion.html', {"form": form,"ser_ver_id":ser_ver_id})
    elif request.method == "POST":
        form = SerVersionForm(request.POST)
        backpath = request.path.split('/')[1]
        try:
            form.is_valid()
            '''sys_name = form('sys_name')
            #sys_name = request.POST.get("sys_name")
            mod_name = form.cleaned_data('mod_name')
            process_name = form.cleaned_data('process_name')
            version = form.cleaned_data('version')
            process_path = form.cleaned_data('process_path')
            md5 = form.cleaned_data('md5')
            remark = form.cleaned_data('remark')
            repostory = ver_repostory(sys_name=sys_name,mod_name=mod_name,process_name=process_name,version=version,process_path=process_path, \
                    md5=md5,remark=remark)'''
            ser_version.objects.filter(id=ser_ver_id).update(**form.cleaned_data)

            return render(request, "sys_version/editok.html",{"backpath":backpath})
        except Exception as e:
            print(e)
            return HttpResponse('信息不全')
    else:
        return HttpResponseRedirect('/ser_version/')

def del_ser(request):
    if request.method == "POST":
        id = request.POST.get('id')
        print("id = %s" % id)
        status = "删除成功！"
        result = "Error!"
        deletesql = ser_version.objects.filter(id=id)  # 执行删除操作
        if deletesql.delete():
            return HttpResponse(json.dumps({
                "status": status
            }))
        else:
            return HttpResponse(json.dumps({
                "result": result
            }))
    else:
        return HttpResponse("系统错误")


def ver_monitor(request,page_flag=True):
    cursor = connection.cursor()
    sql = "select a.sys_name,a.ope_director,a.ser_ip,a.process_name,a.version as sys_version,a.md5,b.version as rep_version,b.md5 from ser_version a  \
           left join ver_repostory b on a.sys_name=b.sys_name and a.mod_name = b.mod_name;"
    cursor.execute(sql)
    ver_monitor_list = cursor.fetchall()
    ver_monitor_count = ser_version.objects.all().count()

    cursor.close()
    page_count = 10
    pagenator = Paginator(ver_monitor_list, page_count)
    page = request.GET.get('page')
    try:
        pages = pagenator.page(page)
    except PageNotAnInteger:
        #if page is not an integer deliver the first page
        pages = pagenator.page(1)
    except EmptyPage:
        #if page is out of range deliver last page or results
        pages = pagenator.page(pagenator.num_pages)
    print(locals())
    return render(request,'sys_version/ver_monitor.html',{'ver_monitor_list':pages,'page':page,'page_count':page_count,'ver_monitor_count':ver_monitor_count,'page_flag':page_flag})



def query_ver_monitor(request,page_flag=False,sys_name=""):
    if request.method == "GET":
        sys_name = request.GET.get("sys_name")
        if sys_name == "":
            return HttpResponseRedirect("/ver_monitor/")
        else:
            cursor = connection.cursor()
            sql = "select a.sys_name,a.ope_director,a.ser_ip,a.process_name,a.version as sys_version,a.md5,b.version as rep_version,b.md5 from ser_version a  \
           left join ver_repostory b on a.sys_name=b.sys_name and a.mod_name = b.mod_name where a.sys_name=" + "\"" +sys_name+ "\""
            print(sql)
            cursor.execute(sql)
            ver_monitor_list = cursor.fetchall()
            ver_monitor_count = ser_version.objects.all().count()
            cursor.close()
        page_count = 10
        pagenator = Paginator(ver_monitor_list, page_count)
        page = request.GET.get('page')
        try:
            pages = pagenator.page(page)
        except PageNotAnInteger:
        #if page is not an integer deliver the first page
            pages = pagenator.page(1)
        except EmptyPage:
        #if page is out of range deliver last page or results
            pages = pagenator.page(pagenator.num_pages)
        return render(request,'sys_version/ver_monitor.html',{'ver_monitor_list':pages,'page':page,'page_count':page_count,'ver_monitor_count':ver_monitor_count,'page_flag':page_flag,'sys_name':sys_name})
    else:
        return HttpResponseRedirect("/ver_monitor/")