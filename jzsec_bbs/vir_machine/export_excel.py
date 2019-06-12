import os,sys
from django.conf import settings
from .utils import *
from users.models import User
from django.db import models
from django.contrib import admin
from django.shortcuts import render
from .models import *

from django.http import HttpResponse,HttpResponseRedirect
#导出功能实现

def process_export_excel(request):
    project_codes = request.POST.get("project_code")
    project_codes = project_codes.split(',')
    #print(type(project_codes))
    print(len(project_codes))
    print(project_codes)

    #表头字段
    head_data = [u'虚拟机名称',u'虚拟机ID',u'虚拟机IP',u'系统名称',u'物理机名称']
    #查询记录数据
    records = []
    for project_code in project_codes[1:]:
        if project_code != "":
            project_obj = vir_machine.objects.get(vir_id=project_code)
            vir_name = project_obj.vir_name
            vir_id = project_obj.vir_id
            vir_ip = project_obj.vir_ip
            belong_sys = project_obj.belong_sys
            phy_name = project_obj.phy_name
            #project_test_start_date = project_obj.test_start_date
            #project_release_date = project_obj.release_date

            '''process_obj = vir_machine.objects.get(project_code=project_code)
            process_stage = process_obj.get_process_stage_display()
            process_percent = process_obj.process_percent
            process_is_percent_nomal = process_obj.get_is_percent_nomal_display()
            process_unnomal_reason = process_obj.unnomal_reason
            is_pass_smoketest = process_obj.get_is_pass_smoketest_display()
            nopass_smoketest_reason = process_obj.nopass_smoketest_reason

            daiyRecord_obj = vir_machine.objects.filter(project_code_id=project_code).values()
            daiyRecord_list = list(daiyRecord_obj)
            problem_record= daiyRecord_list[-1]['problem_record']'''

            record = []
            record.append(vir_name)
            record.append(vir_id)
            record.append(vir_ip)
            record.append(belong_sys)
            record.append(phy_name)
        records.append(record)
    print(len(records))
    n = len(records)

    #获取当前路径
    cur_path = os.path.abspath('.')
    #设置生成文件所在路径
    download_url = cur_path+'\\vir_machine\\upload\\'

    #写入数据到excel中
    ret = wite_to_excel(n,head_data,records,download_url)

    return HttpResponse(ret)

def download(request,offset):

    from django.http import StreamingHttpResponse
    def file_iterator(file_name,chunk_size=512):
        with open(file_name,'rb') as f:
            while True:
                c = f.read(chunk_size)
                if c:
                    yield c
                else:
                    break

    # 显示在弹出对话框中的默认的下载文件名
    the_file_name ='New-'+offset+'.xls'

    #获取当前路径
    cur_path = os.path.abspath('.')
    #设置生成文件所在路径
    download_url = cur_path+'\\vir_machine\\upload\\'

    response = StreamingHttpResponse(file_iterator(download_url+'New-'+offset+'.xls'))
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{0}"'.format(the_file_name)

    return response