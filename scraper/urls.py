from django.urls import path
from .views import WebsiteDetailView, WebsiteListView, WebsiteCreateView

urlpatterns = [
    path("websites/", WebsiteListView.as_view(), name="WebsiteListView"),
    path("websites/<int:pk>", WebsiteDetailView.as_view(), name="WebsiteDetailView"),
    path("websites/create", WebsiteCreateView.as_view(), name="WebsiteCreateView")
]
