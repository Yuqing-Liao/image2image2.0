"""Process_web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from os import name, replace
from django.conf.urls import url
from django.contrib import admin
from django.urls import path,re_path
from i2iProcessApp import views

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import staticfiles
from django.contrib.staticfiles.urls import static
from . import settings

'''
urlpatterns = [
    path('admin/', admin.site.urls),
    path('render/',views.html_data),
    re_path(r'^download/(?P<file>)',views.download_file,name='download'),
    path('test/',views.test),
    re_path('uploadPage/',views.page),
    re_path(r'^storage/',views.storage_view),
    re_path(r'^$',views.test)
    #re_path(r'^$',views.test)
]
'''
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',views.index),
    path('result/',views.result),
    path('cTime/',views.cTime,name='changetime'),
    path('cSimple/',views.cSimple),
    path('cByself/',views.cByself),
    path('invoke/',views.invoke),
    path('wait/',views.wait),
    path('cBysystem/',views.cBysystem),
    path('download/',views.download_file),
    re_path(r'^upload/',views.uploadToChange),
    re_path('Up/',views.page),
    re_path(r'^$',views.index),
    path('test/',views.test),
    #re_path(r'^download/(?P<file_path>.*)/$',views.download_file)
    #re_path(r'^$',views.test)
]


urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)