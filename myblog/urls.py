#-*- coding:utf-8 -*-
from django.conf.urls import url
from . import views

app_name = 'myblog'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^detail/$', views.detail, name='detail'),
]