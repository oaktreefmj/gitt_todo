#coding:utf-8
 
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dj04.settings")
 
import django

django.setup()
 
 
def main():
    from baoban.models import org,minjing
    obj=org.objects.get(id=9)
    f = open('data.txt')
    for line in f:
        name_minjing,jinghao_minjing,lingdao_minjing,daiban_minjing,w5c_minjing = line.split(',')
        minjing.objects.create(name_minjing=name_minjing,jinghao_minjing=jinghao_minjing,
        					lingdao_minjing=lingdao_minjing,daiban_minjing=daiban_minjing,
        					w5c_minjing=w5c_minjing,danwei_minjing=obj)
    f.close()
 
if __name__ == "__main__":
    main()
    print('Done!')