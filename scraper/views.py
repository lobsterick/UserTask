from django.views.generic import ListView, DetailView
from .models import *


class WebsiteListView(ListView):
    # queryset = Website.objects.all()
    template_name = 'scraper/website_list.html'
    context_object_name = "website_list"
    paginate_by = 2

    # #working
    # def get_ordering(self):
    #     ordering = self.request.GET.get('order_by', 'id')
    #     return ordering

    def get_queryset(self):
        if self.request.GET.get('category'):
            filter_val = self.request.GET.get('category')
            order = self.request.GET.get('order_by', 'id')
            new_context = Website.objects.filter(
                category__name=filter_val,
                ).order_by(order)
            return new_context
        else:
            order = self.request.GET.get('order_by', 'id')
            new_context = Website.objects.all().order_by(order)
            return new_context

    def get_context_data(self, **kwargs):
        context = super(WebsiteListView, self).get_context_data(**kwargs)
        context['category'] = self.request.GET.get('category')
        context['order_by'] = self.request.GET.get('order_by', 'id')
        context['categories'] = WebsiteCategory.objects.all()
        return context


class WebsiteDetailView(DetailView):
    model = Website
