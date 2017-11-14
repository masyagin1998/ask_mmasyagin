"""questions URL Configuration

The 'urlpatterns' list routes URLs to views.
"""

from django.conf.urls import url

from questions import views

# Urls.

urlpatterns = [
    # Base.
    url(r'^login', views.login_view, name='login'),
    url(r'^signup', views.signup_view, name='signup'),
    url(r'^settings', views.settings_view, name='settings'),
    url(r'^logout', views.logout_view, name='logout'),
    # Index.
    url(r'^$', views.index_view, name='index'),
    # Hot.
    url(r'^hot', views.hot_view, name='hot'),
    # Question.
    url(r'^question/(\d+)', views.question_view, name='question'),
    # Tags.
    url(r'^tag/(.+)', views.tag_view, name='tag'),
    # Ask.
    url(r'^ask', views.ask_view, name='ask'),
    # Notification.
    # For Ajax.
]
