from django.urls import path
from movies import views

urlpatterns = [
    path('',views.index),
    path('search/', views.search),
    path('denglu/', views.denglu),
    path('logout/', views.logout),
    path('zhuce/', views.zhuce),
    path('classify/',views.classify),
    path('nation/',views.nation),
    path('data/',views.data),
    path('list/',views.list),
    path('get_info/',views.get_info),
    path('shoucang/',views.shoucang),
    path('shoucang_jiaru/',views.shoucang_jiaru),
    path('fenye/',views.fenye),
]