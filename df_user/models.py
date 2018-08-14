from django.db import models


# Create your models here.
class UserInfo(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=50, null=True)
    recipients = models.CharField(max_length=20, null=True)  # 收件人
    address = models.CharField(max_length=500, null=True)
    postcode = models.CharField(max_length=6, null=True)
    mobilephone = models.CharField(max_length=11, null=True)
