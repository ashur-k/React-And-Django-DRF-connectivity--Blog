from rest_framework.decorators import api_view
from rest_framework.response import Response

from . models import MyInfo
from . serializers import MyInfoSerializer


@api_view(['GET'])
def myInfo(request):
  my_info = MyInfo.objects.all();
  serializer = MyInfoSerializer(my_info, many=True)
    
  return Response(serializer.data)
