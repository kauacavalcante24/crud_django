from rest_framework import serializers
from .models import User
import re


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def validate_user_nickname(self, value):
        value = value.lower()
        if not re.match(r'^[a-z0-9._]+$', value):
            raise serializers.ValidationError("The nickname must contain only lowercase letters, numbers, dots, and underscores.")
        if len(value) > 30:
            raise serializers.ValidationError("The nickname must be at most 30 characters long.")
        return value

    def validate_user_email(self, value):
        value = value.lower()
        if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', value):
            raise serializers.ValidationError("Invalid email.")
        return value

    def validate_user_age(self, value):
        if value < 13:
            raise serializers.ValidationError("Insufficient or invalid age to access the system.")
        return value
