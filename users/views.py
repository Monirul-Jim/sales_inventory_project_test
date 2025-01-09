from django.shortcuts import render
from rest_framework.views import APIView
from users.serializers import UserRegistrationSerializers
from rest_framework.response import Response
from rest_framework import status
# Create your views here.


class UserRegistrationView(APIView):
    def post(self, request):
        serializer = UserRegistrationSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {'status': 'success', 'message': 'User Registration Successfully'},
                status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
