from django.urls import include, path, re_path
from .views import Providers
from api import views
from django.conf.urls import url

urlpatterns = [
    #path('providers/', Providers.as_view(), name="list")
    #re_path(r'^providers/$', Providers.as_view(), name="list"),
    url(r'^providers/$', Providers.as_view(), name="list"),
]
