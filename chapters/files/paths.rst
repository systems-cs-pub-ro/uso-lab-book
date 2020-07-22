Căi absolute și relative
========================

1) Calea curentă
----------------

Calea curentă se afișează folosind utilitarul ``pwd``. Etimologia comenzii
provine din engleză - *Print Working Directory*. Acesta afișează calea
completă de la rădăcină; aceasta este o cale **absolută**. Putem învăța
mai multe detalii despre comandă uitându-ne în manual ``man pwd``.


**Exercițiu:** Afișați calea curentă.

2) Cale relativă și cale absolută
---------------------------------

În sistemul de fișiere, ne putem referi la un fișier prin 2 modalități:
folosind **calea relativă** sau folosind **calea absolută**. Pentru o mai bună
înțelegere, o să folosind un exemplu din viața noastră. Considerând un
serial pe Netflix, putem să ne referim la un episod în 2 moduri:

#. Față de început - primul episod (în mod absolut): *În episodul 213 s-a întâmplat X.*
#. Față de episodul la care ne aflăm (în mod relativ): *În urmă cu 3 episoade s-a întâmplat Y.*

Similar, ne referim la un fișier:

1. Pornind de la **/** (root), directorul de început - **cale absolută**.
2. Pornind de la directorul curent - **cale relativă**.

3) Schimbarea căii curente
--------------------------

Calea curentă de schimbă folosind utilitarul **cd**. Etimologia comenzii
provine din engleză - *Change Directory*. Putem învăța mai multe detalii
despre comandă folosind manualul ``man cd``. Acesta primește ca prim
parametru o cale, iar efectul comenzii constă în schimbarea căii curente.
Putem folosi atât cale absolută, cât și cale relativă.

**Exercițiu:** Schimbați directorul curent în **/tmp** folosind cale relativă.

4) Scurtături de căi
--------------------

Pentru o eficiență mai bună, putem folosi simboluri pentru interacțiunea cu
utilitarul ``cd``:

* Folosim **-** pentru a referi la **calea anterioară**.
* Folosim **~** pentru a referi **calea home** a utilizatorului.

**Exercițiu:** Mergeți la calea anterioară.
**Exercițiu:** Schimbați directorul curent în **/tmp** folosind cale absolută.
**Exercițiu:** Schimbați directorul curent în calea home a utilizatorului curent.
