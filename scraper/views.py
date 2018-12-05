from django.views.generic import ListView, DetailView
from .models import *


class WebsiteListView(ListView):
    queryset = Website.objects.all()
    template_name = 'scraper/website_list.html'
    context_object_name = "website_list"
    paginate_by = 8

    def get_ordering(self):
        ordering = self.request.GET.get('order_by', 'id')
        return ordering


class WebsiteDetailView(DetailView):
    model = Website
