from rest_framework import serializers

from .models import Music,Coupon,User


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('url', 'id', 'email', 'name', 'last_name', 'birthday', 'password')

class CouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        fields = ('coupon_id','coupon_title','coupon_class','coupon_content')

class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = ('song','singer')