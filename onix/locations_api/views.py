from locations.models import Country, City, User
from .serializers import CountrySerializer, CitySerializer, UserSerializer, SchemaCountrySerializer
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from django.contrib.auth.hashers import make_password
from django.contrib.auth.base_user import BaseUserManager
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.utils import json
from locations_api.tasks import country_created, country_updated

import requests
import django_filters.rest_framework


class CountryApiView(RetrieveUpdateDestroyAPIView):
    serializer_class = CountrySerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    queryset = Country.objects.all()
    # permission_classes = (IsAuthenticated,)

    def get_queryset(self, country_id):
        try:
            country = get_object_or_404(Country, id=country_id)
        except Country.DoesNotExist:
            content = {
                'status': 'Not Found'
            }
            return Response(content, status=status.HTTP_404_NOT_FOUND)
        return country

    def get(self, request, country_id):
        country = self.get_queryset(country_id)
        serializer = CountrySerializer(country)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        request_body=SchemaCountrySerializer,
        responses={
            201: CountrySerializer(many=True),
        }
    )
    def put(self, request, country_id):
        country = self.get_queryset(country_id)
        serializer = CountrySerializer(country, data=request.data)
        if serializer.is_valid():
            serializer.save()
            task = country_updated.delay(request.user.email, country.name, str(request.get_host()) + str(request.path))
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        request_body=SchemaCountrySerializer,
        responses={
            201: CountrySerializer(many=True),
        }
    )
    def patch(self, request, country_id):
        country = self.get_queryset(country_id)
        serializer = CountrySerializer(country, data=request.data)
        if serializer.is_valid():
            serializer.save()
            task = country_updated.delay(request.user.email, country.name, str(request.get_host()) + str(request.path))
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, country_id):
        country = self.get_queryset(country_id)
        country.delete()
        content = {
            'status': 'NO CONTENT'
        }
        return Response(content, status=status.HTTP_204_NO_CONTENT)


class CountriesApiView(ListCreateAPIView):
    serializer_class = CountrySerializer
    queryset = Country.objects.all()
    permission_classes = (IsAuthenticated,)
    authentication_classes = [SessionAuthentication, BasicAuthentication]

    def get_queryset(self):
        country = Country.objects.all()
        return country

    def get(self, request):
        country = self.get_queryset()
        serializer = self.serializer_class(country, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        request_body=SchemaCountrySerializer,
        responses={
            201: CountrySerializer(many=True),
        }
    )
    def post(self, request):
        serializer = CountrySerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            task = country_created.delay(request.user.email)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CityViewSet(ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    queryset = City.objects.all()
    serializer_class = CitySerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['country_id']
    permission_classes = (IsAuthenticated,)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        content = {
            'status': 'NO CONTENT'
        }
        return Response(content, status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.delete()


class CreateUserAPIView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        user = request.data
        serializer = UserSerializer(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class GoogleView(APIView):
    def post(self, request):
        payload = {'access_token': request.data.get("token")}  # validate the token
        r = requests.get('https://www.googleapis.com/oauth2/v2/userinfo', params=payload)
        data = json.loads(r.text)

        if 'error' in data:
            content = {'message': 'wrong google token / this google token is already expired.'}
            return Response(content)

        # create user if not exist
        try:
            user = User.objects.get(email=data['email'])
        except User.DoesNotExist:
            user = User()
            user.username = data['email']
            # provider random default password
            user.password = make_password(BaseUserManager().make_random_password())
            user.email = data['email']
            user.save()

        token = RefreshToken.for_user(user)  # generate token without username & password
        response = {}
        response['username'] = user.username
        response['access_token'] = str(token.access_token)
        response['refresh_token'] = str(token)
        return Response(response)
