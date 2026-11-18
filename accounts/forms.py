from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ("username", "email", "first_name", "last_name", "household_name")
        labels = {
            "first_name": "First name",
            "last_name": "Last name",
            "household_name": "Household name (optional)",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        hints = {
            "username": ("Choose a username", "username"),
            "email": ("you@example.com", "email"),
            "first_name": ("Juan", "given-name"),
            "last_name": ("Dela Cruz", "family-name"),
            "household_name": ("e.g. Dela Cruz family", "organization"),
            "password1": ("Create a password", "new-password"),
            "password2": ("Type it again", "new-password"),
        }
        for name, field in self.fields.items():
            placeholder, autocomplete = hints[name]
            field.widget.attrs.update(
                {
                    "class": "field-input",
                    "placeholder": placeholder,
                    "autocomplete": autocomplete,
                }
            )
        self.fields["first_name"].required = True
        self.fields["last_name"].required = True
        self.fields["password2"].label = "Confirm password"
        self.fields["password2"].help_text = ""

    def clean_email(self):
        email = self.cleaned_data["email"].strip().lower()
        if CustomUser.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError("An account with this email already exists.")
        return email