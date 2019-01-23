# from django.urls import path
from django.conf.urls import url, include
from . import views

from django.conf import settings

urlpatterns = [
  url(r'^new/$', views.new),
  url(r'^mypage/(?P<num>\d+)/$', views.mypage),
  url(r'^mypage/$', views.redirect_top, name='mypage'),
  url(r'^delete/(?P<num>\d+)/$', views.delete),
  url(r'^delete/$', views.redirect_top, name='delete'),
  url(r'^edit/(?P<num>\d+)/$', views.edit),
  url(r'^edit/$', views.redirect_top, name='edit'),
  url(r'^show/(?P<num>\d+)/$', views.show),
  url(r'^show/$', views.redirect_top, name='show'),
  url(r'^$', views.index, name='index'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += (
        url(r'^pictweet/', include(debug_toolbar.urls)),
    )
