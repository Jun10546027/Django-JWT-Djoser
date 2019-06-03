# Create your views here.
from rest_framework import viewsets
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework import status,generics

from .models import Music,Coupon,User
from .serializers import MusicSerializer ,CouponSerializer,UserSerializer




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
class CouponViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Coupon.objects.all()
    serializer_class = CouponSerializer
    permission_classes = (IsAuthenticated,)

#eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6Imp1biIsImV4cCI6MTU1OTQwODYwNiwiZW1haWwiOiIxMjNAMTMyLjEyIn0.T1a4IUlW3F5ysUk3f5tOV7GMG_3Uesbpfl3BPhv367Y

#curl -H "Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6Imp1biIsImV4cCI6MTU1OTQwODYwNiwiZW1haWwiOiIxMjNAMTMyLjEyIn0.T1a4IUlW3F5ysUk3f5tOV7GMG_3Uesbpfl3BPhv367Y" http://localhost:8000/music/

#curl http://localhost:8000/music/