# Simple Crawler
Simple implementation of web crawler in Django Framework. Because ... why not?

## What's  inside?
Inside this project, you will find a Django Web Application, containing webscraper operating on 1.000.000 most popular pages, according to [Alexa](https://www.alexa.com/).
Main features of this app are:
* scraping all websites, that are inside each of 1.000.000 sites
* possibility of refreshing choosen website's URL base

## How to use?
1. Start Django localserver (something like `python manage.py runserver` - more on that in the [Django tutorial](https://docs.djangoproject.com/en/2.1/intro/tutorial01/))
2. Start Celery worker with `celery -A UserTask worker --loglevel=info`
3. Go to `<server_ip>:<server_port>/websites`

## Sorting in /websites
This app allow to aply ordering, sorting and pagination:
* sort by category by choosing desired category from drop-down menu
* order by any column by clicking on it
* automatic pagination (row per page can be changed in code)
