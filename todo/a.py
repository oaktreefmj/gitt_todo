from django.shortcuts import render_to_response,render,get_object_or_404 
from django.http import HttpResponse, HttpResponseRedirect 
from django.contrib.auth.models import User 
from django.contrib import auth
from django.contrib import messages
from django.template.context import RequestContext 

from django.forms.formsets import formset_factory
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from bootstrap_toolkit.widgets import BootstrapUneditableInput
from django.contrib.auth.decorators import login_required



from django import forms
 
class AddForm(forms.Form):
    a = forms.IntegerField()
    b = forms.IntegerField()

from django.forms import ModelForm
from models import Store, Address, Depot

 
class StoreForm(ModelForm): 
 class Meta: 
 model = Store 
 fields = '__all__'
 
class AddressForm(ModelForm): 
 class Meta: 
 model = Address 
 exclude = ['s_name'] 
 
class DepotForm(ModelForm): 
 class Meta: 
 model = Depot 
 exclude = ['s_name']