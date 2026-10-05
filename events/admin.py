from django.contrib import admin
from .models import Event, ArtistApplication, GalleryAlbum, GalleryImage


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

    readonly_fields = ("created_at",)


class GalleryImageInline(admin.StackedInline):
    model = GalleryImage
    extra = 3
    can_delete = True
    show_change_link = True
    fields = ("image", "video", "title", "description", "is_published")


@admin.register(GalleryAlbum)
class GalleryAlbumAdmin(admin.ModelAdmin):
    list_display = ("title", "date", "is_published", "created_at")
    list_filter = ("is_published", "date", "created_at")
    search_fields = ("title", "description")
    inlines = [GalleryImageInline]


@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ("title", "album", "is_published", "created_at")
    list_filter = ("is_published", "album", "created_at")
    search_fields = ("title", "description", "album__title")
    fields = ("album", "image", "video", "title", "description", "is_published")