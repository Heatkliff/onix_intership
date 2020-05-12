from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.http import HttpResponse
from locations.models import Country, City


@login_required
def index(request, template="locations/country_list.html"):
    countries_list = Country.objects.all()
    content = {
        'countries': countries_list,
    }
    return render(request, template, content)


@login_required
def single_country(request, country_id, template="locations/country.html"):
    country = get_object_or_404(Country, id=country_id)
    cities_list = City.objects.filter(country=country)
    content = {
        'country': country,
        'cities': cities_list
    }
    return render(request, template, content)


@login_required
def single_city(request, city_id, template="locations/city.html"):
    city = get_object_or_404(City, id=city_id)
    content = {
        'city': city,
    }
    return render(request, template, content)


@login_required
def delete_city(request, city_id):
    city = get_object_or_404(City, id=city_id)
    city.delete()
    return redirect(f'/locations/country/{city.country.id}')
