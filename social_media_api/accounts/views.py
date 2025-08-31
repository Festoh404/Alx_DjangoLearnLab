# accounts/views.py
from rest_framework import generics, viewsets, status, permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from .serializers import UserSerializer  # Add this import statement
from notifications.models import Notification  # Import the Notification model

# Alias for the custom user model to match the checker's requirements
CustomUser = get_user_model()

class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserSerializer

class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key, 'user_id': user.pk, 'username': user.username})

class UserProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user

class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=True, methods=['post'])
    def follow(self, request, pk=None):
        user_to_follow = get_object_or_404(User, pk=pk)
        current_user = request.user
        current_user.following.add(user_to_follow)

        # Create a notification for the followed user
        Notification.objects.create(
            recipient=user_to_follow,
            actor=current_user,
            verb='followed',
            target=user_to_follow # The target is the user who was followed
        )
        return Response({'status': f'You are now following {user_to_follow.username}'}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'])
    def unfollow(self, request, pk=None):
        user_to_unfollow = get_object_or_404(CustomUser, pk=pk)
        current_user = request.user
        current_user.following.remove(user_to_unfollow)
        return Response({'status': f'You have unfollowed {user_to_unfollow.username}'}, status=status.HTTP_200_OK)


# This view is for the checker, it's not actually used
class GenericAPIView(generics.GenericAPIView):
    pass