from rest_framework import serializers
from locations.models import Country, Symbol, User, City
from locations.validators import validate_image_url
from django.core import files
from . import additional


class SymbolSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Symbol
        fields = ('image',)


class UserSerializer(serializers.ModelSerializer):
    date_joined = serializers.ReadOnlyField()

    class Meta(object):
        model = User
        fields = ('id', 'email', 'first_name', 'last_name',
                  'date_joined', 'password')
        extra_kwargs = {'password': {'write_only': True}}


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ('id', 'name', 'country', 'longitude', 'latitude')

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name') if validated_data.get('name') is not None else instance.name
        instance.country = validated_data.get('country') if validated_data.get(
            'country') is not None else instance.country
        instance.longitude = validated_data.get('longitude') if validated_data.get(
            'longitude') is not None else instance.longitude
        instance.latitude = validated_data.get('latitude') if validated_data.get(
            'latitude') is not None else instance.latitude
        instance.save()
        return instance


class CountrySerializer(serializers.ModelSerializer):
    flag = SymbolSerializer(read_only=True)
    users = UserSerializer(many=True, read_only=True)
    cities = CitySerializer(many=True, read_only=True)

    class Meta:
        model = Country
        fields = '__all__'

    def create(self, validated_data):
        request_data = self.context.get("request").data
        flag_url = validate_image_url(request_data.get("flag_url"))
        image = additional.image_load(flag_url)
        flag = Symbol()
        flag.image.save(image['name'], files.File(image['file']))
        country = Country.objects.create(flag=flag, **validated_data)
        return country

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name') if validated_data.get('name') is not None else instance.name
        instance.description = validated_data.get('description') if validated_data.get(
            'description') is not None else instance.description
        instance.population = validated_data.get('population') if validated_data.get(
            'population') is not None else instance.population
        instance.cities_count = validated_data.get('cities_count') if validated_data.get(
            'cities_count') is not None else instance.cities_count
        instance.save()
        return instance


class SchemaCountrySerializer(serializers.ModelSerializer):
    flag_url = serializers.CharField(min_length=10)

    class Meta:
        model = Country
        fields = ('name', 'description', 'population', 'cities_count', 'flag_url')
