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


## Migracje

### Polecenia do migracji:

    python manage.py makemigrations
    python manage.py migrate


    python manage.py makemigrations <app_label>
    python manage.py migrate <app_label>

    python manage.py showmigrations
    python manage.py sqlmigrate <app_label> <migration_name>


    # cofniecie migracji dla konkretnej aplikacji
    python manage.py migrate <app_label> zero

    python manage.py migrate <app_label> <migration number>


## Praca z modelem w shell

    python manage.py shell

### tworzenie obiektu:

    o = Offer()
    o.title = "test"
    o.description = "test"
    o.save()

    o2 = Offer.objects.create(title="test2", description="test2")

## cwieczenie - prosty model

Utworz model Todo z polami title i description, start_date i end_date i flaga is_done
wykonaj migracje
w shell utworz 2 instancje tej klasy i zapisz je do bazy

## cwiczenie - utworz relacje z Tag dla Todo

## cwiczenie - zmien sposob wyswietlania tagow w PA dla ofert

## cwiczenie - uzyj parametru q z request.GET do filtrowania TODO w widoku listy (analogicznie do jobs)

## cwiczenie

Dodaj model Category z polami name i slug (models.SlugField). Wprowadz relacje z Todo.
Dodaj do Panelu Admina


## cwiczenie - fabryki

Utworz fabryke dla Tag
Utorz polecenie ktore utworzy n Todo, np:

    python manage.py create_todos 10

## cwiczenie - testy modeli

Dopisz testy do modelu Company
Dopisz testu do modelu Todo
Dopisz testy do modelu Tag