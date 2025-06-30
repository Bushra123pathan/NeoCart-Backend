from django.urls import path
from .views import RegisterView

#register/login api's here

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
]
