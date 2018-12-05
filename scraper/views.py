from django.views.generic import ListView, DetailView, CreateView
from .forms import *
from django.urls import reverse_lazy
from .tasks import *
from django.http import HttpResponse



class WebsiteListView(ListView):
    context_object_name = "website_list"
    paginate_by = 100

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

    def post(self, request, pk):
        print(pk)
        scrapper_site.delay(pk)
        return HttpResponse(f"Scrap task for id {pk} was send to Celery!")



class WebsiteCreateView(CreateView):
    template_name = "scraper/website_form.html"
    form_class = WebsiteModelForm


class WebsiteCategoryListView(ListView):
    template_name = "scraper/category_list.html"
    context_object_name = "category_list"
    queryset = WebsiteCategory.objects.all().order_by("id")
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(WebsiteCategoryListView, self).get_context_data(**kwargs)
        context['counter'] = WebsiteCategory.objects.all().count()
        return context


class WebsiteCategoryCreateView(CreateView):
    template_name = "scraper/category_form.html"
    form_class = WebsiteCategoryModelForm
    success_url = reverse_lazy("WebsiteCategoryListView")
