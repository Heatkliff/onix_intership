from rest_framework import serializers
from locations.models import Country, Symbol, User


class SymbolSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Symbol
        fields = ('image',)


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username',)


class CountrySerializer(serializers.HyperlinkedModelSerializer):
    flag = SymbolSerializer(read_only=True)
    users = UserSerializer(many=True, read_only=True)
    # flag = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Country
        fields = ('name', 'description', 'flag', 'population', 'cities_count', 'users')
