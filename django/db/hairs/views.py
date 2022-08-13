from .models import Hair
from .serializers import HairSerializer
from rest_framework import status
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from django.http import JsonResponse


@api_view(["GET"])
@parser_classes([JSONParser])
def hair_api(request):
    try:
        print('hairs > GET')
        hairs = Hair.objects.all()
        serializer = HairSerializer(hairs, many=True)
        return Response(serializer.data)
    except Hair.DoesNotExist:
        return JsonResponse({'hairs': 'fail'})
