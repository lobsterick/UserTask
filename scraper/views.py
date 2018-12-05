from django.views.generic import ListView, DetailView
from .models import *


class WebsiteListView(ListView):
    # queryset = Website.objects.all()
    template_name = 'scraper/website_list.html'
    context_object_name = "website_list"
    paginate_by = 8

    # #working
    # def get_ordering(self):
    #     ordering = self.request.GET.get('order_by', 'id')
    #     return ordering

    def get_queryset(self):
        if self.request.GET.get('filter'):
            filter_val = self.request.GET.get('filter')
            order = self.request.GET.get('order_by', 'id')
            new_context = Website.objects.filter(
                category=filter_val,
                ).order_by(order)
            return new_context
        else:
            order = self.request.GET.get('order_by', 'id')
            new_context = Website.objects.all().order_by(order)
            return new_context

    def get_context_data(self, **kwargs):
        context = super(WebsiteListView, self).get_context_data(**kwargs)
        context['filter'] = self.request.GET.get('filter')
        context['order_by'] = self.request.GET.get('order_by', 'id')
        return context


class WebsiteDetailView(DetailView):
    model = Website
