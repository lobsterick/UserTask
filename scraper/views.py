from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *


class WebsiteListView(ListView):
    queryset = Website.objects.all()
    template_name = 'scraper/website_list.html'
    context_object_name = "website_list"
    paginate_by = 8


class WebsiteDetailView(DetailView):
    model = Website
