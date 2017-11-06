# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from django.views.generic import TemplateView

def get_post(request):
    data=[]
    method = ""
    if request.method == 'GET':
        data = request.GET
        method = 'Get'
    if request.method == 'POST':
        data = request.POST
        method = 'Post'
    return render(request, 'get_post.html',
                  {'method' : method, 'data' : data})
    
