from django.shortcuts import render
from .models import Skin
from .serializers import SkinSerializer
from rest_framework import status
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from django.http import JsonResponse

# Create your views here.


@api_view(["GET"])
@parser_classes([JSONParser])
def skin_api(request):
    try:
        print('skins > GET')
        skins = Skin.objects.all()
        serializer = SkinSerializer(skins, many=True)
        return Response(serializer.data)
    except Skin.DoesNotExist:
        return JsonResponse({'skins': 'fail'})

