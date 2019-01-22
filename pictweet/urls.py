from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
  path('', views.index),
  path('new/', views.new),
  path('mypage/', views.mypage),
  url(r'^mypage/(?P<num>\d+)/$', views.mypage),
  url(r'^delete/(?P<num>\d+)/$', views.delete),
  url(r'^edit/(?P<num>\d+)/$', views.edit),
  url(r'^show/(?P<num>\d+)/$', views.show),
]
