from django.shortcuts import render
from .models import Packages,Destination,Tour_guides,Testimonial

# Create your views here.

def home_page(request):
    package = Packages.objects.all()
    destination = Destination.objects.all()
    tour_guide = Tour_guides.objects.all()
    testimonial = Testimonial.objects.all()
    context = {
        "packages": package,
        "destinations" : destination,
        "tour_guides": tour_guide,
        "testimonials": testimonial
    }
    return render(request, "Tourism/index.html", context)


def about(request):
    return render(request, "Tourism/about.html")

def blog(request):
    return render(request, "Tourism/blog.html")

def contact(request):
    return render(request, "Tourism/contact.html")

def destination(request):
    return render(request, "Tourism/destination.html")

def guide(request):
    return render(request, "Tourism/guide.html")

def package(request):
    return render(request, "Tourism/package.html")

def service(request):
    return render(request, "Tourism/service.html")

def single(request):
    return render(request, "Tourism/single.html")
def testimonial(request):
    return render(request, "Tourism/testimonial.html")


