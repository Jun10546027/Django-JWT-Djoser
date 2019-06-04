from django.db import models


# Create your models here.
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    created = models.DateTimeField(auto_now_add=True)
    gender=models.CharField(max_length=1)
    REQUIRED_FIELDS = ["email", "gender"]

    class Meta:
        ordering = ('created',)

class Coupon(models.Model):
    # user = models.ForeignKey(User,on_delete=models.CASCADE)
    coupon_id = models.CharField(max_length=20, primary_key=True)
    coupon_price = models.IntegerField()
    coupon_title = models.CharField(max_length=150)
    coupon_class = models.CharField(max_length=20)
    coupon_content = models.CharField(max_length=200)
    coupon_create_at = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ('coupon_create_at',)

    def __str__(self):
        return self.coupon_title

class Music(models.Model):
    song = models.TextField()
    singer = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "music"