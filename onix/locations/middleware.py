from django.utils.deprecation import MiddlewareMixin

from locations.models import Country


class CountryMiddleware(MiddlewareMixin):
    def process_request(self, request):
        country = Country.objects.all()
        request.countries_list = country
