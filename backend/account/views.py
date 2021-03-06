from rest_framework.generics import GenericAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.token_blacklist.models import OutstandingToken, BlacklistedToken
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.throttling import ScopedRateThrottle
from rest_framework.parsers import MultiPartParser
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from .serializers import UserSerializer, RegisterSerializer, LogOutSerializer, LogOutAllSerializer, EditProfileSerializer


# Create your views here.


class CurrentUserView(GenericAPIView):
    """
    API endpoint that returns the currently authenticated user's information.
    """
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer
    filter_backends = []
    pagination_class = None

    @swagger_auto_schema(responses={200: UserSerializer(many=False)}, operation_id="get_current_user", tags=["users"])
    def get(self, request):
        try:
            user = request.user
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(UserSerializer(user, context={'request': request}).data, status=status.HTTP_200_OK)

    def options(self, request, *args, **kwargs):
        meta = self.metadata_class()
        data = meta.determine_metadata(request, self)
        return Response(data=data, status=status.HTTP_200_OK)


class RegisterView(GenericAPIView):
    """
    API endpoint to register a user in the system.
    """
    authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny]
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'register'
    serializer_class = RegisterSerializer
    parser_classes = [MultiPartParser]
    filter_backends = []
    pagination_class = None

    @swagger_auto_schema(responses={200: TokenObtainPairSerializer(many=False)}, operation_id="register_user", tags=["users"])
    def post(self, request):
        serialiser = RegisterSerializer(data=request.data)
        response = dict()

        if serialiser.is_valid():
            new_user = serialiser.save()
            refresh_token = RefreshToken.for_user(new_user)
            response['jwt'] = {'refresh': str(refresh_token), 'access': str(refresh_token.access_token)}
            response['user'] = UserSerializer(new_user, context={'request': request}).data
            response_status = status.HTTP_201_CREATED
        else:
            response = serialiser.errors
            response_status = status.HTTP_400_BAD_REQUEST

        return Response(response, status=response_status)

    def options(self, request, *args, **kwargs):
        meta = self.metadata_class()
        data = meta.determine_metadata(request, self)
        return Response(data=data, status=status.HTTP_200_OK)


class EditProfileView(GenericAPIView):
    """
    API endpoint to edit a user's information.
    """
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'account_edit'
    serializer_class = EditProfileSerializer
    parser_classes = [MultiPartParser]
    filter_backends = []
    pagination_class = None

    @swagger_auto_schema(operation_id="edit_profile", tags=["users"])
    def post(self, request):
        serialiser = EditProfileSerializer(request.user.userextrainfo, data=request.data, partial=True)

        if serialiser.is_valid():
            updated_userextrainfo = serialiser.save()
            response = EditProfileSerializer(updated_userextrainfo, context={'request': request}).data
            response_status = status.HTTP_202_ACCEPTED
        else:
            response = serialiser.errors
            response_status = status.HTTP_400_BAD_REQUEST

        return Response(response, status=response_status)

    def options(self, request, *args, **kwargs):
        meta = self.metadata_class()
        data = meta.determine_metadata(request, self)
        return Response(data=data, status=status.HTTP_200_OK)


class LogOutView(GenericAPIView):
    """
    API endpoint to logout.
    """
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    throttle_classes = [ScopedRateThrottle]
    serializer_class = LogOutSerializer
    throttle_scope = 'logout'
    filter_backends = []
    pagination_class = None

    @swagger_auto_schema(responses={204: "User logged out."}, operation_id="logout_user", tags=["users"])
    def post(self, request):
        response = dict()

        if request.user:
            RefreshToken(request.data.get("refresh_token")).blacklist()

            response["result"] = "User logged out."
            response_status = status.HTTP_204_NO_CONTENT
        else:
            response["error"] = "Not logged in."
            response_status = status.HTTP_400_BAD_REQUEST

        return Response(response, status=response_status)

    def options(self, request, *args, **kwargs):
        meta = self.metadata_class()
        data = meta.determine_metadata(request, self)
        return Response(data=data, status=status.HTTP_200_OK)


class LogOutAllView(GenericAPIView):
    """
    API endpoint to logout on all devices.
    """
    # Known issue: Refreshed tokens aren't assigned a User, and hence won't be logged out through this.

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    throttle_classes = [ScopedRateThrottle]
    serializer_class = LogOutAllSerializer
    throttle_scope = 'logout'
    filter_backends = []
    pagination_class = None

    @swagger_auto_schema(responses={204: "User logged out."}, operation_id="logout_user_all", tags=["users"])
    def post(self, request):
        response = dict()

        if request.user:
            for token in OutstandingToken.objects.filter(user_id=request.user.id):
                BlacklistedToken.objects.get_or_create(token=token)

            response["result"] = "User logged out."
            response_status = status.HTTP_204_NO_CONTENT
        else:
            response["error"] = "Not logged in."
            response_status = status.HTTP_400_BAD_REQUEST

        return Response(response, status=response_status)

    def options(self, request, *args, **kwargs):
        meta = self.metadata_class()
        data = meta.determine_metadata(request, self)
        return Response(data=data, status=status.HTTP_200_OK)
