from django.conf.urls import  include, url, patterns
from django.views.generic import ListView
from . import views

urlpatterns = [
		url(r'^$',views.index, name = 'index'),
		url(r'^file/', views.simple_upload, name = 'simple_upload'),
		]

