from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import Providers
#from rest_framework.authtoken.views import obtain_auth_token
from api import views

urlpatterns = {
    url(r'^providers/$', Providers.as_view(), name="list"),
}

urlpatterns = format_suffix_patterns(urlpatterns)
