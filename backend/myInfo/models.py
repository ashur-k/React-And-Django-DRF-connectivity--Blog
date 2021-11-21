from django.db import models


class MyInfo(models.Model):
  first_name = models.CharField(max_length=200, null=True, blank=True)
  second_name = models.CharField(max_length=200, null=True, blank=True)
  image = models.ImageField(null=True, blank=True, default='/placeholder.png')
  about_you = models.TextField(null=True, blank=True)
