#! /usr/bin/python
# -*- coding:utf-8 -*-

from django.conf.urls import url
from restful import views

urlpatterns = [
    url(r'^v1/rest/$', views.rest_list),
    url(r'^v1/rest/(?P<pk>[0-9]+)/$', views.rest_detail),
]