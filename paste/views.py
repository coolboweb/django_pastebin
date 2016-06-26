# -*- coding: utf-8 -*-
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.models import User
from .models import Paste
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
# Create your views here.


class PasteCreateView(CreateView):
    model = Paste
    fields = ['title', 'content', 'visibility']
    template_name = "paste/form.html"
    success_url = reverse_lazy('main_page')


class PasteListView(View):
    template_name = "paste/list.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {
            'all_paste': Paste.objects.all()
        })