from rest_framework import viewsets
from .serializers import CountrySerializer
from locations.models import Country


class CountryView(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer