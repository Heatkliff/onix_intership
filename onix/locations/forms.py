from django import forms

from .models import Country, City, Symbol


class CountryForm(forms.ModelForm):
    class Meta:
        model = Country
        exclude = ['users', 'flag']


class SymbolForm(forms.ModelForm):
    class Meta:
        model = Symbol
        fields = '__all__'


class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = '__all__'
