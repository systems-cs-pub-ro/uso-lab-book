Inspectarea sistemului de fișiere
=================================


1) Cea mai importantă comandă
-----------------------------

Comanda ``man``, ``man man``.

* Prezentarea secțiunilor din manual: ``man printf`` vs ``man 3 printf``.
* Navigarea prin paginile manualului: search (/, ?, n, N), go up (g), go down (G), help (h) în timp ce folosim comanda man pt a afla mai multe despre cum o putem folosi mai bine; bonus: j/k pt navigare jos/sus
* Prezentarea pachetului ``tldr`` - poate fi util pentru cazurile uzuale, dar nu trebuie să ne fie frică să căutăm în ``man`` pentru detalii


2) Comanda ``cd``
-----------------

Shortcut-uri pt cd: `cd` echivalent cu `cd ~`, `cd -` pt a sări la calea anterioară.

* Recapitulare căi absolute vs căi relative?


3) Comanda ``ls``
-----------------

``ls, ls -a, ls -l, ls -ld``

a. Globbing
^^^^^^^^^^^

Ce este globbing?

Folosire caractere ``*``, ``?``, [seturi] și {liste,grupuri}, escaping folosind ``“`` ex.
::

	ls “[USO] file”


4) ``find`` și ``locate``
-------------------------

``find``

* La ce este util și cum îl folosim
* Exerciții folosind ``find``: toate fișierele de tip **regular file** (trebuie să folosească ``man find``)
* Follow-up la exercițiul anterior: rulat comenzi pe fișierele respective
	* În cazul ăsta vom da un ``ls -l``
	* Exercițiul ăsta pune o bază. O să folosesc asta pentru a da search&replace recursiv folosind ``find`` și ``sed``

``locate``

* Ce este?
* Q: De ce îl folosim? A: Mai semnificativ mai rapid decât find
* Q: Ce dezavantaj are? A: Trebuie reconstruită baza de date periodic

* Takeaway: ``locate`` este probabil sufient pentru majoritatea cazurilor; folosim ``find`` atunci când vrem să căutăm după criterii mai complexe (ex. tipul fișierelor, data creării/ultimei modificări, etc.) sau dacă vrem să rulăm o comandă pe fișierele găsite


5) ``file`` și ``touch``
------------------------

În contextul ăsta arătăm că touch actualizează data ultimei modificări pentru un fișier existent


6) Bonus: procfs
----------------
