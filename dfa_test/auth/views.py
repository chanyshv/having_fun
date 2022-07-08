from django.contrib.auth.models import User
from django.contrib.auth import (
    login,
    logout,
)
from rest_framework.permissions import AllowAny
from rest_framework import (
    generics,
    views,
    permissions,
    response,
    request,
)
from rest_framework.authentication import SessionAuthentication
from auth.serializers import (
    UserSerializer,
    LoginSerializer,
)


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class LoginView(views.APIView):
    permission_classes = [permissions.AllowAny]
    authentication_classes = [SessionAuthentication]

    def post(self, request: request.Request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        if user is None:
            return response.Response({"error": "Invalid credentials"}, status=401)
        login(request, user)
        return response.Response(UserSerializer(user).data)


class LogoutView(views.APIView):
    authentication_classes = [SessionAuthentication]

    def post(self, request: request.Request):
        logout(request)
        return response.Response()


class GetUserView(generics.RetrieveAPIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user
