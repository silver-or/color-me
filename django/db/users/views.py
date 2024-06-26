from .models import User
from .serializers import UserSerializer, LoginSerializer, TokenSerializer
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.authtoken.models import Token


@api_view(["GET", "POST", "PUT", "DELETE"])
@parser_classes([JSONParser])
def join(request):
    print('1. join 으로 들어옴')
    try:
        if request.method == 'GET':  # Read
            print('2. GET 으로 들어옴')
            all_users = User.objects.all()
            serializer = UserSerializer(all_users, many=True)
            return Response(serializer.data)
        elif request.method == 'POST':  # Create
            print(f'2. POST 로 들어옴')
            # print('request_data: ', request.data)
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):  # raise된 에러를 가시적으로 클라이언트에 전달
                # print(serializer)
                # print('3. 들어온 내부값: ', serializer.data)
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            print('error: ', serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'PUT':  # Update
            print('2. PUT 으로 들어옴')
            email = request.data.get('email', None)
            user = get_object_or_404(User, email=email)
            serializer = UserSerializer(user, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':  # Delete
            email = request.data.get('email', None)
            user = get_object_or_404(User, email=email)
            user.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
    except User.DoesNotExist:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
@parser_classes([JSONParser])
def login(request):
    email = request.data.get('email')  # 클라이언트 요청 이메일
    password = request.data.get('password')  # 클라이언트 요청 패스워드
    user = get_object_or_404(User, email=email)
    try:
        if email == user.email:
            if password == User.objects.get(email=email).password:
                Token.objects.create(user=user)
                token = Token.objects.get(user=user)
                # data = User.objects.get(email=email).username
                loginSerializer = LoginSerializer(user)
                # serializer = TokenSerializer(token)
                # serializer = TokenSerializer(token=token)
                # token = Token.objects.create(user=settings.AUTH_USER_MODEL)
                print(' ############################# ')
                print(f' 출력된 토큰값: {token}')
                print(' ############################# ')
                return Response(loginSerializer.data)
            else:
                print('#############3')
                return Response({"Message": "비밀번호 오류"})
    except User.DoesNotExist:
        print('#############4')
        return Response({"Message": "존재하지 않는 아이디"})


@api_view(["POST"])
@parser_classes([JSONParser])
def logout(request):
    email = request.data.get('email')  # 클라이언트 요청 이메일
    user = get_object_or_404(User, email=email)
    access_token = Token.objects.get(user=user)
    access_token.delete()
    return Response({"Message": "Logout Successfully"}, status=status.HTTP_200_OK)