from .models import WorstColor
from .serializers import WorstColorSerializer
from rest_framework import status
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from django.http import JsonResponse


@api_view(["GET"])
@parser_classes([JSONParser])
def worst_color_api(request):
    try:
        print('worst colors > GET')
        worst_colors = WorstColor.objects.all()
        serializer = WorstColorSerializer(worst_colors, many=True)
        return Response(serializer.data)
    except WorstColor.DoesNotExist:
        return JsonResponse({'worst colors': 'fail'})
