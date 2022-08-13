from .models import Post
from .serializers import PostSerializer
from rest_framework import status
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from django.http import JsonResponse


@api_view(["GET"])
@parser_classes([JSONParser])
def post_api(request):
    try:
        print('posts > GET')
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    except Post.DoesNotExist:
        return JsonResponse({'posts': 'fail'})
