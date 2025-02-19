"""website URL Configuration"""
from django.conf.urls import include
from django.contrib import admin
from django.urls import re_path

sitemaps = {}

urlpatterns = [
    re_path(r"admin/", admin.site.urls),
    re_path(r"i18n/", include("django.conf.urls.i18n")),
    re_path(r"accounts/", include("django.contrib.auth.urls")),
    re_path(r"", include("leave.urls")),
]
