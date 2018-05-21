from rest_framework.authtoken import views as drf_views
from django.conf.urls import url, include
from rest_framework import routers
from .views import UserViewSet

app_name = "api"

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)


urlpatterns = [
    url(r'^auth$', drf_views.obtain_auth_token, name='auth'),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^', include(router.urls)),
]
