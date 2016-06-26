# -*- coding: utf-8 -*-
from django import forms
from .models import Paste


class UserToolsForm(forms.ModelForm):

    class Meta:
        model = Paste
        fields = ['title', 'content', 'visibility']