from django.db import models

# Create your models here.

yes_no = ((u'1',u'是'),(u'0',u'否'),)

class org(models.Model):
	name_org = models.CharField(max_length=32,verbose_name='单位')
	code_org = models.CharField(max_length=2,verbose_name='单位代码')
	yafan_org = models.CharField(max_length=1,choices=yes_no,verbose_name='是否押犯')
	memo_org = models.TextField(blank=True,verbose_name='备注')
	yw_org = models.CharField(max_length=2,choices=yes_no,verbose_name='是否运维')
#	def __unicode__(self):
#		return self.name_org
	def __str__(self):
		return self.name_org


class minjing(models.Model):
	name_minjing = models.CharField(max_length=12,verbose_name='民警姓名')
	jinghao_minjing = models.CharField(max_length=8,verbose_name='警号')
	danwei_minjing = models.ForeignKey(org,verbose_name='单位')
	lingdao_minjing = models.CharField(max_length=1,choices=yes_no,verbose_name='是否狱长')
	daiban_minjing = models.CharField(max_length=1,choices=yes_no,verbose_name='是否代班')
	w5c_minjing = models.CharField(max_length=1,choices=yes_no,verbose_name='五查值班')
	def __str__(self):
		return self.name_minjing


class area(models.Model):
	name_area = models.CharField(max_length=128,verbose_name='区域名称')
	code_area = models.CharField(max_length=4,verbose_name='区域代码')
	yafan_area = models.CharField(max_length=1,choices=yes_no,verbose_name='是否押犯')


class gzzl(models.Model):
	name_gzzl = models.CharField(max_length=128,verbose_name='故障分类')
	code_gzzl = models.CharField(max_length=4,verbose_name='故障代码')
	status_gzzl = models.CharField(max_length=4,verbose_name='鼓掌状态')


class result(models.Model):
	name_result = models.CharField(max_length=128,verbose_name='处理结果')
	code_result = models.CharField(max_length=4,verbose_name='处理代码')
	status_result = models.CharField(max_length=4,verbose_name='处理状态')
