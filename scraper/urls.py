from django.urls import path
from .views import WebsiteDetailView, WebsiteListView, WebsiteCreateView, WebsiteCategoryListView

urlpatterns = [
    path("websites/", WebsiteListView.as_view(), name="WebsiteListView"),
    path("websites/<int:pk>", WebsiteDetailView.as_view(), name="WebsiteDetailView"),
    path("websites/create", WebsiteCreateView.as_view(), name="WebsiteCreateView"),
    path("categories/", WebsiteCategoryListView.as_view(), name="WebsiteCategoryListView")
]
