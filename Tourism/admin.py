from django.contrib import admin
from .models import Packages,Destination,Tour_guides,Testimonial

# Register your models here.

admin.site.register(Packages)
admin.site.register(Destination)
admin.site.register(Tour_guides)
admin.site.register(Testimonial)
