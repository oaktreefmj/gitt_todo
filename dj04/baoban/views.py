#coding:utf-8
from django.shortcuts import render
from baoban.models import *
from django.utils import timezone
from datetime import date,datetime
from baoban.forms import *
# Create your views here. 
# 

def index(request):
	jianqus = org.objects.all()
#	minjings = minjing.objects.all()
#	zhibans = zhiban.objects.all()
	username=request.session['username']
	zb = timezone.now()
	y = zb.strftime('%Y')
	m = zb.strftime('%m')
	d = zb.strftime('%d')
	zfrenshus = zfrenshu.objects.filter(date_zfrenshu__year=y,
										date_zfrenshu__month=m,
										date_zfrenshu__day=d)
	
	zhibans = zhiban.objects.filter(date_zhiban__year=y,
									date_zhiban__month=m,
									date_zhiban__day=d)
	scro1 = 0
	scro2 = 0
	scro3 = 0
	for i in zfrenshus:
		scro1 = scro1 + int(i.shiya_zfrenshu)
		scro2 = scro2 + int(i.jinbi_zfrenshu)
		scro3 = scro3 + int(i.other_zfrenshu)
	
	w5c = zhibans.filter(name_zhiban__lingdao_minjing="1")
	for i in w5c:
		for a in i.name_zhiban.all():
			lingdao = a.name_minjing

	w5c1 = zhibans.filter(name_zhiban__w5c_minjing="1")
	lingdao1 = ''
	for i in w5c1:
		for a in i.name_zhiban.all():
			lingdao1 =lingdao1 + "   " + a.name_minjing

	zhibans1 = zhibans.exclude(name_zhiban__w5c_minjing='1').order_by('name_zhiban__danwei_minjing__code_org')
				
	
	obj1 = ['jianqu','shiya','jiuyi','oth','mj']
	obj = []
	for dw in [2,3,4,5,6,7,8,9,10,11,12,13,14]:
		a1 = jianqus.get(code_org=dw)
		zf = zfrenshus.filter(danwei_zfrenshu__code_org=dw)
		if zf.exists():
			for i in zf.all():
				a2=i.shiya_zfrenshu
				a3=i.jiuyi_zfrenshu
				a4=i.other_zfrenshu
				a5=''
		else:
			a2='--'
			a3='--'
			a4='--'
			a5=''
		zb1 = zhibans.filter(name_zhiban__danwei_minjing__code_org=dw)
	
		if zb1.exists():
			i = zb1.all()[0]
			for ii in i.name_zhiban.all():
				a5 = a5 + " " + ii.name_minjing
		else:
			a5 = '--'

			
		obj2=[a1,a2,a3,a4,a5]
		obj3 = dict(zip(obj1,obj2))
		obj.append(obj3)
			
				

	return render(request, 'index.html',locals())


def list(request):
	zhibanf=zhiban.objects.all()
	list1=[]
	dict1={}
	
	for a in zhibanf:
		date1=a.date_zhiban
		b=a.name_zhiban.all()
		ld1=""
		db1=""
		mj1=""
		for item in b:
			
			if item.lingdao_minjing==1:
				ld1=item.name_minjing
			elif item.daiban_minjing==1:
				db1=item.name_minjing
			else:
				mj1=mj1+item.name_minjing
		dict1=dict(zip())	
		
		list1.append(dict1)	
		


				




	return render(request, 'list.html',locals())

def add(request):
	username=request.session['username']
	print(username)
	if request.method =="POST":
		zhibanf = zhiban_form(request.POST)
		zfrenshuf = zfrenshu_form(request.POST)
		if zhibanf.is_valid() and zfrenshuf.is_valid():

			zhibanf.save()
			zfrenshuf.save()


	else:
		zhibanf=zhiban_form()
		zfrenshuf = zfrenshu_form()

	return render(request, 'report.html',locals())

def test(request):
	date=datetime.now()
	form=zhiban_form()
	mj=minjing.objects.filter(lingdao_minjing='1').order_by('jinghao_minjing')

	return render(request, 'test.html',locals())