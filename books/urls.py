from django.urls import path 
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
    path('search',views.search,name='search'),
    path('readMore/<int:b_id>' , views.readMore , name='readMore'),
    path('delete/<int:b_id>' , views.delete , name='delete'),
    path('login/', views.sign_in, name='login'),
    path('project', views.project, name='project'),

]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
