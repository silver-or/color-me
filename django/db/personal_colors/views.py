from .models import PersonalColor
from .serializers import PersonalColorSerializer
from rest_framework import status
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from django.http import JsonResponse


@api_view(["GET"])
@parser_classes([JSONParser])
def personal_color_api(request):
    try:
        print('personal colors > GET')
        personal_colors = PersonalColor.objects.all()
        serializer = PersonalColorSerializer(personal_colors, many=True)
        return Response(serializer.data)
    except PersonalColor.DoesNotExist:
        return JsonResponse({'personal colors': 'fail'})
