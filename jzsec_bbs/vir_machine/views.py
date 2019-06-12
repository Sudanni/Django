from django.shortcuts import render
from .models import *
#导入分页模块
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.http import HttpResponseRedirect
import sys
sys.path.append('E:\Django\jzsec_bbs')
# Create your views here.


def get_vir_machine(request,*page_count,page_flag=True):
    vir_machine_list = vir_machine.objects.all()
    vir_machine_count = vir_machine.objects.all().count()
    page_count = 50
    pagenator = Paginator(vir_machine_list, page_count)
    page = request.GET.get('page')
    try:
        pages = pagenator.page(page)
    except PageNotAnInteger:
        #if page is not an integer deliver the first page
        pages = pagenator.page(1)
    except EmptyPage:
        #if page is out of range deliver last page or results
        pages = pagenator.page(pagenator.num_pages)
    return render(request,'vir_machine/vir_machine.html',{'vir_machine_list':pages,'page':page,'page_count':page_count,'vir_machine_count':vir_machine_count,'page_flag':page_flag})

def query_by_field(request,vip_ip="",phy_name="",page_flag=False):
    if request.method == 'GET':
        vir_ip = request.GET.get("vir_ip")
        phy_name = request.GET.get("phy_name")
        '''if vir_ip in ["","虚拟机IP"] and phy_name in ["","物理机名称"]:
            return HttpResponseRedirect("/vir_list/")
        elif vir_ip in ["","虚拟机IP"]:
            print(11111111111111111)
            vir_machine_list = vir_machine.objects.filter(phy_name=phy_name)
            vir_machine_count = vir_machine_list.count()
        elif phy_name in ["","物理机名称"]:
            vir_machine_list = vir_machine.objects.filter(vir_ip=vir_ip)
            vir_machine_count = vir_machine_list.count()
        else:
            vir_machine_list = vir_machine.objects.filter(phy_name=phy_name,vir_ip=vir_ip)
            vir_machine_count = vir_machine_list.count()
            '''
        if vir_ip == "" and phy_name == "":
            return HttpResponseRedirect("/vir_list/")
        elif vir_ip == "" and phy_name != "":
            vir_machine_list = vir_machine.objects.filter(phy_name=phy_name)
            vir_machine_count = vir_machine_list.count()
        elif vir_ip != "" and phy_name == "":
            vir_machine_list = vir_machine.objects.filter(vir_ip=vir_ip)
            vir_machine_count = vir_machine_list.count()
        else:
            vir_machine_list = vir_machine.objects.filter(phy_name=phy_name, vir_ip=vir_ip)
            vir_machine_count = vir_machine_list.count()


        page_count = 50
        pagenator = Paginator(vir_machine_list, page_count)
        page = request.GET.get('page')
        try:
            pages = pagenator.page(page)
        except PageNotAnInteger:
            # if page is not an integer deliver the first page
            pages = pagenator.page(1)
        except EmptyPage:
            # if page is out of range deliver last page or results
            pages = pagenator.page(pagenator.num_pages)
        return render(request, 'vir_machine/vir_machine.html', {'vir_machine_list': vir_machine_list,'page': page, 'page_count': page_count,'vir_machine_count': vir_machine_count,'vir_ip':vir_ip,'phy_name':phy_name,'page_flag':page_flag})
    else:
        return HttpResponseRedirect("/vir_list/")







