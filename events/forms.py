from django import forms
from .models import ArtistApplication


class ArtistApplicationForm(forms.ModelForm):
    class Meta:
        model = ArtistApplication

        fields = [
            "event",
            "name",
            "email",
            "instagram_contact",
            "phone",
            "art_form",
            "contribution_title",
            "description",
            "duration_minutes",
            "technical_needs",
            "consent_privacy",
        ]

        widgets = {
            "name": forms.TextInput(attrs={
                "placeholder": "z. B. Max Mustermann / Künstler:innenname"
            }),
            "email": forms.EmailInput(attrs={
                "placeholder": "deine-mail@example.de"
            }),
            "instagram_contact": forms.TextInput(attrs={
                "placeholder": "@deinaccount"
            }),
            "phone": forms.TextInput(attrs={
                "placeholder": "optional"
            }),
            "art_form": forms.TextInput(attrs={
                "placeholder": "z. B. Musik, Lesung, Performance, Fotografie"
            }),
            "contribution_title": forms.TextInput(attrs={
                "placeholder": "optional"
            }),
            "description": forms.Textarea(attrs={
                "rows": 5,
                "placeholder": "Beschreibe kurz, was du zeigen, spielen, lesen oder ausstellen möchtest."
            }),
            "duration_minutes": forms.NumberInput(attrs={
                "placeholder": "z. B. 10",
                "min": "1"
            }),
            "technical_needs": forms.Textarea(attrs={
                "rows": 4,
                "placeholder": "z. B. Mikrofon, Beamer, Strom, Aufbauzeit, Stellfläche ..."
            }),
            "consent_privacy": forms.CheckboxInput(),
        }

        labels = {
            "event": "Für welchen Termin möchtest du dich anmelden?",
            "name": "Name / Künstler:innenname",
            "email": "E-Mail-Adresse",
            "instagram_contact": "Instagram-Kontakt",
            "phone": "Telefonnummer",
            "art_form": "Kunstform",
            "contribution_title": "Titel des Beitrags",
            "description": "Beschreibung deines Beitrags",
            "duration_minutes": "Dauer in Minuten",
            "technical_needs": "Technische Anforderungen",
            "consent_privacy": "Ich stimme zu, dass meine Angaben zur Bearbeitung meiner Anmeldung gespeichert und zur Kontaktaufnahme verwendet werden.",
        }