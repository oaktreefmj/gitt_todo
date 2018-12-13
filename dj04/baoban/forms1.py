#coding:utf-8
#

from django import forms
from django.forms import ModelForm
from baoban.models import *
from django.forms import fields
from django.forms import widgets


class zhiban_form(ModelForm):
	'''def __init__(self,*args,**kwargs):
		super(zhiban_form,self).__init__(*args,**kwargs)
		self.fields['name_zhiban'].widget.choices=name_zhiban.objects.filter().values_list('id','name_minjing')
	'''
#	name_zhiban = forms.CharField(widget=forms.SelectMultiple())
	class Meta:
		model = zhiban
		exclude = ['date_zhiban']
		widgets = {'name_zhiban':widgets.CheckboxSelectMultiple(attrs={'rows':10})}




class zfrenshu_form(ModelForm):
	class Meta:
		model = zfrenshu
		exclude = ['date_zfrenshu']

class minjing_form(ModelForm):
	'''def __init__(self,*args,**kwargs):
		for key in kwargs:
			super(minjing_form,self).__init__(*args,**kwargs)
		
			self.fields['danwei_minjing'].widget.choices=org.objects.filter(code_org=kwargs[key]).values_list('id','name_org')
'''
	class Meta:
		model = minjing
		exclude = ['id']