
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
