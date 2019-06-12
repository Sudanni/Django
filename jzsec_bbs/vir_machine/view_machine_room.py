from django.shortcuts import render
from .models import *
#导入分页模块
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.http import HttpResponseRedirect
from django.template.loader import render_to_string
import os

def get_machine_room(request):
    context = {'some_key': 'some_value'}

    static_html = 'machine_room.html'

    #if not os.path.exists(static_html):
    #    content = render_to_string('template.html', context)
    #    with open(static_html, 'w') as static_file:
    #       static_file.write(content)

    return render(request, static_html)