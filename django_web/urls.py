"""django_web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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

from django.urls import re_path, include, path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from login.views import *
import common

urlpatterns = [
    path("", home, ),  # 根路由，http://localhost:8000
    re_path(r'^login/', login),
    re_path(r'^news/', tables),
    re_path(r'^neo4j/', neo4j),
    re_path(r'^choujiang/', choujiang),
    re_path(r'^logout/', logout),

]

urlpatterns += staticfiles_urlpatterns()
