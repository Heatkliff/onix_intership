from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save, post_save, pre_delete, post_delete, post_init
from django.dispatch import receiver


class Symbol(models.Model):
    image = models.ImageField(null=False, blank=False)

    def __str__(self):
        return f"{self.image}"


class Country(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(null=True)
    population = models.IntegerField(default=0)
    flag = models.OneToOneField(Symbol, on_delete=models.CASCADE, related_name='symbol')
    cities_count = models.IntegerField(default=0)
    users = models.ManyToManyField(User, related_name="users")

    class Meta:
        verbose_name_plural = "Countries"

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    longitude = models.FloatField(null=False)
    latitude = models.FloatField(null=False)

    class Meta:
        verbose_name_plural = "Cities"

    def __str__(self):
        return self.name


@receiver(pre_save, sender=City)
def pre_save_city(instance, **kwargs):
    print(f"[INFO] City {instance} wil be added")


@receiver(post_save, sender=City)
def post_save_city(instance, **kwargs):
    instance.country.cities_count += 1
    instance.country.save()


@receiver(pre_delete, sender=City)
def pre_delete_city(instance, **kwargs):
    instance.country.cities_count -= 1
    instance.country.save()


@receiver(post_delete, sender=City)
def post_delete_city(instance, **kwargs):
    print(f"[INFO] City {instance} was deleted")
