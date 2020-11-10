.. _improve_cli_inspect_files_summary:

Sumar: Inspectarea fișierelor
=============================


Inspectarea rapida a conținutului fișierelor
--------------------------------------------

Pentru a vedea rapid conținutul unui fișier folosim utlitarul ``less``.
În cadrul unei sesiuni ``less`` putem folosi aceeleași taste ca în cadrul sesiunii interactive ``man`` pentru navigarea în pagină:

* ``Arrow Down``/``Arrow Up`` sau ``j``/``k`` pentru a naviga, cu câte o linie, în jos, respectiv în sus; recomandăm utlizarea tastelor ``j``/``k`` pentru a fi mai eficienți
* Search (``/``, ``?``, ``n``, ``N``)
* Go up (``g``), go down (``G``)
* Help (``h``) pentru a afla mai multe despre cum putem folosi mai bine sesiunea interactivă
* Quit (``q``) pentru a ieși din sesiunea interactivă

Pentru a afișa pe ecran conținutul unui fișier folosim utlitarul ``cat``.

Pentru a afișa parțial conținutul unui fișier sau a extrage rezultatul unei comenzi folosim utilitarele ``head`` și ``tail``.

Căutarea în fișiere
-------------------

Folosim comanda ``grep`` pentru a căuta un *pattern* într-un fișier sau în rezultatul unei comenzi (cum ar fi ``cat``).
Modul de folosire este ``grep PATTERN cale/către/fișier`` sau ``cmd | grep PATTERN``.

Opțiuni uzuale ale ``grep``
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Folosim opțiunea ``-n`` pentru a afișa și numărul liniei care conține patternul căutat.

Implicit, grep caută în mod case-sensitive patternul.
Folosim opțiunea ``-i`` pentru a căuta patternul în mod case-insensitive.

Pentru a afișa toate liniile, mai puțin pe cele care conțin pattern, folosim opțiunea ``-v``.

Pentru a efectua o căutare recursivă folosim opțiunea ``-r``.

De cele mai multe ori vom folosi opțiunile ``-n``, ``-i`` și ``-r`` în aceelași timp.
Astfel avem o căutare cât mai cuprinzătoare și putem folosi funcția de căutare în sesiunea interactivă ``less`` pentru a găsi linia și fișierul care ne interesează.

Extra: Dacă dorim să căutăm cuvântul **search** folosim sintaxa ``\b`` (boundary) pentru a delimita patternul, ca în exemplul următor: ``grep -nri "\bsearch\b" workspace/C/ | less``.


Căutarea unei expresii regulate
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Pentru a căuta folosind o expresie regulată putem să folosim opțiunea ``-E`` a utilitarului ``grep``, sau forma prescurtată ``egrep``.

În cadrul unei expresii regulate, caracterul ``.`` poate fi înlocuit cu orice caracter.

În cadrul unei expresii regulate, caracterul ``+`` urmează întotdeauna un caracter sau o expresie și spune că expresia sau caracterul din stânga lui apare cel puțin o dată în patternul căutat.

În cadrul unei expresii regulate, caracterul ``*`` urmează întotdeauna un caracter sau o expresie și spune că expresia sau caracterul din stânga lui apare de oricâte ori, sau poate lipsi cu totul.

În cadrul unei expresii regulate, caracterul ``?`` urmează întotdeauna un caracter sau o expresie și spune că expresia sau caracterul din stânga lui apare cel mult o dată.

În cadrul unei expresii regulate, caracterul ``|`` separă două expresii și spune că poate să se potrivească expresia din stânga sau din dreapta lui.

În cadrul unei expresii regulate, folosim sintaxa ``[]`` pentru a defini o listă de caractere care pot fi folosite în înlocuire.
Această sintaxă înlocuiește exact un caracter din lista oferită.

Compararea fișierelor
---------------------

Comparăm două fișiere, octet cu octet, folosind utilitarul ``cmp``.

Comparăm textual două fișiere folosind utilitarul ``diff``.