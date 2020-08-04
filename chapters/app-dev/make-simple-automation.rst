Introducere în utilitarul Make și fișiere Makefile
==================================================

1) Folosirea unui Makefile existentă
------------------------------------

Aici vor avea la dispoziție un director cu cod sursă și Makefile și vor 
rula toate regulile din Makefile, pe rând, și vor observa care este efectul fiecăreia.
Abia după ce se acomodează cu acest lucru își vor crea propriul Makefile.

2) Crearea primului Makefile
----------------------------

Vor crea un Makefile simplu.

a. Adăugarea regulii all
^^^^^^^^^^^^^^^^^^^^^^^^

Vor adăuga regulă all. 

b. Adăugarea regulii clean
^^^^^^^^^^^^^^^^^^^^^^^^^^

Vor adăuga regulă clean.

c. Adăugarea fișierului Makefile în repository
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Vor comite modificările făcute anterior.

3) Fișiere Makefile cu alte nume
--------------------------------

Aici vor redenumi fișierul Makefile creat anterior și îl vor folosi folosind `make -f`.
De asemenea vor comite această schimbare.

4) Adăugarea unor reguli de creare a fișierelor obiect
------------------------------------------------------

Vor adăuga câte o regulă pentru fiecare fișier cod sursă pentru a-l compila până la modul obiect.

5) Modificarea regulii de creare a executabilului
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Vor modifica regula existentă astfel încât executabilul final să fie 
obținut din module obiect.

6) Modificarea regulii clean
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Vor adăuga fișierele obiect la regula clean.

7) Testarea fișierului Makefile
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Vor testa toate regulile și vor observa încă de aici că fișierele se recompilează
la fiecare rulare a regulii indiferent dacă fișierul obținut a fost modificat sau nu. 

8) Crearea unui nou commit cu modificărilor făcute
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Vor comite modificările aduse asupra fișierului Makefile.

9) Wildcards
^^^^^^^^^^^^^

Acum că ați înțeles importanța compilării separate, cum am proceda 
pentru un proiect care are sute de fișiere sursă? Goto wildcards.
