from django.urls import path , include
from books import views
urlpatterns = [
    path("",views.home ,name='home'),
    path("doctor",views.doctor,name="doctor"),
    path("about",views.about,name="about"),
    path("contact",views.contact,name="contact"),
    path("testimonial",views.testimonial,name="testimonial"),
    path("treatment",views.treatment,name="treatment"),

]

