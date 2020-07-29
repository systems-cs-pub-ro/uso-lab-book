Inspectarea fișierelor
======================


1) Inspectarea rapida a conținutului fișierelor
-----------------------------------------------

``cat, head, tail, less, cat | less, view``

* Navigarea în less: ca la man; bonus: reload (:Examine non_existing_file, ex. :e ee)
* Încurajați să folosească less în loc de cat pt a inspecta un fișier: așa își păstrează consola curată și pot urmări mai ușor ce comenzi au dat și care au fost rezultatele


2) Compararea fișierelor
------------------------

* ``cmp``
* ``diff``
* Bonus: ``vimdiff``


3) Căutarea în fișiere
----------------------

Opțiuni uzualre pentru ``grep``:

* ``-n``
* ``-r``
* ``-i``
* ``-v``

Expresii regulate uzuale: ``.``, ``+``, ``?``, ``*``, ``[seturi]``, ``|``

* Utilizare ``grep -e`` sau ``egrep``
