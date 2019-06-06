# Create your views here.
from rest_framework import viewsets
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

#permission(用於我的最愛)
from util.permission import IsOwnerOrReadOnly
from rest_framework.response import Response
from rest_framework import status,generics,mixins

from .models import Music,Coupon,User,UserFav
from .serializers import MusicSerializer ,CouponSerializer,UserSerializer ,UserFavSerializer

#設定分頁
from rest_framework.pagination import PageNumberPagination

#設定過濾器
from .filter import CouponFilter
from django_filters.rest_framework import DjangoFilterBackend

#設定搜尋，排序
from rest_framework.filters import SearchFilter , OrderingFilter

##Coupont自訂分頁
class CouponPagination(PageNumberPagination):
    #每頁顯示個數
    page_size = 10
    #允許動態改變每頁顯示個數
    page_size_query_param = 'page_size'
    #設定頁碼參數
    page_query_param = 'page'
    #最多多少頁
    max_page_size = 100

# Create your views here.
class MusicViewSet(viewsets.ModelViewSet):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer
    parser_classes = (JSONParser,)
    #permission_classes = [AllowAny]
    permission_classes = (IsAuthenticated,)

class UserViewSet(viewsets.ModelViewSet):
    permission_classes = ()
    queryset = User.objects.all()
    serializer_class = UserSerializer


# Create your views here.
class CouponViewSet(viewsets.ModelViewSet):
    queryset = Coupon.objects.all()
    serializer_class = CouponSerializer

    #載入自定義Pagination
    pagination_class = CouponPagination

    #自定義filter
    filter_backends = (DjangoFilterBackend,SearchFilter,OrderingFilter)
    filter_class = CouponFilter

    #permission設置(JWT)
    permission_classes = ()

    #search設定
    search_fields = ("coupon_title","coupon_class")

    #ordering_fields -->  設定可排序的參數      ordering  ->  默認排序
    ordering_fields = ('coupon_price',)
    ordering=('coupon_title',)

#我的最愛
class UserFavViewset(viewsets.GenericViewSet
                    ,mixins.RetrieveModelMixin
                    , mixins.ListModelMixin
                    , mixins.CreateModelMixin
                    , mixins.DestroyModelMixin):

    queryset = UserFav.objects.all()
    serializer_class = UserFavSerializer

    #透過自定permission，來判斷使用者是誰
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    #因為在serializers 是 coupons ->所以這裡不是coupon_id
    lookup_field = 'coupons_id'

    def get_queryset(self):
        # 只能看到自己的收藏，不能看到別人的
        return UserFav.objects.filter(user=self.request.user)

