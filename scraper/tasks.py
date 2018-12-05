# from celery import Celery
# import csv
# from .models import Website
# from bs4 import BeautifulSoup
# import urllib.request
#
# app = Celery('tasks', broker='pyamqp://guest@localhost//')
#
# @app.task
# def scraper_alexa():
#     with open("top-1m.csv") as file:
#         reader = csv.reader(file)
#         for row in reader:
#             x = Website.objects.get_or_create(alexa_rank=row[0], url=row[1])
#     return True
#
# @app.task
# def scrapper_site():
#     all_websites = Website.objects.all()
#     for website in all_websites:
#         url = website.url
#         opener = urllib.request.build_opener()
#         opener.addheaders = [('User-agent', 'Mozilla/5.0')]
#         urllib.request.install_opener(opener)
#         html_page = urllib.request.urlopen(url).read()
#         soup = BeautifulSoup(html_page, 'html.parser')
#         for link in soup.find_all('a'):
#             print(link.get('href'))

# Create your tasks here
from __future__ import absolute_import, unicode_literals
from celery import shared_task
import csv
from .models import Website, WebPage
from bs4 import BeautifulSoup
from urllib import request as url_request
from urllib import error


@shared_task
def scraper_alexa():
    with open("scraper/top-1m.csv") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
            Website.objects.get_or_create(alexa_rank=row[0], url=row[1], category_id=1)
    return True


@shared_task
def scrapper_site(arg):
    if arg == "all":
        all_websites = Website.objects.all()
        for website in all_websites:
            url = "http://" + website.url
            opener = url_request.build_opener()
            opener.addheaders = [('User-agent', 'Mozilla/5.0')]
            url_request.install_opener(opener)
            try:
                html_page = url_request.urlopen(url).read()
                soup = BeautifulSoup(html_page, 'html.parser')
                for script in soup(["script", "style"]):
                    script.decompose()
                links = [a.get('href') for a in soup.find_all('a', href=True)]
                print(links)
            except error.URLError:
                print("Can't connect to site ", url)
            except:
                print("Unknown problem with site: ", url)
    elif isinstance(arg, int):
        website = Website.objects.get(id=arg)
        url = "http://" + website.url
        opener = url_request.build_opener()
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        url_request.install_opener(opener)
        try:
            html_page = url_request.urlopen(url).read()
            soup = BeautifulSoup(html_page, 'html.parser')
            links = [a.get('href') for a in soup.find_all('a', href=True)]
            print(links)
            links = list(set(links))  # remove duplicates
            for link in links:
                WebPage.objects.get_or_create(website=website, url=link, title=soup.title.string, meta_description="Dont have")
        except error.URLError:
            print("Can't connect to site ", url)
    else:
        return False
    # TODO Unique constrain on webpage.url make some calls end terribly wrong