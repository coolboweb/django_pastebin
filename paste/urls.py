# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from . import views
from .views import PasteCreateView, PasteListView, PasteShowView, PasteDeleteView
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^add/$', PasteCreateView.as_view(), name='add_paste'),
    url(r'^list/$', PasteListView.as_view(), name='paste_list'),
    url(r'^(?P<paste_id>\d+)/$', PasteShowView.as_view(), name='show_paste'),
    url(r'^d/(?P<pk>\d+)/$', PasteDeleteView.as_view(), name='delete_paste'),
]