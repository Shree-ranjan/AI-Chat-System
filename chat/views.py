from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import make_password, check_password
from .models import User, Chat
from .serializers import UserSerializer, ChatSerializer
import uuid

# Temporary in-memory token store
AUTH_TOKENS = {}


class RegisterView(APIView):
    def post(self, request):
        data = request.data
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save(password=make_password(data['password']))
            return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        try:
            user = User.objects.get(username=username)
            if check_password(password, user.password):
                token = str(uuid.uuid4())
                AUTH_TOKENS[token] = user.id
                return Response({'token': token}, status=status.HTTP_200_OK)
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)


class ChatView(APIView):
    def post(self, request):
        token = request.headers.get('Authorization')
        user_id = AUTH_TOKENS.get(token)
        if not user_id:
            return Response({'error': 'Unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)

        user = User.objects.get(id=user_id)
        if user.tokens < 100:
            return Response({'error': 'Insufficient tokens'}, status=status.HTTP_400_BAD_REQUEST)

        message = request.data.get('message')
        response = "This is a dummy AI response"  # Placeholder for actual AI logic
        user.tokens -= 100
        user.save()

        chat = Chat.objects.create(
            user=user, message=message, response=response)
        return Response(ChatSerializer(chat).data, status=status.HTTP_201_CREATED)


class TokenBalanceView(APIView):
    def get(self, request):
        token = request.headers.get('Authorization')
        user_id = AUTH_TOKENS.get(token)
        if not user_id:
            return Response({'error': 'Unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)

        user = User.objects.get(id=user_id)
        return Response({'tokens': user.tokens}, status=status.HTTP_200_OK)
