.. _improve_cli_inspect_fs_summary:

Sumar: Inspectarea sistemului de fișiere
========================================

Sumar: Inspectarea paginilor de manual
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Navigarea prin paginile manualului: search (/, ?, n, N), go up (g), go down (G), help (h) în timp ce folosim comanda man pt a afla mai multe despre cum o putem folosi mai bine; bonus: j/k pt navigare jos/sus
* Prezentarea secțiunilor din manual: ``man printf`` vs ``man 3 printf``.
* Prezentarea pachetului ``tldr`` - poate fi util pentru cazurile uzuale, dar nu trebuie să ne fie frică să căutăm în ``man`` pentru detalii

Sumar: ``locate``
"""""""""""""""""

Folosim utilitarul ``locate`` pentru a căuta un fișier în întreg sistemul de fișiere.

Are avantajul că este foarte rapid, deoarece folosește o bază de date pentru a indexa fișierele.

Are două dezavantaje:
    #. Baza de date trebuie reconstruită periodic.
       Dacă vrem să reconstruim manual baza de date, avem nevoie de drepturi privilegiate pentru a rula comanda ``updatedb``.
    #. Utilitarul caută în tot sistemul de fișiere: nu putem să specificăm un punct de start pentru căutare.
       Este necesar să filtrăm rezultatul căutării cu punctul de start dorit, așa cum am făcut în exemplul de mai sus: ``| grep workspace/C``.

Sumar: ``find``
"""""""""""""""

Folosim ``find`` pentru a căuta după criterii mai complexe decât numele fișierului, cum ar fi tipul fișierului, data ultimei modificări, etc.

De cele mai multe ori vom folosi ``find`` în conjuncție cu opțiunea ``-exec`` pentru a rula o comandă asupra fișierelor găsite.

Utilitarul ``find`` este mai lent decât ``locate``, dar nu necesită o bază de date care trebuie actualizată periodic.
``locate`` este probabil suficient pentru majoritatea cazurilor când suntem interesați de căutarea unui fișier.
