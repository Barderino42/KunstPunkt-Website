from django.shortcuts import render, redirect
from .models import Event
from .forms import ArtistApplicationForm


def home(request):
    return render(request, "home.html")


def event_list(request):
    events = Event.objects.all().order_by("date")
    return render(request, "events.html", {"events": events})


def galerie(request):
    return render(request, "galerie.html")


def application_create(request):
    if request.method == "POST":
        form = ArtistApplicationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("application_success")
    else:
        form = ArtistApplicationForm()

    return render(request, "application_form.html", {"form": form})


def application_success(request):
    return render(request, "application_success.html")