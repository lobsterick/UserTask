# UserTask

## Użytkowanie - struktura URL

* order_by
* category
* page

Na przykład

http://127.0.0.1:8000/websites/?order_by=alexa_rank&category=Search&page=1

## Zadania
1. Modele dla Website, Websitecategory oraz WebPage - ZROBIONE
2. Widoki dla websites:
- list view - W TRAKCIE
- detail view - ZROBIONO
- create view
3. Widoki dla categories:
- list view
- create view
4. Skrypt odczytujący z CSV oraz tworzący obiekty - ZROBIONY
5. Scraper dla stron WWW z bazy danych - ZROBIONY
6. Opakowanie powyższych w Celery Task
