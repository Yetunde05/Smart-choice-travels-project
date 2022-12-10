from django.urls import path
from .views import home_page,blog,about,contact,destination,guide,package,service,single,testimonial

urlpatterns = [
    path("", home_page, name="home"),
    path("about/", about, name="about"),
    path("blog/", blog, name="blog"),
    path("contact/", contact, name="contact"),
    path("destination/", destination, name="destination"),
    path("guide/", guide, name="guide"),
    path("package/", package, name="package"),
    path("service/", service, name="service"),
    path("single/", single, name="single"),
    path("testimonial/", testimonial, name="testimonial")
]