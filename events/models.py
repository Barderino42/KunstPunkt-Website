from django.db import models
from django.utils import timezone


class Event(models.Model):
    title = models.CharField(max_length=200, verbose_name="Titel")
    date = models.DateField(verbose_name="Datum")
    location = models.CharField(max_length=200, verbose_name="Ort")
    description = models.TextField(verbose_name="Beschreibung")

    def __str__(self):
        return f"{self.title} – {self.date}"


class ArtistApplication(models.Model):
    STATUS_CHOICES = [
        ("new", "Neu"),
        ("contacted", "Kontaktiert"),
        ("accepted", "Angenommen"),
        ("waitlist", "Warteliste"),
        ("rejected", "Abgelehnt"),
    ]

    event = models.ForeignKey(Event, on_delete=models.CASCADE, verbose_name="Gewünschter Termin")
    name = models.CharField(max_length=200, verbose_name="Name / Künstler:innenname")
    email = models.EmailField(verbose_name="E-Mail-Adresse")
    instagram_contact = models.CharField(max_length=100, blank=True, default="", verbose_name="Instagram-Kontakt")
    phone = models.CharField(max_length=100, blank=True, default="", verbose_name="Telefonnummer optional")
    art_form = models.CharField(max_length=200, verbose_name="Kunstform")
    contribution_title = models.CharField(max_length=200, blank=True, default="", verbose_name="Titel des Beitrags optional")
    description = models.TextField(verbose_name="Kurze Beschreibung des Beitrags")
    duration_minutes = models.PositiveIntegerField(default=10, verbose_name="Dauer in Minuten")
    technical_needs = models.TextField(blank=True, default="", verbose_name="Technische Anforderungen")
    portfolio_link = models.URLField(blank=True, default="", verbose_name="Link zu Portfolio / Website / Soundcloud optional")
    consent_privacy = models.BooleanField(default=False, verbose_name="Ich stimme der Speicherung meiner Angaben zur Bearbeitung der Anmeldung zu.")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="new", verbose_name="Status")
    internal_notes = models.TextField(blank=True, default="", verbose_name="Interne Notizen")
    created_at = models.DateTimeField(default=timezone.now, verbose_name="Eingegangen am")

    def __str__(self):
        return f"{self.name} – {self.event}"


class GalleryAlbum(models.Model):
    title = models.CharField(max_length=200, verbose_name="Titel")
    event = models.ForeignKey(Event, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Zugehöriger Termin")
    description = models.TextField(blank=True, default="", verbose_name="Beschreibung")
    date = models.DateField(null=True, blank=True, verbose_name="Datum")
    is_published = models.BooleanField(default=True, verbose_name="Veröffentlicht")
    created_at = models.DateTimeField(default=timezone.now, verbose_name="Erstellt am")

    def __str__(self):
        return self.title


class GalleryImage(models.Model):
    album = models.ForeignKey(GalleryAlbum, on_delete=models.CASCADE, related_name="images", null=True, blank=True, verbose_name="Album")
    title = models.CharField(max_length=200, blank=True, default="", verbose_name="Titel")
    description = models.TextField(blank=True, default="", verbose_name="Beschreibung")
    image = models.ImageField(upload_to="gallery/images/", verbose_name="Bild", blank=True, null=True)
    video = models.FileField(upload_to="gallery/videos/", verbose_name="Video", blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now, verbose_name="Erstellt am")
    is_published = models.BooleanField(default=True, verbose_name="Veröffentlicht")

    def __str__(self):
        if self.title:
            return self.title
        if self.album:
            return f"Medien aus {self.album.title}"
        return "Galerie-Medium"
