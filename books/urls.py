from django.urls import path , include
from books import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path("",views.home ,name='home'),
    path("doctor",views.doctor,name="doctor"),
    path("about",views.about,name="about"),
    path("contact",views.contact,name="contact"),
    path("testimonial",views.testimonial,name="testimonial"),
    path("treatment",views.treatment,name="treatment"),

]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
