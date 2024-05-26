from django.db import models


class Car(models.Model):
    model = models.CharField(max_length=200)
    year = models.IntegerField()
    make = models.CharField(max_length=100)
    IMEI = models.CharField(max_length=100)
    BODY_STYLE_CHOICES = [
        ("sedan", "Sedan"),
        ("coupe", "Coupe"),
        ("sports car", "Sports car"),
        ("station wagon", "Station wagon"),
        ("hatchback", "Hatchback"),
        ("convertible", "Convertible"),
        ("suv", "SUV"),
        ("minivan", "Minivan"),
        ("pickup truck", "Pickup truck"),
    ]
    LICENSE_CHOICES = [("provided", "Provided"), ("not provided", "Not Provided")]
    STATUS_CHOICES = [("ready", "Ready"), ("leased", "Leased"), ("repair", "In Repair")]
    body_style = models.CharField(
        max_length=20, choices=BODY_STYLE_CHOICES, default="sedan"
    )
    license = models.CharField(
        max_length=20, choices=LICENSE_CHOICES, default="provided"
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="ready")
    image = models.ImageField(upload_to="car_images/", null=True, blank=True)

    def __str__(self):
        return f"{self.make} ({self.model}) - ({self.IMEI})"
