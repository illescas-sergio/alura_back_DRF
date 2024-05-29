from django.contrib.auth import authenticate, login, logout
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import CustomUserSerializer, RegisterUserSerializer
from rest_framework import generics
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication



class RegisterApiView(generics.CreateAPIView):
    serializer_class = RegisterUserSerializer


class LoginView(APIView):

    def post(self, request):
        # Recuperamos las credenciales y autenticamos al usuario
        
        email = request.data.get('email', None)
        password = request.data.get('password', None)
        user = authenticate(email=email, password=password)

        # Si es correcto añadimos a la request la información de sesión
        if user:
            login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class LogoutView(APIView):

    authentication_classes = [TokenAuthentication]

    
    def post(self, request):

        user = request.user

        Token.objects.filter(user=user).delete()

        logout(request)

        return Response({'message': 'Successfully logged out'}, status=status.HTTP_200_OK)
    

class ProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = CustomUserSerializer
    http_method_names = ['get', 'patch', 'options']
    authentication_classes = [TokenAuthentication]

    def get_object(self):
        if self.request.user.is_authenticated:
            return self.request.user
    