from celery import Celery
import csv
from .models import Website
from bs4 import BeautifulSoup
import urllib.request

app = Celery('tasks', broker='pyamqp://guest@localhost//')

@app.task
def scraper_alexa():
    with open("top-1m.csv") as file:
        reader = csv.reader(file)
        for row in reader:
            x = Website.objects.get_or_create(alexa_rank=row[0], url=row[1])
    return True

@app.task
def scrapper_site():
    all_websites = Website.objects.all()
    for website in all_websites:
        url = website.url
        opener = urllib.request.build_opener()
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        urllib.request.install_opener(opener)
        html_page = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(html_page, 'html.parser')
        for link in soup.find_all('a'):
            print(link.get('href'))
