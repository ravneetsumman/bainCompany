from django.urls import include, path, re_path, URLResolver, URLPattern
from .views import Providers
from api import views
#from django.conf.urls import url
#from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('providers/', Providers.as_view(), name="list")
]
#urlpatterns = format_suffix_patterns(urlpatterns)
