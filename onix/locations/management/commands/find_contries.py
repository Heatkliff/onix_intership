from django.core.management.base import BaseCommand
from locations.models import Country
import re


class Command(BaseCommand):
    help = u'Get contries by regex'

    def add_arguments(self, parser):
        parser.add_argument('search', type=str, help=u'Word for find countries')

    def handle(self, *args, **kwargs):
        all_countries = Country.objects.all()
        search = kwargs['search']
        search_lower = str(search).lower()
        for country in all_countries:
            if re.search(rf"{search_lower}", str(country).lower()) is not None:
                self.stdout.write(str(country))
