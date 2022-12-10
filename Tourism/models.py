from django.db import models

# Create your models here.

class Packages(models.Model):
    country = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="img")
    price = models.DecimalField(decimal_places=2,max_digits=9)

    def __str__(self):
        return self.country

class Destination(models.Model):
    countries = models.CharField(max_length=100)
    images = models.ImageField(upload_to="imgs")
    def __str__(self):
        return self.countries

class Tour_guides(models.Model):
    name = models.CharField(max_length=100)
    title = models.TextField()
    images1 = models.ImageField(upload_to="im")

    def __str__(self):
        return self.name

class Testimonial(models.Model):
    images2 = models.ImageField(upload_to="ib")
    testimony = models.TextField()
    name = models.CharField(max_length=100)
    occupation = models.TextField()
    
    def __str__(self):
        return self.name





