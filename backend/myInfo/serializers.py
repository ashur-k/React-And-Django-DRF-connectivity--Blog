from rest_framework import serializers
from .models import MyInfo


class MyInfoSerializer(serializers.ModelSerializer):
  class Meta:
    model = MyInfo
    fields = '__all__'
