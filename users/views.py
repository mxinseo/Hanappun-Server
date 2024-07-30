from django.core.exceptions import ValidationError

from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.password_validation import validate_password

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import get_object_or_404

from .serializers import UserSerializer, UserProfileSerializer
from .models import User

# Create your views here.

# minseo : 회원 가입 뷰
class SignUpView(APIView):
    def post(self, request):
        username = request.data.get('username')
        nickname = request.data.get('nickname')
        password = request.data.get('password')
        password2 = request.data.get('password2')
        email = request.data.get('email')

        # 비밀번호 일치 확인
        if password != password2:
            return Response({"message": ["입력한 비밀번호가 다릅니다."]}, status=status.HTTP_400_BAD_REQUEST)
        
        # 비밀번호 유효성 검사
        try:
            validate_password(password)
        except ValidationError as e:
            return Response({"message": e.messages}, status=status.HTTP_400_BAD_REQUEST)

        # serializer로 유효성 검사 후 데이터 전달
        serializer = UserSerializer(data=request.data)
        serializer.email = email
        serializer.username = username
        serializer.nickname = nickname

        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            user.set_password(password)
            user.save()

            return Response({"message":"회원가입에 성공하였습니다."}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message": f"${serializer.errors}"}, status=status.HTTP_400_BAD_REQUEST)

# minseo : 로그인 뷰
class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
    
        if user is not None:
            auth_login(request, user) 
            return Response({"로그인에 성공하였습니다."}, status=status.HTTP_200_OK)
        else:
            return Response({"이름 혹은 비밀번호가 잘못 입력 되었습니다."}, status=status.HTTP_401_UNAUTHORIZED)

# minseo : 로그아웃 뷰
class LogoutView(APIView):
    def post(self, request):
        auth_logout(request)
        return Response({"로그아웃에 성공하였습니다."}, status=status.HTTP_200_OK)

# minseo : 탈퇴 뷰
class QuitView(APIView):
    def delete(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            user.delete()
            auth_logout(request) 
            return Response({"탈퇴에 성공하였습니다 "}, status=status.HTTP_200_OK)
        else:
            return Response({"이름 혹은 비밀번호가 잘못 입력 되었습니다."}, status=status.HTTP_401_UNAUTHORIZED)
        
# minseo : 프로필 조회, 수정
class ProfileView(APIView):
    def get_object(self, username):
        return get_object_or_404(User, username=username)

    # 프로필 조회
    def get(self, request):
        user = self.get_object(request.data.get('username'))
        serializer = UserProfileSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK) 