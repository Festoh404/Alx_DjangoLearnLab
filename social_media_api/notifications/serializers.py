# notifications/serializers.py
from rest_framework import serializers
from .models import Notification

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ['id', 'recipient', 'actor', 'verb', 'target', 'is_read', 'created_at']
        read_only_fields = ['recipient', 'actor', 'verb', 'target', 'created_at']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        # You may want to customize the representation of the 'target' here
        return representation