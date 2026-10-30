from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    country = models.CharField(max_length=100, blank=True, default="")
    founded_year = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name


class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE, related_name="models")
    dealer_id = models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=100)

    SEDAN = "Sedan"
    SUV = "SUV"
    WAGON = "Wagon"
    HATCHBACK = "Hatchback"
    COUPE = "Coupe"
    CAR_TYPES = [
        (SEDAN, "Sedan"),
        (SUV, "SUV"),
        (WAGON, "Wagon"),
        (HATCHBACK, "Hatchback"),
        (COUPE, "Coupe"),
    ]
    type = models.CharField(max_length=20, choices=CAR_TYPES, default=SUV)
    year = models.IntegerField(
        default=2023,
        validators=[MaxValueValidator(2023), MinValueValidator(2015)]
    )

    def __str__(self):
        return f"{self.car_make.name} {self.name}"


class DealerReview(models.Model):
    dealer_id = models.IntegerField()
    dealership = models.CharField(max_length=200)
    name = models.CharField(max_length=100)
    purchase = models.BooleanField(default=False)
    review = models.TextField()
    purchase_date = models.CharField(max_length=20)
    car_make = models.CharField(max_length=100)
    car_model = models.CharField(max_length=100)
    car_year = models.IntegerField()
    sentiment = models.CharField(max_length=20, default="Positive")

    def __str__(self):
        return self.review


class Dealer(models.Model):
    city = models.CharField(max_length=100, default="")
    state = models.CharField(max_length=100)
    st = models.CharField(max_length=10, default="")
    address = models.CharField(max_length=200)
    zip = models.CharField(max_length=20)
    latitude = models.FloatField(default=0.0)
    longitude = models.FloatField(default=0.0)
    short_name = models.CharField(max_length=100)
    full_name = models.CharField(max_length=200)

    def __str__(self):
        return self.full_name