from django.urls import path
from FitnessFreaks import views

urlpatterns = [
    path('',views.Home,name="Home"),
    path('about',views.about,name="about"),
    path('services',views.services,name="services"),
    path('contact',views.contact,name="contact"),
    path('enroll',views.enroll,name="enroll"),
    path('signup',views.signup,name="signup"),
    path('login',views.handlelogin,name="handlelogin"),
    path('logout',views.handleLogout,name="handleLogout"),
    path('gallery',views.gallery,name="gallery"),
]
