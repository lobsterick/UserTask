from django import forms
from .models import Website, WebsiteCategory


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


class WebsiteCategoryModelForm(forms.ModelForm):
    class Meta:
        model = WebsiteCategory
        fields = [
            "name",
            "description",
        ]
