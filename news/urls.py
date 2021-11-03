from django.conf.urls import url
from . import views

urlpatterns = [
    url('save/', views.save, name="save"),
    url('hacking/', views.hacking, name="hacking"),
    url('tech/', views.tech, name="tech"),   
    url('programming/', views.Programming.as_view(), name="programming"),
    url('^$', views.HomeNews.as_view(), name="home"),
]
