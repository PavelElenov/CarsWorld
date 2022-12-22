from django.db import models


class Cars(models.Model):
    img = models.ImageField(
        upload_to="cars_images"
    )
    brand = models.CharField(
        max_length=30,
    )
    model = models.CharField(
        max_length=30,
    )
    engine_type = models.CharField(
        max_length=30,
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )

    def __str__(self):
        return f"{self.brand} {self.model}"


class Accessories(models.Model):
    img = models.ImageField(
        upload_to="accessories"
    )
    name = models.CharField(
        max_length=30,
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )

    def __str__(self):
        return f"{self.name}"


class Profile(models.Model):
    first_name = models.CharField(
        max_length=30,
    )
    last_name = models.CharField(
        max_length=30,
    )
    email = models.EmailField()
    password = models.CharField(
        max_length=30,
    )
    favourite_cars = models.ManyToManyField(
        Cars,
        blank=True,
    )
    favourite_accessories = models.ManyToManyField(
        Accessories,
        blank=True,
    )
    logged = models.BooleanField(
        default=False,
    )
    img = models.ImageField(
        upload_to='profile_image',
        blank=True,
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


