from rest_framework.authtoken import views as drf_views
from django.conf.urls import url, include
from rest_framework import routers, serializers, viewsets
from django.contrib.auth.models import User

app_name = "api"


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)


urlpatterns = [
    url(r'^auth$', drf_views.obtain_auth_token, name='auth'),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^', include(router.urls)),
]
