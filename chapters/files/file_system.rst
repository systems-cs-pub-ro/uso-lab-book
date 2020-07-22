Sistemul de fișiere
===================

1) Find
-------

Pentru a căuta un fișier într-o ierarhie de directoare, putem folosi utilitarul **find**.
Pentru a învăța mai multe despre acest utilitar, putem inspecta manualul ``man find``.
Acesta nu scalează pentru situațiile când avem multe fișiere și dorim un răspuns rapid. 

Folosirea utilitarului **find**
"""""""""""""""""""""""""""""""
Căutați în sistem fișierul **passwd**.


2) Locate
---------

Utilitarul **locate** se folosește astfel: ``locate nume_fisier``.
Utilitarul funcționează în 2 pași:
 * Crearea și actualizarea unei baze de date folosind comanda **updatedb**;
 * Căutarea folosind **locate**.

Performanța utilitarului este foarte bună, superioară lui **find**.
Partea negativă este că la fiecare căutare trebuie folosit utilitarul **updatedb**.

Folosirea utilitarului **locate**
"""""""""""""""""""""""""""""""""
Căutați fișierul **pwd** în sistemul de fișiere folosind **locate**.


3) PATH
-------

După cum am menționat într-un capitol anterior, PATH este
o variabilă de mediu ce se află în contextul executării 
în linia de comandă. De fiecare dată când apelăm un program
prima oară se verifică dacă în căile din **PATH** se află
acest program.

.. code-block::

    $ echo $PATH
    /usr/local/bin:/usr/bin:/bin:/usr/games



**Exercițiu:** Afișează valoarea PATH a sistemului tău.

4) Which
--------

Acest utilitar identifică calea programelor din sistem.
Acesta folosește variabila de mediu **PATH** pentru a găsi utilitarul cerut și va afișa rezultatele în ordinea directoarelor din **PATH**.
Pentru mai mute detalii verificați manualul ``man which``.

.. code-block::

    student@uso:~$ which ls
    /bin/ls
    student@uso:~$ which pwd
    /bin/pwd
    student@uso:~$ which man
    /usr/bin/man 
