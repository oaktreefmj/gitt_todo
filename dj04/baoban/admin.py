from django.contrib import admin

# Register your models here.
from baoban import models


class orgAdmin(admin.ModelAdmin):
	list_display = ('name_org','code_org','yafan_org','memo_org',)

class minjingAdmin(admin.ModelAdmin):
	list_display = ('name_minjing','jinghao_minjing','danwei_minjing','daiban_minjing','w5c_minjing')
	fk_fields = ('name_org')

class zhibanAdmin(admin.ModelAdmin):
	list_display = ('date_zhiban','fangbao_zhiban','yeban_zhiban',)

class zfrenshuAdmin(admin.ModelAdmin):
	list_display = ('date_zfrenshu','danwei_zfrenshu','shiya_zfrenshu','jiuyi_zfrenshu','jinbi_zfrenshu','other_zfrenshu')

admin.site.register(models.org,orgAdmin)
admin.site.register(models.minjing,minjingAdmin)
admin.site.register(models.zhiban,zhibanAdmin)
admin.site.register(models.zfrenshu,zfrenshuAdmin)
