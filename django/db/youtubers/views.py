from .models import Youtuber
from .serializers import YoutuberSerializer
from rest_framework import status
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from django.http import JsonResponse


@api_view(["GET"])
@parser_classes([JSONParser])
def youtuber_api(request):
    try:
        print('youtubers > GET')
        youtubers = Youtuber.objects.all()
        serializer = YoutuberSerializer(youtubers, many=True)
        return Response(serializer.data)
    except Youtuber.DoesNotExist:
        return JsonResponse({'youtubers': 'fail'})
