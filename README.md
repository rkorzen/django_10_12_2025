* 9-11 praca
* 11 - 11.15
* 11.15 - 13.00 - praca
* 13-14 - Obiad
* 14-15.30 - praca
* 15.30-15.45 - kawa
potem do 17



## instalacja django

    pip install django
    
    uv add django

## tworzenie projektu:

Przy aktywnym srodowisku z zainstalowanym django:

    django-admin startproject <nazwa>

## uruchomienie serwera:

    cd <nazwa>
    python manage.py runserver


## wykonanie migracji:

    python manage.py migrate

## tworzenie superusera:

    python manage.py createsuperuser

## tworzenie aplikacji:

    python manage.py startapp <nazwa>

# idea projektu joboffers

    / - glowna strona
    /offers - strona z lista ofert
    /offers/<id> - strona ze szczegolami konkretnej oferty
    </offers/add - strona dodawania oferty>
    /about - strona o projekcie
    /kontakt - strona z formularzem kontaktowym

## adres URL



http://example.com/this/is/path?query=string&a=1#fragment=anchor

http://127.0.0.1:8000/offers/


## Cwiczenie 1.

Utworz projekt todo_project z aplikacja todo.

/todos - lista zadan (z linkami do szczegolow zadan)
/todos/<id> - szczegoly zadania

zadanie ma miec tytul i tresc
zamodeluj baze - poprzez zwykla pythonowa liste zawierajaca dane - moze to byc slownik, albo obiekt