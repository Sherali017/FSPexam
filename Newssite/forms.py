from django import forms

from Newssite.models import ContactModel


class ContactModelform(forms.Form):
    class Meta:
        model = ContactModel
        exclude  = ['created_at']