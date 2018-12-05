from django import forms
from .models import Website


class WebsiteModelForm(forms.ModelForm):
    class Meta:
        model = Website
        fields = [
            "url",
            "title",
            "meta_description",
            "alexa_rank",
            "category"
        ]