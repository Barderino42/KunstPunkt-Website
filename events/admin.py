from django.contrib import admin
from .models import Event, ArtistApplication, GalleryImage


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("title", "date", "location")
    search_fields = ("title", "location", "description")
    list_filter = ("date",)


@admin.register(ArtistApplication)
class ArtistApplicationAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "event",
        "art_form",
        "instagram_contact",
        "duration_minutes",
        "status",
        "created_at",
    )

    list_filter = (
        "status",
        "event",
        "art_form",
        "created_at",
    )

    search_fields = (
        "name",
        "email",
        "instagram_contact",
        "art_form",
        "description",
        "technical_needs",
    )

    readonly_fields = (
        "created_at",
    )

@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ("title", "is_published", "created_at")
    list_filter = ("is_published", "created_at")
    search_fields = ("title", "description")