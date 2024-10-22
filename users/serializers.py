from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    role = serializers.ChoiceField(choices=Profile.ROLES)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'role', 'password')

    def validate_role(self, value):
        if not hasattr(Profile, 'ROLES') or not Profile.ROLES:
            raise serializers.ValidationError("Profile roles are not defined.")
        
        value_lower = value.lower()
        if value_lower not in dict(Profile.ROLES).keys():
            raise serializers.ValidationError("Invalid role")
        return value_lower

    def create(self, validated_data):
        role = validated_data.pop('role')
        user = User.objects.create_user(**validated_data)
        Profile.objects.create(user=user, role=role)
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

class PasswordResetSerializer(serializers.Serializer):
    email = serializers.EmailField()

class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')
        partial = True

class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    user_id = serializers.SerializerMethodField()  
    username = serializers.SerializerMethodField()
    email = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = ('id', 'user_id', 'username', 'email', 'user', 'role')

    def create(self, validated_data):
        return Profile.objects.create(**validated_data)

    def get_user_id(self, obj):
        return obj.user.id

    def get_username(self, obj):
        return obj.user.username

    def get_email(self, obj):
        return obj.user.email
