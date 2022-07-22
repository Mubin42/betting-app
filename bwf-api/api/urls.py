from api import views
from rest_framework import routers
from django.urls import path, include, re_path
from django.contrib import admin

router = routers.DefaultRouter()
router.register(r'groups', views.GroupViewset)


urlpatterns = [
    re_path(r'^', include(router.urls)),
]
