from django.conf.urls import url, include
from django.urls import path
from . import views

# set the application namespace
# https://docs.djangoproject.com/en/2.0/intro/tutorial03/
app_name = 'accounts'

urlpatterns = [
  # path('signup/', views.SignUpView.as_view(), name='signup'),
  url(r'^signup/$', views.SignUpView.as_view(), name='signup'),
]
