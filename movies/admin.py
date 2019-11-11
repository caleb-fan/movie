from django.contrib import admin
from movies import models
import urllib.request,re,os,time,random,pymysql
from bs4 import BeautifulSoup
# Register your models here.
#添加下面的代码就可以进行管理
# admin.site.register(models.User)

#将模型中的内容具体显示
@admin.register(models.User)
class MoviesAdmin(admin.ModelAdmin):
    #以列表的形式显示
    list_display = ['u_id','u_name','u_password']
    #排序
    ordering = ('u_id',)
    #搜索条件
    search_fields = ('u_id','u_name',)

@admin.register(models.Movies)
class MoviesAdmin(admin.ModelAdmin):
    #以列表的形式显示
    list_display = ['m_id','m_name','m_post']
    #排序
    ordering = ('m_id',)
    #搜索条件
    search_fields = ('m_id','m_name',)

    #要执行的方法
    def show(self,request,queryset):
        print(1)
    #给方法起名（指令）
    show.short_description = "爬取电影"
    #添加到action下拉菜单中
    actions = [show,]