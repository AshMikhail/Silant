from django.urls import include, path
from rest_framework.authtoken import views
from . import views

urlpatterns = [
    path('token/auth/', views.UserAuthToken.as_view()),
]
