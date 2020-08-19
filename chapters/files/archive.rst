Arhive
======

Arhivele sunt o agregare a mai multor fișiere și directoare într-un singur fișier.

.. note::
    **Comprimarea** este asemănătoare cu arhivarea dar, în plus, micșorează dimensiunea fișierului rezultat.
    Rezultatul este similar: agregarea într-un singur fișier.

În acest capitol vom folos arhive de tipul **zip** și **tar**.

1. Arhive **tar**
-----------------

a. Crearea arhivelor
^^^^^^^^^^^^^^^^^^^^

Folosim utilitarul **tar** împreună cu parametrii potriviți:

* -c: creează arhiva;
* -v: *verbose* - afișează detalii despre operație;
* -f: folosește arhiva dată ca parametru (în cazul de față, numele ei).

.. code-block:: bash

    student@uso-demo:~$ ls -lh
    total 9.0M
    -rw-r--r-- 1 student student 5.0M Aug 19 11:55 fisier1
    -rw-r--r-- 1 student student 3.0M Aug 19 11:55 fisier2
    -rw-r--r-- 1 student student 1.0M Aug 19 11:55 fisier3
    student@uso-demo:~$ tar -cvf fisiere.tar fisier1 fisier2 fisier3
    fisier1
    fisier2
    fisier3
    student@uso-demo:~$ ls -lh
    total 19M
    -rw-r--r-- 1 student student 5.0M Aug 19 11:55 fisier1
    -rw-r--r-- 1 student student 3.0M Aug 19 11:55 fisier2
    -rw-r--r-- 1 student student 1.0M Aug 19 11:55 fisier3
    -rw-r--r-- 1 student student 9.1M Aug 19 11:56 fisiere.tar

.. note::
    Obervăm cum după comanda de creare a arhivei **tar** am verficat corectitudinea operației.

Putem observa că fișierul de tipul **tar** nou creat **nu** ocupă mai puțin spațiu; din contră, ocupă mai mult spațiu din cauza metadatelor fișierului.
Pentru o mai bună înțelegere a comenzii de creare a arhivelor inspectați manualul: ``man tar``.

Exercițiu - creare arhive
"""""""""""""""""""""""""
Creați 3 fișiere ca în exemplu. Creați o arhivă de tipul **tar** a fișierelor cu numele **fisiere.tar**.


b. Afișarea conținutului arhivelor
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Pentru a vizualiza arhiva **fără** dezarhivare folosim opțiunea **-t** ca în exemplul de mai jos:

.. code-block:: bash

    student@uso-demo:~$ tar -tf fisiere.tar
    fisier1
    fisier2
    fisier3

Opțiunea **-f** este pentru a specifica ce arhivă vrem să afișăm.

Exercițiu - afișarea conținutului unei arhive
"""""""""""""""""""""""""""""""""""""""""""""
Afișați conținutul arhivei **fără** dezarhivare.


c. Dezarhivarea arhivelor
^^^^^^^^^^^^^^^^^^^^^^^^^

Dezarhivăm o arhivă folosim opțiunea **-x**, ca în exemplul de mai jos.
Pentru acest exemplu ștergem înainte fișierele existente.

.. code-block:: bash

    student@uso-demo:~$ rm fisier1 fisier2 fisier3
    student@uso-demo:~$ ls
    fisiere.tar
    student@uso-demo:~$ tar xvf fisiere.tar
    fisier1
    fisier2
    fisier3
    student@uso-demo:~$ ls -lh
    total 19M
    -rw-r--r-- 1 student student 5.0M Aug 19 11:55 fisier1
    -rw-r--r-- 1 student student 3.0M Aug 19 11:55 fisier2
    -rw-r--r-- 1 student student 1.0M Aug 19 11:55 fisier3
    -rw-r--r-- 1 student student 9.1M Aug 19 12:04 fisiere.tar

.. note::
    Observăm cum după operațiile de ștergere și dezarhivare, am verificat corectitudinea operațiilor.


Pentru a extrage fișierele către o anumită cale, folosim opțiunea **--directory**:

.. code-block:: bash

    student@uso-demo:~$ ls -l
    total 18436
    -rw-r--r-- 1 student student 5242880 Aug 19 11:55 fisier1
    -rw-r--r-- 1 student student 3145728 Aug 19 11:55 fisier2
    -rw-r--r-- 1 student student 1048576 Aug 19 11:55 fisier3
    -rw-r--r-- 1 student student 9439088 Aug 19 12:04 fisiere.tar
    student@uso-demo:~$ mkdir -p dezarhivare/tar
    student@uso-demo:~$ tree
    .
    |-- dezarhivare
    |   `-- tar
    |-- fisier1
    |-- fisier2
    |-- fisier3
    `-- fisiere.tar

    2 directories, 4 files
    student@uso-demo:~$ tar -xvf fisiere.tar --directory dezarhivare/tar/
    fisier1
    fisier2
    fisier3
    student@uso-demo:~$ tree
    .
    |-- dezarhivare
    |   `-- tar
    |       |-- fisier1
    |       |-- fisier2
    |       `-- fisier3
    |-- fisier1
    |-- fisier2
    |-- fisier3
    `-- fisiere.tar

    2 directories, 7 files

.. note::
    Observăm că după crearea directoarelor și după extragerea arhivelor am verificat corectitudinea operațiilor.

Pentru a dezarhiva un singur fișier din toată arhiva, punem ca ultim parametru numele fișierului ca în exemplul de mai jos:

.. code-block:: bash

    student@uso-demo:~$ rm fisier1 fisier2 fisier3
    student@uso-demo:~$ ls
    dezarhivare  fisiere.tar
    student@uso-demo:~$ tar -xvf fisiere.tar fisier1
    fisier1
    student@uso-demo:~$ ls -l
    total 14344
    drwxr-xr-x 3 student student    4096 Aug 19 12:15 dezarhivare
    -rw-r--r-- 1 student student 5242880 Aug 19 11:55 fisier1
    -rw-r--r-- 1 student student 9439088 Aug 19 12:04 fisiere.tar


.. note::
    Obervăm cum după comenzile de ștergere și dezarhivare s-a verificat corectitudinea operațiilor.


Exercițiu - dezarhivarea unei arhive
""""""""""""""""""""""""""""""""""""
Creați un director cu numele **dezarhivare** și în acest director încă unul cu numele **tar** ca în ierarhia de mai sus.
Dezarhivați arhiva în directorul **dezarhivare/tar/**.
Dezarhivați **doar** fișierul **fisier2** în directorul curent.
Verificați corectitudinea operațiilor.

d. Adăugarea de noi fișiere la arhive
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Adăugăm un nou fișier la arhivă folosind opțiunea **-r**:

.. code-block:: bash

    student@uso-demo:~$ ls -l
    total 25608
    drwxr-xr-x 3 student student    4096 Aug 19 12:15 dezarhivare
    -rw-r--r-- 1 student student 5242880 Aug 19 11:55 fisier1
    -rw-r--r-- 1 student student 3145728 Aug 19 11:55 fisier2
    -rw-r--r-- 1 student student 1048576 Aug 19 11:55 fisier3
    -rw-r--r-- 1 student student 7340032 Aug 19 12:35 fisier4
    -rw-r--r-- 1 student student 9441280 Aug 19 12:36 fisiere.tar
    student@uso-demo:~$ tar -tf fisiere.tar
    fisier1
    fisier2
    fisier3
    student@uso-demo:~$ tar -rvf fisiere.tar fisier4
    fisier4
    student@uso-demo:~$ tar -tf fisiere.tar
    fisier1
    fisier2
    fisier3
    fisier4

În primă fază am verificat că **fisier4** nu există în arhivă.
În continuare am adăugat **fisier4** la arhivă.

.. note::
    Observăm cum după comanda de adăugare de fișier la arhivă, am verificat corectitudinea operației.


Exercițiu - adăugare de noi fișiere
"""""""""""""""""""""""""""""""""""
Creați un fișier **fisier4** și adăugați-l la arhivă, ca în exemplul de mai sus.
Verificați corectitudinea operației.


2. Arhive **zip**
-----------------

a. Crearea arhivelor
^^^^^^^^^^^^^^^^^^^^

Folosim utilitarul **zip** împreună cu parametrii potriviți:


.. code-block:: bash

    student@uso-demo:~$ ll
    total 16388
    drwxr-xr-x 3 student student    4096 Aug 19 12:15 dezarhivare
    -rw-r--r-- 1 student student 5242880 Aug 19 11:55 fisier1
    -rw-r--r-- 1 student student 3145728 Aug 19 11:55 fisier2
    -rw-r--r-- 1 student student 1048576 Aug 19 11:55 fisier3
    -rw-r--r-- 1 student student 7340032 Aug 19 12:35 fisier4
    -rw-r--r-- 1 student student 9.1M Aug 19 17:56 fisiere.tar
    student@uso-demo:~$ zip fisiere.zip fisier1 fisier2 fisier3
      adding: fisier1 (deflated 0%)
      adding: fisier2 (deflated 0%)
      adding: fisier3 (deflated 0%)
    student@uso-demo:~$ ls -lh
    total 26M
    drwxr-xr-x 3 student student 4.0K Aug 19 12:15 dezarhivare
    -rw-r--r-- 1 student student 5.0M Aug 19 11:55 fisier1
    -rw-r--r-- 1 student student 3.0M Aug 19 11:55 fisier2
    -rw-r--r-- 1 student student 1.0M Aug 19 11:55 fisier3
    -rw-r--r-- 1 student student 7.0M Aug 19 12:35 fisier4
    -rw-r--r-- 1 student student 9.1M Aug 19 17:56 fisiere.tar
    -rw-r--r-- 1 student student 9.1M Aug 19 17:54 fisiere.zip

.. note::
    Obervăm cum după comanda de creare a arhivei **zip** am verficat corectitudinea operației.

Putem observa că fișierul de tipul **zip** nou creat **nu** ocupă mai puțin spațiu; din contră, ocupă mai mult spațiu din cauza metadatelor fișierului.
Pentru o mai bună înțelegere a comenzii de creare a arhivelor inspectați manualul: ``man zip``.

Exercițiu - creare arhive
"""""""""""""""""""""""""
Creați o arhivă de tipul **zip** a fișierelor cu numele **fisiere.zip**.


b. Afișarea conținutului arhivelor
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Pentru a vizualiza arhiva **fără** dezarhivare folosim opțiunea **-sf** ca în exemplul de mai jos:

.. code-block:: bash

    student@uso-demo:~$ zip -sf fisiere.zip
    Archive contains:
      fisier1
      fisier2
      fisier3
    Total 3 entries (9437184 bytes)

Opțiunea **-f** este pentru a specifica ce arhivă vrem să afișăm.

Exercițiu - afișarea conținutului unei arhivei
""""""""""""""""""""""""""""""""""""""""""""""
Afișați conținutul arhivei **fără** dezarhivare.


c. Dezarhivarea arhivelor
^^^^^^^^^^^^^^^^^^^^^^^^^

Pentru a dezarhiva o arhivă folosim utilitarul **unzip**.
Pentru acest exemplu ștergem înainte fișierele existente.

.. code-block:: bash

    student@uso-demo:~$ ll
    total 29708
    drwxr-xr-x 3 student student    4096 Aug 19 12:15 dezarhivare
    -rw-r--r-- 1 student student 5242880 Aug 19 11:55 fisier1
    -rw-r--r-- 1 student student 3145728 Aug 19 11:55 fisier2
    -rw-r--r-- 1 student student 1048576 Aug 19 11:55 fisier3
    -rw-r--r-- 1 student student 7340032 Aug 19 12:35 fisier4
    -rw-r--r-- 1 student student 9441280 Aug 19 17:56 fisiere.tar
    -rw-r--r-- 1 student student 4195250 Aug 19 18:00 fisiere.zip
    student@uso-demo:~$ rm fisiere.zip
    student@uso-demo:~$ zip fisiere.zip fisier1 fisier2  fisier3
      adding: fisier1 (deflated 0%)
      adding: fisier2 (deflated 0%)
      adding: fisier3 (deflated 0%)
    student@uso-demo:~$ ll
    total 34828
    drwxr-xr-x 3 student student    4096 Aug 19 12:15 dezarhivare
    -rw-r--r-- 1 student student 5242880 Aug 19 11:55 fisier1
    -rw-r--r-- 1 student student 3145728 Aug 19 11:55 fisier2
    -rw-r--r-- 1 student student 1048576 Aug 19 11:55 fisier3
    -rw-r--r-- 1 student student 7340032 Aug 19 12:35 fisier4
    -rw-r--r-- 1 student student 9441280 Aug 19 17:56 fisiere.tar
    -rw-r--r-- 1 student student 9439072 Aug 19 18:02 fisiere.zip
    student@uso-demo:~$ rm fisier1 fisier2  fisier3
    student@uso-demo:~$ unzip fisiere.zip
    Archive:  fisiere.zip
      inflating: fisier1
      inflating: fisier2
      inflating: fisier3
    student@uso-demo:~$ ls -lh
    total 35M
    drwxr-xr-x 3 student student 4.0K Aug 19 12:15 dezarhivare
    -rw-r--r-- 1 student student 5.0M Aug 19 11:55 fisier1
    -rw-r--r-- 1 student student 3.0M Aug 19 11:55 fisier2
    -rw-r--r-- 1 student student 1.0M Aug 19 11:55 fisier3
    -rw-r--r-- 1 student student 7.0M Aug 19 12:35 fisier4
    -rw-r--r-- 1 student student 9.1M Aug 19 17:56 fisiere.tar
    -rw-r--r-- 1 student student 9.1M Aug 19 18:02 fisiere.zip
.. note::
    Observăm cum după operațiile de ștergere și dezarhivare, am verificat corectitudinea operațiilor.


Pentru a extrage fișierele către o anumită cale, folosim opțiunea **-d**:

.. code-block:: bash

    student@uso-demo:~$ mkdir dezarhivare/zip
    student@uso-demo:~$ unzip fisiere.zip -d dezarhivare/zip/
    Archive:  fisiere.zip
      inflating: dezarhivare/zip/fisier1
      inflating: dezarhivare/zip/fisier2
      inflating: dezarhivare/zip/fisier3
    student@uso-demo:~$ tree
    .
    |-- dezarhivare
    |   |-- tar
    |   `-- zip
    |       |-- fisier1
    |       |-- fisier2
    |       `-- fisier3
    |-- fisier1
    |-- fisier2
    |-- fisier3
    |-- fisier4
    |-- fisiere.tar
    `-- fisiere.zip

    3 directories, 9 files

.. note::
    Observăm că după crearea directoarelor și după extragerea arhivelor am verificat corectitudinea operațiilor.

Pentru a dezarhiva un singur fișier din toată arhiva, punem ca ultim parametru numele fișierului ca în exemplul de mai jos:

.. code-block:: bash

    student@uso-demo:~$ rm fisier3
    student@uso-demo:~$ ls -lh
    total 34M
    drwxr-xr-x 4 student student 4.0K Aug 19 18:05 dezarhivare
    -rw-r--r-- 1 student student 5.0M Aug 19 11:55 fisier1
    -rw-r--r-- 1 student student 3.0M Aug 19 11:55 fisier2
    -rw-r--r-- 1 student student 7.0M Aug 19 12:35 fisier4
    -rw-r--r-- 1 student student 9.1M Aug 19 17:56 fisiere.tar
    -rw-r--r-- 1 student student 9.1M Aug 19 18:02 fisiere.zip
    student@uso-demo:~$ unzip fisiere.zip fisier3
    Archive:  fisiere.zip
    inflating: fisier3
    student@uso-demo:~$ ls -lh
    total 35M
    drwxr-xr-x 4 student student 4.0K Aug 19 18:05 dezarhivare
    -rw-r--r-- 1 student student 5.0M Aug 19 11:55 fisier1
    -rw-r--r-- 1 student student 3.0M Aug 19 11:55 fisier2
    -rw-r--r-- 1 student student 1.0M Aug 19 11:55 fisier3
    -rw-r--r-- 1 student student 7.0M Aug 19 12:35 fisier4
    -rw-r--r-- 1 student student 9.1M Aug 19 17:56 fisiere.tar
    -rw-r--r-- 1 student student 9.1M Aug 19 18:02 fisiere.zip

.. note::
    Obervăm cum după comenzile de ștergere și dezarhivare s-a verificat corectitudinea operațiilor.


Exercițiu - dezarhivarea unei arhive
""""""""""""""""""""""""""""""""""""
Creați un director cu numele **zip** în directorului **dezarhivare** ca în ierarhia de mai sus.
Dezarhivați arhiva în directorul **dezarhivare/zip/**.
Dezarhivați **doar** fișierul **fisier2** în directorul curent.
Verificați corectitudinea operațiilor.


d. Adăugarea de noi fișiere la arhive
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Adăugăm un nou fișier la arhivă folosind opțiunea **-u**:

.. code-block:: bash

    student@uso-demo:~$ zip -u fisiere.zip fisier4
      adding: fisier4 (deflated 0%)
    student@uso-demo:~$ zip -sf fisiere.zip
    Archive contains:
      fisier1
      fisier2
      fisier3
      fisier4
    Total 4 entries (16777216 bytes)


În exemplul de mai sus am adăugat **fisier4** la arhivă.

.. note::
    Observăm cum după comanda de adăugare de fișier la arhivă, am verificat corectitudinea operației.


Exercițiu - adăugarea unui fișier în arhivă
"""""""""""""""""""""""""""""""""""""""""""
Creați un fișier **fisier4** și adăugați-l la arhivă, ca în exemplul de mai sus.
Verificați corectitudinea operației.
