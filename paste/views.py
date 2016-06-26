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
from django.shortcuts import get_object_or_404

class PasteCreateView(CreateView):
    model = Paste
    fields = ['title', 'content', 'visibility']
    template_name = "paste/form.html"
    success_url = reverse_lazy('main_page')


class UserToolsFormView(UpdateView):
    model = Paste
    fields = ['title', 'content', 'visibility']
    template_name = "paste/form.html"
    success_url = reverse_lazy('main_page')


class PasteDeleteView(DeleteView):

    model = Paste
    template_name = "paste/confirm_delete.html"

    def get_success_url(self):
        return reverse_lazy('paste_list')


class PasteShowView(View):
    template_name = "paste/show.html"

    def get(self, request, paste_id):
        paste = get_object_or_404(Paste, pk=paste_id)

        return render(request, self.template_name, {
            'paste': paste,
        })


class PasteListView(View):
    template_name = "paste/list.html"

    def get(self, request):
        return render(request, self.template_name, {
            'all_paste': Paste.objects.all()
        })