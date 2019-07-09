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
from vir_machine import views as vir
from vir_machine import view_machine_room as machine_room
from vir_machine import export_excel
from sys_app import views as sys_ver


urlpatterns = [
    url(r'developing/',main.developing,name="developing"),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('users.urls')),
    url(r'^$', main.index),
    url(r'^accounts/profile/',main.accounts_profile),
    url(r'blog/$',main.blog),
    url(r'^blog/create/$',main.create_blog),
    url(r'^createok/$',main.create_ok),
    url(r'^blog/(?P<blog_id>\d+)$',main.blog_for_id,name="comment"),
    url(r'^vir_list/$',vir.get_vir_machine,name="vir_list"),
    url(r'machine_room.html$', machine_room.get_machine_room, name="machine_room"),
    url(r'vir_list/query/?',vir.query_by_field,name="query_vir_list"),
    url(r'vir_list/process_export_excel/$',export_excel.process_export_excel),
    url(r'vir_list/download/(\w+)*/$',export_excel.download),
    url(r'^sys_display/$',sys_ver.sys_display),
    url(r'^ver_repostory/$',sys_ver.get_ver_repostory,name="get_ver_repostory"),
    url(r'ver_repostory/query/?',sys_ver.query_rep,name="query_repostory_list"),
    url(r'^ver_repostory/add/$',sys_ver.add_sys,name="add_sys"),
    url(r'^ver_repostory/edit/(?P<ver_rep_id>\d+)$',sys_ver.edit_sys,name="edit_sys"),
    url(r'^ver_repostory/delete/',sys_ver.del_sys,name="del_sys"),
    url(r'^ser_version/$', sys_ver.get_ser_version, name="get_ser_version"),
    url(r'^ser_version/query/?', sys_ver.query_ser, name="query_server_list"),
    url(r'^ser_version/add/$', sys_ver.add_ser, name="add_ser"),
    url(r'^ser_version/edit/(?P<ser_ver_id>\d+)$', sys_ver.edit_ser, name="edit_ser"),
    url(r'^ser_version/delete/', sys_ver.del_ser, name="del_ser"),
    url(r'^ver_monitor/$',sys_ver.ver_monitor,name="ver_monitor"),
    url(r'ver_monitor/query_rep/?',sys_ver.query_ver_monitor,name="query_ver_monitor"),
    url(r'^ope_director/$', sys_ver.get_ope_director, name="get_ope_director"),
    url(r'^ope_director/query/?', sys_ver.query_director, name="query_director_list"),
    url(r'^ope_director/add/$', sys_ver.add_director, name="add_director"),
    url(r'^ope_director/edit/(?P<sys_name>(\w+)*)/$', sys_ver.edit_director, name="edit_director"),
    url(r'^ope_director/delete/', sys_ver.del_director, name="del_director"),
    #url(r'vir_list/machine_room.html',machine_room.query_by_field,name="query_vir_list"),
]
