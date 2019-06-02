# -*- coding: utf-8 -*-
from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^test1', JsonTest, name='test'),
    url(r'^test2', HtmlTest, name='test'),
    url(r'^index', Index, name='test'),
    url(r'^detail', Detail, name='test'),
    url(r'^getlist', GetList, name='test'),
    url(r'^getdetailbyname', GetDetailByName, name='test'),
    url(r'^add', Add, name='test'),    
    url(r'^getlocations', GetLocations, name='test'),        
]
