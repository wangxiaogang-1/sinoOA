from django.conf.urls import url
from authManage.views import *


urlpatterns = [
    url(r'delete', delete),
]
