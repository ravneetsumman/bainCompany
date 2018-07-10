from django.urls import include, path, re_path, url
from .views import Providers
from api import views


urlpatterns = [
    #path('providers/', Providers.as_view(), name="list")
    #re_path(r'^providers/$', Providers.as_view(), name="list"),
    url(r'^providers/$', Providers.as_view(), name="list"),
]
