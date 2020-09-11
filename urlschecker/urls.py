from django.urls import path
from .views import *

app_name = "urlschecker"

urlpatterns = [
    path('', home, name="home"),
    path('update_status/', update_urls_status, name="update_status"),
    path('load_urls/', load_urls, name="load_urls"),
]
