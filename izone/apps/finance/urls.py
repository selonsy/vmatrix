# -*- coding: utf-8 -*-
from django.conf.urls import url
from .views import HtmlTest, JsonTest

urlpatterns = [
    url(r'^test1', JsonTest, name='test'),
    url(r'^test2', HtmlTest, name='test'),
]
