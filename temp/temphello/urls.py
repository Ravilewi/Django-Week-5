from django.urls import path
from .views import helloworldjson

urlpatterns = [
    path("", helloworldjson, name="home"),
]
