from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.http import HttpResponse
from locations.models import Country, City, Symbol
from .forms import CountryForm, CityForm, SymbolForm


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
    content = {
        'country': country,
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


@login_required
def create_country(request):
    if request.method == "POST":
        form = CountryForm(request.POST, request.FILES)
        if form.is_valid():
            flag = Symbol.objects.create(image=request.POST['image'])
            country = form.save(commit=False)
            country.flag = flag
            country.save()
            return redirect('single_country', country_id=country.id)
        else:
            flag_form = SymbolForm()
    else:
        form = CountryForm()
        flag_form = SymbolForm()
    return render(request, 'locations/create_country.html', {'form': form, 'flag_form': flag_form})


@login_required
def update_country(request, country_id):
    country = get_object_or_404(Country, id=country_id)
    if request.method == "POST":
        form = CountryForm(request.POST, request.FILES, instance=country)
        if form.is_valid():
            flag = Symbol.objects.create(image=request.POST['image'])
            country = form.save(commit=False)
            country.flag = flag
            country.save()
            return redirect('single_country', country_id=country.id)
        else:
            flag_form = SymbolForm(instance=country.flag)
    else:
        form = CountryForm(instance=country)
        flag_form = SymbolForm(instance=country.flag)
    return render(request, 'locations/create_country.html', {'form': form, 'flag_form': flag_form})


@login_required
def create_city(request):
    if request.method == "POST":
        form = CityForm(request.POST)
        if form.is_valid():
            city = form.save()
            return redirect('single_city', city_id=city.id)
    else:
        form = CityForm()
    return render(request, 'locations/create_city.html', {'form': form})


@login_required
def update_city(request, city_id):
    city = get_object_or_404(City, id=city_id)
    if request.method == "POST":
        form = CityForm(request.POST, instance=city)
        if form.is_valid():
            city = form.save()
            return redirect('single_city', city_id=city.id)
    else:
        form = CityForm(instance=city)
    return render(request, 'locations/create_city.html', {'form': form})
