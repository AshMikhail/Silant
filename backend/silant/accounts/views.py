from rest_framework import viewsets, status, permissions
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.views import APIView

from . import models
from . import Serializers


class UserAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        queryset = models.baseCompany.objects.get(user=user.pk)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'user_name': user.username,
            'сategory': queryset.сategory,
            'company_id': queryset.id,
            'company_name': queryset.name

        })

class baseCompanyViewset(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]

    queryset = models.baseCompany.objects.all()
    serializer_class = Serializers.baseCompanySerializer


class clientViewset(viewsets.ModelViewSet):
    queryset = models.client.objects.all()
    serializer_class = Serializers.clientSerializer

class service_companyViewset(viewsets.ModelViewSet):
    queryset = models.service_company.objects.all()
    serializer_class = Serializers.serviceCompanySerializer