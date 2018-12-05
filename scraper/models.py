from django.db import models
from django.urls import reverse

class WebsiteCategory(models.Model):
    name = models.CharField(max_length=1000)
    description = models.CharField(max_length=10000)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    count = models.IntegerField()

    def __str__(self):
        return self.name

class Website(models.Model):
    url = models.CharField(max_length=1000)
    title = models.CharField(max_length=1000)
    meta_description = models.CharField(max_length=1000)
    alexa_rank = models.IntegerField()
    category = models.ForeignKey(WebsiteCategory, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("WebsiteDetailView", kwargs={"pk": self.id})


class WebPage(models.Model):
    website = models.ForeignKey(Website, on_delete=models.CASCADE)
    url = models.CharField(max_length=1000, unique=True)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=1000)
    meta_description = models.CharField(max_length=10000)

    def __str__(self):
        return self.website
