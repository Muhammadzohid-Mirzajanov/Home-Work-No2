"""
URL configuration for homework2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from homework2.homework2.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('views1/',views1),
    path('views2/',views2),
    path('views3/',views3),
    path('views4/',views4),
    path('views5/',views5),
    path('views6/',views6),
    path('views7/',views7),
    path('views8/',views8),
    path('views9/',views9),
    path('views10/',views10),

]