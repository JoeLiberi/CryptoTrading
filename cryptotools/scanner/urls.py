from django.urls import path, re_path
from django.conf.urls import include, url
from . import views

urlpatterns = [
	url(r'^$', views.scanner),
]