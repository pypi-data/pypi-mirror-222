"""
Urls for herald app
"""

from django.urls import path, re_path

from .views import TestNotificationList, TestNotification

urlpatterns = [
    path('', TestNotificationList.as_view(), name='herald_preview_list'),
    re_path(r'^(?P<index>\d+)/(?P<type>[\w\-]+)/$', TestNotification.as_view(), name='herald_preview'),
]
