from django.conf.urls import url,include
from . import views

urlpatterns = [
    url('send/', views.sendMail, name="send"),
    url('contact/', views.contact, name="contact"),
    url('delete/', views.delete, name="delete"),
    url('save/', views.save, name="save"),
    url('hacking/', views.hacking, name="hacking"),
    url('tech/', views.tech, name="tech"),   
    url('programming/', views.Programming.as_view(), name="programming"),
    url('^$', views.HomeNews.as_view(), name="home"),
    url('accounts/', include('django.contrib.auth.urls')),
]
