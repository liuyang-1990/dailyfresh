from django.db import models


# Create your models here.
class UserInfo(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    recipients = models.CharField(max_length=20)  # 收件人
    address = models.CharField(max_length=500)
    postcode = models.CharField(max_length=6)
    mobilephone = models.CharField(max_length=11)
