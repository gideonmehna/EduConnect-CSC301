# from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from django.contrib.auth.models import User

from Accounts.models import UserProfile


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = UserProfile
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'password', 'phone_number',
                  'avatar', 'password2']
        extra_kwargs = {
            'username' : {'required': True},
            'first_name': {'required': True},
            'last_name': {'required': True},
            'password': {'required': True},
            'email': {'required': True}
        }

    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.pop('password2')
        if password != password2:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):

        user = UserProfile.objects.create_user(**validated_data)
        # user.save()
        return user

# class AccountSerializer(serializers.ModelSerializer):
#     user = UserSerializer()
#
#     class Meta:
#         model = UserProfile
#         fields = ['id', 'user', 'phone_number', 'password2']
#         depth = 1
#



class UpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'password', 'phone_number',
                  'avatar']
        extra_kwargs = {
            'username': {'required': False},
            'first_name': {'required': False},
            'last_name': {'required': False},
            'password': {'required': False},
            'email': {'required': False},
            'phone_number': {'required': False},
            'avatar': {'required': False}
        }

    # def update(self, instance, validated_data):
    #     user_data = validated_data.pop('user', None)
    #     if user_data:
    #         user = instance.user
    #         for attr, value in user_data.items():
    #             setattr(user, attr, value)
    #         user.save()
    #
    #     for attr, value in validated_data.items():
    #         setattr(instance, attr, value)
    #
    #     instance.save()
    #     return instance







