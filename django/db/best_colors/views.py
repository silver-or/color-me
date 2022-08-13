from .models import BestColor
from .serializers import BestColorSerializer
from rest_framework import status
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from django.http import JsonResponse


@api_view(["GET"])
@parser_classes([JSONParser])
def best_color_api(request):
    try:
        print('best colors > GET')
        best_colors = BestColor.objects.all()
        serializer = BestColorSerializer(best_colors, many=True)
        return Response(serializer.data)
    except BestColor.DoesNotExist:
        return JsonResponse({'best colors': 'fail'})
