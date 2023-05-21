from users import serializers
from django.contrib.auth import get_user_model
from rest_framework import status, viewsets
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
# from .models import Profile

User = get_user_model()


class UserRegisterationViewSet(viewsets.ModelViewSet):
    """
    An endpoint for the client to create a new User.
    """
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.UserRegisterationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = RefreshToken.for_user(user)
        data = serializer.data
        data["tokens"] = {"refresh": str(
            token), "access": str(token.access_token)}
        return Response(data, status=status.HTTP_201_CREATED)


class UserLoginViewSet(viewsets.ModelViewSet):
    """
    An endpoint to authenticate existing users using their dni and password.
    """

    permission_classes = (AllowAny,)
    serializer_class = serializers.UserLoginSerializer
    queryset = User.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        serializer = serializers.CustomUserSerializer(user)
        token = RefreshToken.for_user(user)
        data = serializer.data
        data["tokens"] = {"refresh": str(
            token), "access": str(token.access_token)}
        return Response(data, status=status.HTTP_200_OK)


class UserLogoutViewSet(viewsets.ModelViewSet):
    """
    An endpoint to logout users.
    """

    permission_classes = (AllowAny,)
    serializer_class = serializers.UserLoginSerializer
    queryset = []

    def create(self, request, *args, **kwargs):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)


class UserAPIView(RetrieveUpdateAPIView):
    """
    Get, Update user information
    """

    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.CustomUserSerializer

    def get_object(self):
        return self.request.user


# class UserProfileAPIView(RetrieveUpdateAPIView):
#     """
#     Get, Update user profile
#     """

#     queryset = Profile.objects.all()
#     serializer_class = serializers.ProfileSerializer
#     permission_classes = (IsAuthenticated,)

#     def get_object(self):
#         return self.request.user.profile


# class UserAvatarAPIView(RetrieveUpdateAPIView):
#     """
#     Get, Update user avatar
#     """

#     queryset = Profile.objects.all()
#     serializer_class = serializers.ProfileAvatarSerializer
#     permission_classes = (IsAuthenticated,)

#     def get_object(self):
#         return self.request.user.profile
