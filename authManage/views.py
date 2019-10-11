import os
import django


from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sinoOA.settings")
django.setup()



@api_view(['GET'])
def delete(request):
    """"""
    id = request.GET.get('id')
    if not id:
        return Response(status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def user_add(request):
    """用户添加"""
