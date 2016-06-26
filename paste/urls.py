# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from . import views
from .views import PasteCreateView, PasteListView
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^add/$', PasteCreateView.as_view(), name='add_paste'),
    url(r'^list/$', PasteListView.as_view(), name='paste_list'),
]