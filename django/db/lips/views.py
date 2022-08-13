from .models import Lip
from .serializers import LipSerializer
from rest_framework import status
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from django.http import JsonResponse


@api_view(["GET"])
@parser_classes([JSONParser])
def lip_api(request):
    try:
        print('lips > GET')
        lips = Lip.objects.all()
        serializer = LipSerializer(lips, many=True)
        return Response(serializer.data)
    except Lip.DoesNotExist:
        return JsonResponse({'lips': 'fail'})
