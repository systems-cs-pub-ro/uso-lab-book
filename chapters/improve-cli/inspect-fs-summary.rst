.. _improve_cli_inspect_fs_summary:

Sumar: Inspectarea sistemului de fișiere
========================================

Inspectarea paginilor de manual
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Navigarea prin paginile manualului:

  * ``Arrow Down``/``Arrow Up`` sau ``j``/``k`` pentru a naviga, cu câte o linie, în jos, respectiv în sus; recomandăm utlizarea tastelor ``j``/``k`` pentru a fi mai eficienți
  * Search (``/``, ``?``, ``n``, ``N``)
  * Go up (``g``), go down (``G``)
  * Help (``h``) pentru a afla mai multe despre cum putem folosi mai bine sesiunea interactivă
  * Quit (``q``) pentru a ieși din sesiunea interactivă

* Prezentarea secțiunilor din manual: ``man printf`` vs ``man 3 printf``.

* Prezentarea pachetului ``tldr`` - poate fi util pentru cazurile uzuale, dar nu trebuie să ne fie frică să căutăm în ``man`` pentru detalii

Selectarea multiplor fișiere folosind globbing
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Folosim *globbing* pentru a selecta mai multe fișiere al căror nume corespunde unui tipar:

* Caracterul ``*`` poate fi înlocuit cu orice caracter de oricâte ori, sau poate lipsi cu totul.
* Caracterul ``?`` înlocuiește exact un caracter, oricare ar fi acela.
* Folosim sintaxa ``[]`` pentru a defini o listă de caractere care pot fi folosite în înlocuire.
* Folosim sintaxa ``{}`` pentru a defini o listă de cuvinte (grupuri de caractere) care pot fi folosite în înlocuire.
* Scăpăm de semnificația specială a unei expresii încadrând-o între ``"`` (ghilimele).

Căutarea unui fișier în sistem
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Utilitarul ``locate``
"""""""""""""""""""""

Folosim utilitarul ``locate`` pentru a căuta un fișier în întreg sistemul de fișiere.

Are avantajul că este foarte rapid, deoarece folosește o bază de date pentru a indexa fișierele.

Are două dezavantaje:
    #. Baza de date trebuie reconstruită periodic.
       Dacă vrem să reconstruim manual baza de date, avem nevoie de drepturi privilegiate pentru a rula comanda ``updatedb``.
    #. Utilitarul caută în tot sistemul de fișiere: nu putem să specificăm un punct de start pentru căutare.
       Este necesar să filtrăm rezultatul căutării cu punctul de start dorit, așa cum am făcut în exemplul de mai sus: ``| grep workspace/C``.

Utilitarul ``find``
"""""""""""""""""""

Folosim ``find`` pentru a căuta după criterii mai complexe decât numele fișierului, cum ar fi tipul fișierului, data ultimei modificări, etc.

De cele mai multe ori vom folosi ``find`` în conjuncție cu opțiunea ``-exec`` pentru a rula o comandă asupra fișierelor găsite.

Utilitarul ``find`` este mai lent decât ``locate``, dar nu necesită o bază de date care trebuie actualizată periodic.
``locate`` este probabil suficient pentru majoritatea cazurilor când suntem interesați de căutarea unui fișier.
j