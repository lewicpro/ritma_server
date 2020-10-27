from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.views import APIView
from app.user.api.serializers import UsersSerializer
from app.user.models import User
from rest_framework.permissions import AllowAny


class UserCreate(generics.CreateAPIView):
    permission_classes = (AllowAny, )
    queryset = User.objects.all()
    serializer_class = UsersSerializer
    