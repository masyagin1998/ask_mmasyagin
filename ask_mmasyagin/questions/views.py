# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# Views.

# Base.
def login_view(request):
    # Title.
    result = {'title' : 'Login'}
    # Get Top Tags from DB.
    result['top_tags'] = top_tags
    # Get Top Users from DB.
    result['top_users'] = top_users
    # User.
    result['user'] = user
    # Input.
    result['login_is_valid'] = ''
    result['password_is_valid'] = 'is-invalid'
    
    # Return render.
    return render(request, 'login.html', result)

def signup_view(request):
    # Title.
    result = {'title' : 'SignUp'}
    # Get Top Tags from DB.
    result['top_tags'] = top_tags
    # Get Top Users from DB.
    result['top_users'] = top_users
    # User.
    result['user'] = user
    # Input.
    result['login_is_valid'] = ''
    result['email_is_valid'] = ''
    result['nick_is_valid'] = ''
    result['password1_is_valid'] = 'is-invalid'
    result['password2_is_valid'] = 'is-invalid'

    # Return render.
    return render(request, 'signup.html', result)

def settings_view(request):
    # Title.
    result = {'title' : 'Settings'}
    # Get Top Tags from DB.
    result['top_tags'] = top_tags
    # Get Top Users from DB.
    result['top_users'] = top_users
    # User.
    result['user'] = user
    # Input.
    result['login_is_valid'] = ''
    result['email_is_valid'] = ''
    result['nick_is_valid'] = ''
    result['password1_is_valid'] = ''
    result['password2_is_valid'] = ''
    result['password3_is_valid'] = 'is-invalid'
    
    # Return render.
    return render(request, 'settings.html', result)

def logout_view(request):
    return redirect('/')

# Index.
def index_view(request):
    # Title.
    result = {'title' : 'MetalForum', }
    # Get Top Tags from DB.
    result['top_tags'] = top_tags
    # Get Top Users from DB.
    result['top_users'] = top_users
    # Get User from DB.
    result['user'] = user
    
    # Return Pagination
    return pagination(request, 'index.html', question_previews, 4, result)

# Hot.
def hot_view(request):
    # Title.
    result = {'title' : 'Hot', }
    # Get Top Tags from DB.
    result['top_tags'] = top_tags
    # Get Top Users from DB.
    result['top_users'] = top_users
    # Get User from DB.
    result['user'] = user
    
    # Return Pagination
    return pagination(request, 'hot.html', question_previews, 4, result)

# Question.
def question_view(request, question_id):
    # Title.
    result = {'title' : 'Question', }
    # Get Top Tags from DB.
    result['top_tags'] = top_tags
    # Get Top Users from DB.
    result['top_users'] = top_users
    # Get User from DB.
    result['user'] = user
    # Get Question from DB.
    result['question'] = question
    # Get Answers from DB.
    result['answers'] = answers

    # Return render.
    return render(request, 'question.html', result)

# Tag.
def tag_view(request, question_tag):
    # Title.
    result = {'title' : 'Tag', }
    # Get Top Tags from DB.
    result['top_tags'] = top_tags
    # Get Top Users from DB.
    result['top_users'] = top_users
    # Get User from DB.
    result['user'] = user
    # Get Tag from DB.
    result['tag'] = question_tag

    # Return Pagination
    return pagination(request, 'tag.html', question_previews, 4, result)

# Ask.
def ask_view(request):
    # Title.
    result = {'title' : 'New Question', }
    # Get Top Tags from DB.
    result['top_tags'] = top_tags
    # Get Top Users from DB.
    result['top_users'] = top_users
    # Get User from DB.
    result['user'] = user

    # Return render.
    return render(request, 'ask.html', result)

# Pagination.
def pagination(request, html_page, objects, objects_count, result):
    # Paginator.
    paginator = Paginator(objects, objects_count)
    page = request.GET.get('page')

    # Error Handling.
    try:
        objects = paginator.page(page)
    except PageNotAnInteger:
        objects = paginator.page(1)
    except EmptyPage:
        objects = paginator.page(paginator.num_pages)

    # Get Question Previews from DB.
    result['question_previews'] = objects
    result['pagination_list'] = objects
        
    return render(request, html_page, result)

# Testing
user = {
    'is_logged_in' : True,
    'id' : '00001',
    'login' : 'ozzy_osbourne_1948', 'email' : 'ozzy@osbourne.ru',
    'nick' : 'Ozzy Osbourne', 'avatar' : 'avatars/00005.png',
}

top_tags = {
    'tag01' : 'Metal', 'tag02' : 'Rock', 'tag03' : 'ManowaR', 'tag04' : 'MotorHead', 'tag05' : 'Doro',
    'tag06' : 'Whitesnake', 'tag07' : 'Accept', 'tag08' : 'DIO', 'tag09' : 'Aerosmith', 'tag10' : 'Death',
    'tag11' : 'In_Flames', 'tag12' : 'M', 'tag13' : 'Russkaja', 'tag14' : 'Molotov', 'tag15' : 'Eisbrecher',
    'tag16' : 'Paddyhats', 'tag17' : 'Rumjacks', 'tag18' : 'In_Extremo', 'tag19' : 'MtH', 'tag20' : 'Deep_Purple',
}

top_users = {
    'nick01' : 'Lemmy Killmister', 'nick02' : 'Marilyn Manson', 'nick03' : 'Andreas Bergh',
    'nick04' : 'Freddy Mercury', 'nick05' : 'Sergey Troitsky', 'nick06' : 'Liv Jagrell',
    'nick07' : 'Yui Itsuki', 'nick08' : 'Rob Halford', 'nick09' : 'Valery Kipelov',
    'nick10' : 'Erick Backman',
}

question_preview = {
    'id' : 1024,
    'avatar' : 'avatars/00004.png',
    'number_of_likes' : 15,
    'number_of_dislikes' : 6,
    'title' : 'The fastest guitarist in the world.',
    'text' : 'Hey, bro\'s! I know that the fastest guitar player in Russia is V. Zinchuck. Also I know about Michael Anhelo Batio, Buckethead and Marty Friedman. But wh',
    'number_of_answers' : 3,
    'tag1' : 'Metal',
    'tag2' : 'Metal',
    'tag3' : 'Metal',
}

question_previews = []
for _ in range(99):
    question_previews.append(question_preview)

question = {
    'id' : 1024,
    'avatar' : 'avatars/00004.png',
    'number_of_likes' : '15',
    'number_of_dislikes' : '6',
    'title' : 'The fastest guitarist in the world.',
    'text' : 'Hey, bro\'s! I know that the fastest guitar player in Russia is V. Zinchuck. Also I know about Michael Anhelo Batio, Buckethead and Marty Friedman. But who is the fastest?!!! It\'s really interesting for me!',
    'tag1' : 'Metal',
    'tag2' : 'Metal',
    'tag3' : 'Metal',
}

answer = {
    'avatar' : 'avatars/00003.png',
    'number_of_likes' : '6',
    'number_of_dislikes' : '3',
    'text' : 'Hello, my friend! The fastest guitar player in the world is (yeah, You name him) Viktor Zinchuck! He is realy fast!',
}

answers = [answer, answer, ]
