
from django.urls import path
from users.views import UserRegistrationView
urlpatterns = [
    path('user-registration', UserRegistrationView.as_view(),
         name='user-registration')
]
