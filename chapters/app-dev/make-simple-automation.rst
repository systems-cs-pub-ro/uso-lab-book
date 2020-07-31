##################################################
Introducere în utilitarul make și fișiere Makefile
##################################################

1) Folosirea unui Makefile deja existentă
*****************************************

Aici vor avea la dispoziție un director cu cod sursă și Makefile și vor 
rula toate regulile din Makefile, pe rând, și vor observa care este efectul fiecăreia.
Abia după ce se acomodează cu acest lucru își vor crea propriul Makefile.

****************************
2) Crearea primului Makefile
****************************

Vor crea un Makefile simplu cu regulă de build.

***************************
3) Adăugarea regulii de run
***************************

Vor adăuga regulă de run.

*****************************
4) Adăugarea regulii de clean
*****************************

Vor adăuga regulă de clean.

**********************************************
5) Adăugarea fișierului Makefile în repository
**********************************************

Vor comite modificările făcute anterior.

**********************************************
6) Makefile-uri cu nume speciale
**********************************************

Aici vor redenumi fișierul Makefile creat anterior și îl vor folosi folosind `make -f`.
De asemenea vor comite această schimbare.

******************************************************
7) Adăugarea unor reguli de creare a fișierelor obiect
******************************************************

Vor adăuga câte o regulă pentru fiecare fișier cod sursă pentru a-l compila până la modul obiect.

*************************************************
8) Modificarea regulii de creare a executabilului
*************************************************

Vor modifica regula existentă astfel încât executabilul final să fie 
obținut din module obiect.

*******************************
9) Modificarea regulii de clean
*******************************

Vor adăuga fișierele obiect la regula clean.

********************************
10) Testarea fișierului Makefile
********************************

Vor testa toate regulile și vor observa încă de aici că fișierele se recompilează
la fiecare rulare a regulii indiferent dacă fișierul obținut a fost modificat sau nu. 

*********************************
11) Comiterea modificărilor făcute
*********************************

Vor comite modificările aduse asupra fișierului Makefile.

*************
12) Wildcards
*************

Acum că ați înțeles importanța compilării separate, cum am proceda 
pentru un proiect care are sute de fișiere sursă? Goto wildcards.