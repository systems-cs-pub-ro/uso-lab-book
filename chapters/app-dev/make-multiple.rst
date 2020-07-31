############################################################
Compilarea unui program din surse și fișiere header multiple
############################################################

*************************
1) Inspectarea fișierelor
*************************

Vor analiza cum se leagă fișierele cod sursă între ele. Unde sunt incluse headerele.
Să vadă că fișiere cod sursă nu se includ în niciun alt fișier.

********************************************
2) Compilarea programului din surse multiple
********************************************

Aici vor compila fișierele și vor obține fișierul binar final.

*****************
3) Fișiere obiect
*****************

a. Compilarea fișierelor cod sursă în fișere obiect
===================================================

Vor compila toare fișierele sursă până la fișiere obiect.

b. Legarea fișierelor obiect într-un fișier binar
=================================================

Vor obține fișierul binar din modulele obiect obținute anterior.

c. Modificarea fișierelor sursă și recompilarea lor
===================================================

Vor modifica fișierele sursă, vor recompila.

d. Ignorarea fișierelor obiect la comitere
==========================================

Scopul este să adauge o nouă intrare în fișierul .gitignore pentru a ignora 
fișierelor obiect.

e. Comiterea noilor modificări
==============================

Vor face iar 2 commit-uri: unul cu fișierul .gitignore și unul cu modificările din fișierele 
cod sursă.

f. Verificarea istoricului git
==============================

``git log``
