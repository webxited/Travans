from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name="cafeapp"),
    path('about/',views.about, name="about"),
    path('services/',views.services, name="services"),
    path('menu/',views.menu, name="menu"),
    path('testimonials/', views.testimonials, name="testimonials"),
    path('gallery/',views.gallery, name="gallery"),
]