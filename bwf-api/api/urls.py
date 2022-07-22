from api import views
from rest_framework import routers
from django.urls import path, include
from django.contrib import admin

router = routers.DefaultRouter()
router.register(r'groups', views.GroupViewset)


urlpatterns = [
    path(r'^', include(router.urls)),
]
