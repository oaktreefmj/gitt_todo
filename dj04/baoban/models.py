#coding:utf-8

from django.db import models

# Create your models here.


yes_no = ((u'1',u'是'),(u'0',u'否'),)

class org(models.Model):
	name_org = models.CharField(max_length=32,verbose_name='单位')
	code_org = models.CharField(max_length=2,verbose_name='单位代码')
	yafan_org = models.CharField(max_length=1,choices=yes_no,verbose_name='是否押犯')
	memo_org = models.TextField(blank=True,verbose_name='备注')
	def __unicode__(self):
		return self.name_org


class minjing(models.Model):
	name_minjing = models.CharField(max_length=12,verbose_name='民警姓名')
	jinghao_minjing = models.CharField(max_length=8,verbose_name='警号')
	danwei_minjing = models.ForeignKey(org,verbose_name='单位')
	lingdao_minjing = models.CharField(max_length=1,choices=yes_no,verbose_name='是否狱长')
	daiban_minjing = models.CharField(max_length=1,choices=yes_no,verbose_name='是否代班')
	w5c_minjing = models.CharField(max_length=1,choices=yes_no,verbose_name='五查值班')
	def __unicode__(self):
		return self.name_minjing


class zhiban(models.Model):
	
	date_zhiban = models.DateField(auto_now_add=True,verbose_name='日期')
	name_zhiban =models.ManyToManyField(minjing,verbose_name='值班民警')
	fangbao_zhiban = models.CharField(max_length=1,choices=yes_no,verbose_name='防爆队员')
	yeban_zhiban = models.CharField(max_length=1,choices=yes_no,verbose_name='夜班')
	def __unicode__(self):
		return str(self.date_zhiban)

class zfrenshu(models.Model):
	date_zfrenshu = models.DateField(auto_now_add=True,verbose_name='日期')
	danwei_zfrenshu = models.ForeignKey(org,verbose_name='单位')
	shiya_zfrenshu = models.IntegerField(verbose_name='实押')
	jiuyi_zfrenshu = models.IntegerField(verbose_name='外出就医')
	jinbi_zfrenshu = models.IntegerField(verbose_name='禁闭')
	other_zfrenshu = models.IntegerField(verbose_name='其他')
	def __unicode__(self):
		return str(self.shiya_zfrenshu)

