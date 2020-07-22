Interacțiunea cu fișiere în linia de comandă
============================================

1) Manipularea fișierelor și directoarelor
------------------------------------------

În această secțiune vom detalia modalități de interacțiune cu fișierele.

a) Crearea fișierelor
^^^^^^^^^^^^^^^^^^^^^

Fișierele se creează folosind utilitarul ``touch``. Putem învăța mai
multe detalii despre comandă uitându-ne în manual ``man touch``. Pentru a crea
un fișier cu spațiu înclus în nume este nevoie să folosim ghilimelele la
începutul și sfârșitul numelui astfel: ``touch numele_ales_de_mine``.

**Exercițiu:** Creați două fișiere cu numele *Mircea* și *Ioana*.

b) Crearea directoarelor
^^^^^^^^^^^^^^^^^^^^^^^^

Directoarele se creează folosind utilitarul ``mkdir``. Etimologia comenzii 
provine din engleză - *Make Directory*. Putem învăța mai multe detalii despre
comandă uitându-ne în manual ``man mkdir``.

**Exercițiu:** Creați două directoare cu nume de orașe din România.

c) Afișarea conținutului unui director
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Precum conținutul unui dosar ce constă în mai multe foi, conținutul directoarelor
este format din fișiere și alte directoare. Pentru a afișa conținutul unui director
folosim comanda ``ls``. Putem învăța mai multe detalii despre comandă uitându-ne în
manual ``man ls``. Pentru a vedea mai multe informații despre fișiere și directoare
putem folosi opțiunea *-l* în felul următor: ``ls -l``.

.. code-block::

    student@uso:~$ ls -l
    PERMISSIONS  L USER  GROUP  SIZE    DATE      NAME
    drwxrwxr-x+ 46 root  admin  1472 Jul 23 22:46 Applications
    drwxr-xr-x  69 root  wheel  2208 Jul 20 09:49 Library
    drwxr-xr-x@  8 root  wheel   256 Oct 24  2019 System
    drwxr-xr-x   7 root  admin   224 Oct 24  2019 Users
    drwxr-xr-x   4 root  wheel   128 Jul 22 05:23 Volumes
    drwxr-xr-x@ 38 root  wheel  1216 Jul 20 09:45 bin
    drwxr-xr-x   2 root  wheel    64 Aug 24  2019 cores
    dr-xr-xr-x   3 root  wheel  4761 Jul 20 09:52 dev
    lrwxr-xr-x@  1 root  admin    11 Nov 26  2019 etc -> private/etc
    lrwxr-xr-x   1 root  wheel    25 Jul 20 09:53 home -> /System/Volumes/Data/home
    drwxr-xr-x   4 root  wheel   128 Nov 26  2019 opt
    drwxr-xr-x   6 root  wheel   192 Jul 20 09:46 private
    drwxr-xr-x@ 63 root  wheel  2016 Jul 20 09:45 sbin
    lrwxr-xr-x@  1 root  admin    11 Nov 26  2019 tmp -> private/tmp
    drwxr-xr-x@ 11 root  wheel   352 Nov 26  2019 usr
    lrwxr-xr-x@  1 root  admin    11 Nov 26  2019 var -> private/var
 
Mai sus avem afișarea comenzii ``ls -l``. Avem fiecare fișier sau director pe
câte o linie. Semnificația coloanelor este: 

* **Tipul fișierului:** Primul caracter specifică dacă este un director (**d**), fișier (**-**) sau legătură (**l**).
  Vom discuta despre legături într-un capitol ulterior.
* **Permisiuni:** avem 2 tipuri de informații:
* **Legături:** Numărul de legături către acest fișier/director. Vom detalia într-un capitol ulterior.
* **USER:** Utilizatorul care deține acest fișier/director.
* **GROUP:** Grupul ce deține acest fisier/director.
* **SIZE:** Dimensiunea fișierului/directorului.
* **DATE:** Data la care a fost creat/modificat.
* **NAME:** Numele fișierului/directorului


**Exercițiu:** Afișați conținutul directorului curent folosind opțiunea **-l**.

**Exercițiu:** Creați fișierul cu numele *Ioana Popescu*.
Afișați conținutul directorului.
Este important de reținut: orice comandă executați aceasta trebuie succedată de o verificare.
De exemplu, la crearea unui fișier (``touch``), executăm comanda de verificare ``ls``.

d) Afișarea conținutului unui fișier
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Afișarea conținutului unui fișier se poate face prin mai multe moduri. Unul din ele
este folosind comanda **cat** astfel: ``cat fișier``. O altă metodă este de a folosi
un editor de text: **vim**, *gedit**, **emacs**, **nano**, **sublime**, etc. Vom
detalia utilizarea unui editor de text într-o secțiune ulterioară.

**Exercițiu:** Afișați conținutul fișierului *Mircea*.

e) Ștergerea fișierelor
^^^^^^^^^^^^^^^^^^^^^^^

Fișierele se șterg folosind utilitarul ``rm``. Putem învăța mai multe
detalii despre comandă uitându-ne în manual ``man rm``.

**Exercițiu:** Ștergeți fișierul *Mircea*. Confirmați ștergerea prin afișarea
conținutului directorului părinte.


f) Ștergerea directoarelor
^^^^^^^^^^^^^^^^^^^^^^^^^^

Directoarele se șterg folosind comanda ``rmdir``.
Etimologia comenzii provine din engleză - *Remove Directory*.
Putem învăța mai multe detalii despre comandă uitându-ne în manual ``man rmdir``. 
Dacă directorul nu este gol, comanda ``rmdir`` se întoarce cu eroare.
Pentru a șterge un director gol, folosim utilitarul ``rm`` cu opțiunile de recursivitate ``-r`` și forțat ``-f``: ``rm -rf``.

**Exercițiu:** Ștergeți unul din directoarele create. Confirmați ștergerea prin
afișarea conținutului directorului părinte.

g) Redenumirea fișierelor și directoarelor 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Fișierele și directoarele se redenumesc în mod similar, folosind comanda ``mv``
astfel: ``mv nume_actual nume_nou``. Putem învăța mai multe detalii despre comandă
uitându-ne în manual ``man mv``.

Un alt rol al comenzii ``mv`` este de a muta fișierele și directoarele, în ierarhia
de fișiere, dintr-un loc în altul. Exemplu ``mv cale_actuală cale_nouă``. Putem
folosi atât căi relative cât și căi absolute.

**Exercițiu:** Redenumiți fișierul *Ioana* în *Maria*. Confirmați ștergerea prin
afișarea conținutului directorului părinte.

**Exercițiu:** Mutați fișierul *Maria* în directorul creat anterior. Confirmați
ștergerea prin afișarea conținutului directorului părinte.

**Exercițiu:** Redenumiți fișierului *Maria* în *Maria.txt* și afișați conținutul.
Redenumiți apoi în *Maria.pdf* și afișați conținutul. Redenumiți apoi în *Maria.qzy*
și afișați conținutul. Ce observați?

h) Fișiere și directoare ascunse
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Un fișier sau director este ascuns atunci când nu apare în mod normal în ierarhia de fișiere.
Pentru a vedea un fișier ascuns se folosește opțiunea **-a** a utilitarului ls, astfel: ``ls -a``.
Pentru a crea un fișier/director ascuns în Linux, acesta trebuie să înceapă cu caracterul *.*: ``touch **.**fisier_ascuns`` sau ``mkdir **.**director_ascuns``.

**Exercițiu:** Creați un fișier numit **fișierul_meu_ascuns** și un director cu numele **directorul_meu_ascuns**.
Confirmați crearea prin afișarea conținutului directorului părinte.

i) Afișarea informațiilor de tip metadata pentru un fișier
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Informațiile de tip metadata pentru un fișier/director includ informații legate de dimensiune, data de creare/accesare, permisiuni, tipul de fișier.
Pentru a afla informații suplimentare despre fișiere, putem folosi comanda ``stat``.
Putem învăța mai multe detalii despre comandă uitându-ne în manual: ``man stat``.
**TODO: interpretat output**

Pentru a vedea tipul de fișier putem folosi comanda ``file``.
Putem învăța mai multe detalii despre comandă uitându-ne în manual: ``man file``.

**Exercițiu:** Afișați metadatele fișierului *Maria*.

j) Afișarea tipului de fișier
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

O ierarhie de fișiere este formată din directoare și fișiere. Fișierele pot fi de mai
multe tipuri: text, binare, imagini, arhive, etc. Pentru a afla tipul fișierului
folosim comanda ``file``. Putem învăța mai multe detalii despre comandă uitându-ne
în manual ``man file``. 

.. code-block::

    student@uso:~$ file Picture.png
    Picture.png: PNG image data, 742 x 320, 8-bit/color RGBA, non-interlaced
    student@uso:~$ file index.rst
    index.rst: ASCII text
    student@uso:~$ file archive.tar
    archive.tar: POSIX tar archive (GNU) 

2) Ierarhie de fișiere
----------------------

Fișierele sunt dispuse într-o formă arborescentă, ierarhică:

.. code-block::

    student@uso:~$ tree
    .
    ├── Makefile
    ├── README.md
    ├── _static
    │   └── my_theme.css
    ├── _templates
    │   └── layout.html
    ├── chapters
    │   ├── files
    │   │   ├── archive.rst
    │   │   ├── file_editor.rst
    │   │   ├── file_system.rst
    │   │   ├── files.rst
    │   │   ├── io_redirection.rst
    │   │   └── paths.rst
    │   └── net
    │       ├── browser.rst
    │       ├── extra.rst
    │       ├── img
    │       │   └── browser.png
    │       ├── services.rst
    │       └── troubleshoot.rst
    ├── conf.py
    ├── docker
    │   ├── Dockerfile
    │   └── docker-compose.yml
    ├── index.rst
    ├── make.bat
    └── requirements.txt

Putem vedea că directorul curent **chapter** include 2 directoare **files** și **net**.
Directorul **files** conține 6 fișiere, iar directorul **net** conține 4 fișiere și un
director **img** care conține la rândul său un fișier.

Pentru a vedea fișierele sub formă arborescentă, folosim comanda ``tree``. Putem învăța
mai multe detalii despre comandă uitându-ne în manual: ``man tree``.

**Exercițiu:** Afișați ierarhia de fișiere pornind de la directorul vostru home (~).

**Exercițiu:** Creați următoarea ierarhie pornind de la directorul **/home/student/**:

.. code-block::

    student@uso:~$ tree
    .
    ├── prime video
    ├── Hulu
    │   └── Favorite
    ├── Netflix
    │   ├── Filme
    │   │   ├── filme 2020.txt
    │   │   ├── filme 2019.txt
    │   │   ├── filme vechi
    │   └── Seriale
    │       ├── seriale 2020
    │       ├── seriale 2019.txt
    │       └── seriale vechi
    ├── HBO GO
    │   ├── Modern Family.txt
    │   └── Harry Potter
    └── YouTube TV

**Exercițiu:** Copiați întreaga ierarhie în calea **/tmp**. Folosiți comanda ``cp``.
Confirmați copierea prim afișarea directorului părinte.

**Exercițiu:** Ștergeți fișierul *Favorite* din Directorul Hulu. Confirmați ștergerea
prin afișarea directorului părinte.

**Exercițiu:** Ștergeți directorul *prime video*. Confirmați ștergerea prin afișarea
directorului părinte.

**Exercițiu:** Ștergeți directorul *HBO GO*. Găsiți parametrii corespunzători ștergerii
unui director care nu este gol. Confirmați ștergerea prin afișarea directorului părinte.

**Exercițiu:** Ștergeri ierarhia de directoare începând cu directorul *Netflix*. Conformați
ștergerea prin afișarea directorului părinte.

**Exercițiu:** Creați ierarhia de directoare de mai jos. Căutați parametrul necesar pentru
``mkdir`` pentru a crea toată ierarhia **dintr-o singură executare a comenzii**:

.. code-block::

    student@uso:~$ tree
    .
    └─── Cale
        └─── Lungă
             └─── De
                  └─── Directoare

**Exercițiu:** Mutați ierarhia copiată anterior în **/tmp** în directorul **Directoare**.

3) Legături (Links)
-------------------

O legătură este o scurtătură către un fișier sau un director. Mai multe legături pot referi
același director/fișier.

Există 2 tipuri de legături:

* Legături simbolice (soft links)
* Legături strânse (hard links)


a) Legături simbolice (Soft Links)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Caracteristici:**

* Similar *Shortcut* din Windows;
* Orice modificare în fisierul țintă, se vede și în fișierul legătură;
* Este o legătură către numele fișierului și nu către conținut;
* Dacă fișierul este mutat sau redenumit, legătura se pierde;
* Putem crea legături simbolice către directoare.

Putem crea legături simbolice folosin comanda ``ln -s fișier_țintă legătură``.

**Exercițiu:** Creați o legătură simbolică către directorul *Netflix*. Verificați crearea legăturii prin afișarea conținutului directorului părinte.

**Exercițiu:** Afișați conținutul legăturii.

**Exercițiu:** Ștergeți directorul  *Netflix*. Afișați conținutul legăturii.


b) Legături strânse (Hard Links)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Caracteristici:**

* Rămân legate indiferent dacă fișierul țintă este mutat sau redenumit;
* Chiar dacă fișierul inițial este șters, legătura conține datele fișierului țintă;
* Orice modificare în fișierul țintă, se vede și în fișierul legătură.
* Au conținutul(dimensiunea) fișierului țintă;
* Nu putem crea legături strânse către directoare.

Putem crea legături strânse folosind comanda ``ln fișier_țintă legătură``.


**Exercițiu:** Creați o legătură strânsă către un fișierul *Modern Family.txt* din ierarhia
creată. Verificați crearea legăturii prin afișarea conținutului directorului părinte.

**Exercițiu:** Afișați conținutul legăturii. 

**Exercițiu:** Ștergeți fișierul *Modern Family.txt*. Afișați conținutul legăturii.

4) Execuția programelor
-----------------------

Executarea fișierelor se face în felul următor: **CALE+NUME**. Se folosește calea relativă
sau absolută. Exemplu: ``./executabil`` sau ``/home/student/executabil``. 

În contextul interpretorului de comenzi există o serie variable de context ce pot fi
vizualizate cu comanda ``env``. În aceste variabile de mediu se află și variabila **PATH**.
Aceasta conține căi predefinite unde se pun de obicei executabilele. Exemplu:

.. code-block::

    student@uso:~$ echo $PATH
    /usr/local/bin:/usr/bin:/bin:/usr/games

Putem vedea mai multe căi predefinite: */usr/local/bin*, */usr/bin*, */bin* și */usr/games*.
Interpretorul de comenzi încearcă să găsească numele executabilului în acestei căi inițial.
De aceea utilitarele **ls**, **pwd**, **cd**, etc. funcționează. Noi executăm comanda ``ls``,
iar interpretorul de comenzi caută în aceste căi.

**Exercițiu:** Puneți un executabil creat de voi în **/usr/local/bin**. Executați folosind **doar numele**, nu și calea.

