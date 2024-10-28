from users_app.api.serializers.user_serializer import RegisterUserSerializer
from users_app.api.models import user_model
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken# type: ignore

class RegisterUser(APIView):
    def post(self, request):
        print(request)
        serializer=RegisterUserSerializer(data=request.data)
        data={}
        if serializer.is_valid():
            account=serializer.save()
            
            data['response']="Successfully registered"
            data['username']=account.username
            data['email']=account.email
            
            
            refresh = RefreshToken.for_user(account)
        
            data['token']= {
                   'refresh': str(refresh),
                   'access': str(refresh.access_token),
                   }
            return Response(data)
        
        return Response({
            'error': 'Registration failed',
            'details': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
        
