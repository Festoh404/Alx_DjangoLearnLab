# notifications/views.py
from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Notification
from .serializers import NotificationSerializer

class NotificationListView(generics.ListAPIView):
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Return notifications for the current user, ordered by creation date
        return Notification.objects.filter(recipient=self.request.user).order_by('-created_at')

    def get(self, request, *args, **kwargs):
        # Set all notifications to read when the user views them
        queryset = self.get_queryset()
        queryset.update(is_read=True)
        return super().get(request, *args, **kwargs)