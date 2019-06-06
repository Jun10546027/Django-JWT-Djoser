from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token
from rest_framework_jwt.views import verify_jwt_token
from rest_framework.routers import DefaultRouter

from test_token.views import MusicViewSet,CouponViewSet,UserViewSet,UserFavViewset

router = DefaultRouter()
router.register(r'music', MusicViewSet, base_name='music')
router.register(r'coupon',CouponViewSet,base_name='coupon')
router.register(r'users',UserViewSet,base_name='user')
router.register(r'userfavs', UserFavViewset, base_name="userfavs")

urlpatterns = [
    path("",include(router.urls)),
    path('auth/', include('djoser.urls')),
    # path('auth/', include('djoser.urls.jwt')),
    path('admin/', admin.site.urls),
    path('api-token-auth/', obtain_jwt_token),
    path('api-token-refresh/', refresh_jwt_token),
    path('api-token-verify/', verify_jwt_token),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]