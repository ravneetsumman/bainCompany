from django.urls import include, path
from .views import Providers
from api import views

urlpatterns = {
    path('providers/', Providers.as_view(), name="list")
}
