from django.db import models

# Create your models here.
class Property(models.Model):
    address = models.CharField(max_length=200, unique=True)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    lat = models.FloatField()
    lng = models.FloatField()

    def __str__(self):
        return self.address
