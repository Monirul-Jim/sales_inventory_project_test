
from rest_framework import serializers
# from django.contrib.auth import get_user_model
# User=get_user_model()
from users.models import User


class UserRegistrationSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'firstName',
            'lastName',
            'email',
            'password',
            'mobile'
        ]

    def create(self, validated_data):
        # user = User.objects.create_user(**validated_data)
        # return user
        # path 2
        # user = User.objects.create_user(
        #     firstName=validated_data['firstName'],
        #     lastName=validated_data['lastName'],
        #     email=validated_data['email'],
        #     mobile=validated_data['mobile'],
        # )
        # return user
        # path 1
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user
        # user = User(
        #     firstName=validated_data['firstName'],
        #     lastName=validated_data['lastName'],
        #     email=validated_data['email'],
        #     mobile=validated_data['mobile'],
        # )
        # user.set_password(validated_data['password'])
        # user.save()
