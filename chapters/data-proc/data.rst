.. _data_proc_data:

Date structurate
================

sunt foarte multe informații (digitale), apar informații noi în fiecare moment

dorim să reținem informații pentru utilizare ulterioară

în general au o structură: entități cu proprietăți cu valori; sau obiecte care au atribute care au valori

informațiile sunt obținute și stocate / reținute ca date structurate

din forma de stocare sunt prelucrate

în general datele sunt conținut brut, fără semnificație; atașarea unei semnificații înseamnă că avem nevoie de informație

vom folosi noțiunea de date, fiind preocupați de modul în care folosim și prelucrăm datele; asocierea unei semnificații este responsabilitatea persoanei care folosește efectiv acele date

fun fact: Excel - cel mai folosit limbaj

.. _data_proc_data_structured:

Exemple de date structurate
---------------------------

catalog studenti

cursul valutare

obiecte de cumpărat dintr-un magazin online

.. _data_proc_data_table:

Date tabelare
-------------

forma "naturală" de reprezentare a datelor structurate:

* rândurile sunt obiectele
* coloanele sunt atributele
* în fiecare celulă se găsește valoarea atributului pentru obiectul respectiv

Forma tabelară este folosită în utilitare care lucrează cu spreadsheeturi.

Este folosită și în formatul CSV (discutăm mai jos) și în fișiere de configurare (de exemplu ``/etc/passwd``).

Este folosită în baze da date.

.. _data_proc_data_storage:

Moduri de stocare a datelor
---------------------------

forme de stocare human readable sau binare

reprezentarea / vizualizarea este cel mai adesea tabelară

forma binară necesită un utilitar de interpretare, vizualizare, prelucrare: spreadsheet

forma binară este folosită și în baze de date; la fel, un client este folosit pentru accesare

format human readable folosește utilitare care prelucrează text; sau putem scrie programe / scripturi care prelucrează text

formatul text standard este CSV (*Comma-Separated Values*); format tabelar pur

alte formate sunt JSON, YAML, XML, TSV;
indicat unde e folsoit prevalent fiecare format, exemple concrete

avantaje / dezavantaje

.. _data_proc_data_process:

Moduri de prelucrare a datelor
------------------------------

Le vom folosi practic în secțiunile următoare

vizualizare

conversie

selectare

(re)formatare

sortare

agregare

substituție / modificare

realizarea de grafice
