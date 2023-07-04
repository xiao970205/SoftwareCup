"""software_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from app01 import views

urlpatterns = [
    # path('',admin.site.urls),
    path('admin/', admin.site.urls),
    path('login/',views.login),
    path('user_list/',views.user_list),
    path('pic/',views.pic),
    path('get_post/',views.get_post_info_test),
    path('up_file/',views.up_file),
    path('uploadPage/',views.uploadPage),
    path('download_flie/',views.download_file)
]
