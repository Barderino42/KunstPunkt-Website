from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("events/", views.event_list, name="event_list"),
    path("galerie/", views.galerie, name="galerie"),
    path("anmeldung/", views.application_create, name="application_create"),
    path("anmeldung/erfolgreich/", views.application_success, name="application_success"),
    path("impressum/", views.impressum, name="impressum"),
]