# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render_to_response, redirect, render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import get_object_or_404
from django.contrib import auth
from django.views.generic import TemplateView

######################################################
######################## Base ########################
######################################################

# 1) Settings.
def settings_view(request):
    return render(request, 'settings.html',  {'is_logged_in' : True})

# 2) Logout.
def logout_view(request):
    return render(request, 'index.html', {'is_logged_in' : False})

# 3) Login.
def login_view(request):
    return render(request, 'login.html',  {'is_logged_in' : False})

# 4) Signup.
def signup_view(request):
    return render(request, 'signup.html',  {'is_logged_in' : False})

######################################################
####################### Index ########################
######################################################

# 1) Index.
def index_view(request):
    question_previews = []
    for _ in range(0, 5):
        question_previews.append({
            'title' : 'Who is the fastest guitar player in the Worlds?',
            'preview' : 'I know that the fastest guitarits in Russia is Zinchuck. Also I know about Mikhael Angelo B...',
            'likes' : '8',
            'dislikes' : '1',
            'number_of_answers' : '6',
            'tag1' : '#Metal',
            'tag2' : '#Metal',
            'tag3' : '#Metal',
        })
    if True:
        return render(request, 'index.html', {'is_logged_in' : True, 'question_previewes' : tuple(question_previews), })
    else:
        return render(request, 'index.html', {'is_logged_in' : False, 'question_previews' : tuple(question_previews), })

######################################################
######################## Tag #########################
######################################################

# 1) Tag.
def tag_view(request):
    return render(request,'tag.html')

######################################################
##################### Answers ########################
######################################################

# 1) Answers.
def question_view(request):
    question = {
        'title' : 'Who is the fastest guitar player in the Worlds?',
        'text' : 'I know that the fastest guitarits in Russia is Zinchuck. Also I know about Mikhael Angelo Bation, Buckethead and Marty Friedman. But who is the fastest?!!!',
        'likes' : '8',
        'dislikes' : '1',
        'tag1' : '#Metal',
        'tag2' : '#Metal',
        'tag3' : '#Metal',
    }
    answers = []
    for _ in range(0, 5):
        answers.append({
            'title' : 'Who is the fastest guitar player in the Worlds?',
            'preview' : 'I know that the fastest guitarits in Russia is Zinchuck. Also I know about Mikhael Angelo B...',
            'likes' : '8',
            'dislikes' : '1',
            'number_of_answers' : '6',
            'tag1' : '#Metal',
            'tag2' : '#Metal',
            'tag3' : '#Metal',
        })
    return render(request, 'question.html', {'question' : question, 'answers' : tuple(answers)})

######################################################
######################## Ask #########################
######################################################

# 1) Ask.
def ask_view_render(request):
    return render(request, 'ask.html')

def ask_view(request):
    return ask_view_render(request)
