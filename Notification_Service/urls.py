"""Notification_Service URL Configuration

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
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from core.views import MailingListViews, ClientViews, Mailing_list_statistic

api_version = 'api/v1/'

router_ml = routers.DefaultRouter()
router_ml.register(r'mailing_list', MailingListViews)

router_c = routers.DefaultRouter()
router_c.register(r'client', ClientViews)


urlpatterns = [
    path('admin/', admin.site.urls),
    path(f'{api_version}', include(router_ml.urls)),
    path(f'{api_version}', include(router_c.urls)),
    path(f'{api_version}mailing_list_statistic', Mailing_list_statistic.as_view()),
    path(f'{api_version}mailing_list_statistic/<int:pk>', Mailing_list_statistic.as_view())
]
