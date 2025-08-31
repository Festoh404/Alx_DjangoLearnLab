from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'phone', 'address', 'bio', 'profile_picture')

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=6)  # This line is required
    password2 = serializers.CharField(write_only=True, min_length=6)  # This line is required
    
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password', 'password2', 'phone', 'address', 'bio')
    
    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError("Passwords don't match")
        return data
    
    def create(self, validated_data):
        validated_data.pop('password2')
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            phone=validated_data.get('phone', ''),
            address=validated_data.get('address', ''),
            bio=validated_data.get('bio', '')
        )
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()  # This line is required
    password = serializers.CharField()  # This line is required
    
    def validate(self, data):
        username = data.get('username')
        password = data.get('password')
        
        if username and password:
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    data['user'] = user
                    return data
                else:
                    raise serializers.ValidationError("User account is disabled.")
            else:
                raise serializers.ValidationError("Unable to log in with provided credentials.")
        else:
            raise serializers.ValidationError("Must include username and password.")