from django.conf.urls import url

from . import views

app_name='my_creep'
urlpatterns = [
    url(r'^movie/$', views.movie,name='creep_mv'),
    url(r'^weather/$', views.weather,name='creep_wea'),
    url(r'^jdphone/$', views.jdphone,name='creep_jd'),
    url(r'^mainPage/$', views.mainPage,name='creep_mainPage')
]


