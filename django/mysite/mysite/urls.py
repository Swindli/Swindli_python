"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = (
    url(r'^admin/', include(admin.site.urls)),
	url(r'^$','mysite.views.hello'),
	url(r'^time/$', 'mysite.views.current_datetime'),
	url(r'^meta/$', 'mysite.views.display_meta'),
	url(r'^time/plus/(\d{1,2})/$','mysite.views.hours_ahead'),
	url(r'^search-form/$','books.views.search_form'),
	url(r'^search/$', 'books.views.search'),
	url(r'^contact/$', 'contact.views.contact'),
	url(r'^excel/$','excelAnalysis.views.excel'),
	url(r'^spider/$', 'spider.views.spider'),
)
