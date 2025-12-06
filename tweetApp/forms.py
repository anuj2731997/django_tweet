from django import forms
from .models import Tweet
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User


class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ["text", "image"]
        widgets = {
            "text": forms.Textarea(
                attrs={
                    "rows": 4,
                    "placeholder": "What's happening?",
                    "class": (
                        "w-full p-3 rounded-xl border border-gray-300 "
                        "focus:ring-2 focus:ring-blue-500 focus:border-blue-500 "
                        "bg-white text-gray-800 resize-none"
                    ),
                }
            ),
            "image": forms.ClearableFileInput(
                attrs={
                    "class": (
                        "mt-3 block w-full text-sm text-gray-700 "
                        "file:mr-4 file:py-2 file:px-4 "
                        "file:rounded-lg file:border-0 "
                        "file:bg-blue-600 file:text-white "
                        "hover:file:bg-blue-700"
                    )
                }
            ),
        }


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(
            attrs={
                "placeholder": "you@example.com",
                "autocomplete": "email",
            }
        ),
    )

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # common Tailwind input classes
        input_classes = (
            "mt-1 block w-full px-3 py-2 border border-gray-500 rounded-lg"
            "focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 bg-white text-gray-900"
        )

        # apply classes and placeholders to all visible fields
        for name, field in self.fields.items():
            # set a friendly placeholder if none provided
            if not field.widget.attrs.get("placeholder"):
                field.widget.attrs["placeholder"] = field.label

            # merge classes (preserve any pre-existing classes)
            existing = field.widget.attrs.get("class", "")
            field.widget.attrs["class"] = (existing + " " + input_classes).strip()

            # accessibility / autocomplete hints
            if name == "username":
                field.widget.attrs["autocomplete"] = "username"
            elif name == "password1":
                field.widget.attrs["autocomplete"] = "new-password"
            elif name == "password2":
                field.widget.attrs["autocomplete"] = "new-password"
            elif name == "email":
                field.widget.attrs["autocomplete"] = "email"


class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "autocomplete": "username",
                "class": (
                    "mt-1 block w-full px-3 py-2 border border-gray-500 rounded-lg"
                    "focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 bg-white text-gray-900"
                ),
            }
        ),
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "autocomplete": "current-password",
                "class": (
                    "mt-1 block w-full px-3 py-2 border border-gray-500 rounded-lg"
                    "focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 bg-white text-gray-900"
                ),
            }
        ),
    )


class LogoutForm(forms.Form):
    pass
    # No fields needed for logout form
