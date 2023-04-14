from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'password',
            'confirm_password',
        ]

    def validate(self, data):
        if data.get('password') != data.pop('confirm_password', None):
            raise serializers.ValidationError('Password did not match')
        return data

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'first_name',
            'last_name',
        ]
