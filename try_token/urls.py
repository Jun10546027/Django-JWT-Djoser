from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter


from django.conf import settings
from django.conf.urls.static import static

from test_token.views import MusicViewSet,CouponViewSet,UserViewSet,UserFavViewset,ActivateUserByGet,ResetPasswordUserByGet

router = DefaultRouter()
router.register(r'music', MusicViewSet, base_name='music')
router.register(r'coupon',CouponViewSet,base_name='coupon')
router.register(r'users',UserViewSet,base_name='user')
router.register(r'userfavs', UserFavViewset, base_name="userfavs")

urlpatterns = [
    path("",include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/',include('djoser.urls.jwt')),
    # path('activate1/(?P<uid>[\w-]+)/(?P<token>[\w-]+)/$', UserActivationView.as_view()),
    path('auth/activate/<str:uid>/<str:token>/', ActivateUserByGet.as_view()),
    path('auth/password/reset/confirm/<str:uid>/<str:token>/',ResetPasswordUserByGet.as_view()),

    path('api/login/', include('rest_social_auth.urls_jwt_pair')),
    path('api/login/', include('rest_social_auth.urls_jwt_sliding')),
    # path('auth/', include('rest_framework_social_oauth2.urls')),
    # path('social-auth/', include('social_django.urls', namespace='social')),

    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)