from django.shortcuts import render, redirect
from django.db.models import Prefetch, Q

from .models import Event, GalleryAlbum, GalleryImage
from .forms import ArtistApplicationForm


def home(request):
    return render(request, "home.html")


def event_list(request):
    events = Event.objects.all().order_by("date")
    return render(request, "events.html", {"events": events})


def galerie(request):
    published_media = (
        GalleryImage.objects
        .filter(is_published=True)
        .filter(Q(image__isnull=False) | Q(video__isnull=False))
        .exclude(image="", video="")
        .order_by("created_at")
    )

    albums = (
        GalleryAlbum.objects
        .filter(is_published=True)
        .prefetch_related(Prefetch("images", queryset=published_media))
        .order_by("-date", "-created_at")
    )

    return render(request, "galerie.html", {"albums": albums})


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


def impressum(request):
    return render(request, "impressum.html")