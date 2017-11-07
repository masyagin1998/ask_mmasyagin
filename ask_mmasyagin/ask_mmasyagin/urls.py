"""ask_mmasyagin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from ask_mmasyagin import views

urlpatterns = [
    ######################################################
    ######################## Base ########################
    ######################################################

    # 1) Settings.
    url(r'^settings', views.settings_view, name='settings'),
    # 2) Logout.
    url(r'^logout/', views.logout_view, name='logout'),
    # 3) Login. 
    url(r'^login', views.login_view, name='login'),
    # 4) Signup.
    url(r'^signup', views.signup_view, name='signup'),

    ######################################################
    ####################### Index ########################
    ######################################################

    # 1) Index.
    url(r'^$', views.index_view, name='index'),

    ######################################################
    ######################## Hot #########################
    ######################################################

    # 1) Hot.
    url(r'^hot/', views.index_view, name='hot'),

    ######################################################
    ######################## Tag #########################
    ######################################################

    # 1) Tag.
    url(r'^tag/metal/', views.tag_view, name='tag'),
    
    ######################################################
    ##################### Question #######################
    ######################################################

    # 1) Question.
    url(r'^question/', views.question_view, name='question'),

    ######################################################
    ######################## Ask #########################
    ######################################################

    # 1) Ask.    
    url(r'^ask', views.ask_view, name='ask'),

    url(r'^admin/', admin.site.urls),
]
