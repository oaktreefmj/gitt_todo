#coding:utf-8
#

from django import forms
from django.forms import ModelForm
from baoban.models import *
from django.forms import fields
from django.forms import widgets


class zhiban_form(forms.Form):
	date=forms.DateField()
	name=forms.ModelMultipleChoiceField(queryset=minjing.objects.filter(lingdao_minjing='1'))
