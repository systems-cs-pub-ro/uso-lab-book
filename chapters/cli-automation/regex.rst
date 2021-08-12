Expresii regulate și `egrep`
============================

Expresii regulate
-----------------

Căutarea unei expresii regulate
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

În exemplele de până acum, patternul folosit era un cuvânt sau șir de caractere.
Folosind o expresie regulată, putem să căutăm după șiruri de caractere care se potrivesc cu descrierea dată în expresia regulată.

Ca și în cazul globbing, avem un set de caractere speciale în cazul expresiilor regulate.

.. warning::

    Expresiile regulate sunt diferite de globbing.
    Mare atenție să nu faceți confuzie între cele două.
    Vom vedea diferențele în continuare.

Pentru a căuta folosind o expresie regulată putem să folosim opțiunea ``-E`` a utilitarului ``grep``, sau forma prescurtată ``egrep``.

Scrieți într-un fișier numit ``demo-regex.txt`` textul de mai jos:

.. code-block:: bash

    Ana
    Ama
    Ioana
    a
    aa
    aaa
    aaabbb
    Ana are mere
    Ana mere are
    USO RUL3Z

Vom folosi fișierul ``demo-regex.txt`` în exemplele următoare.
Textul din fișier este un exemplu didactic.
Este scris în așa fel încât să putem exemplifica mai multe lucruri într-un mod ușor de urmărit.

Caracterul special ``.``
""""""""""""""""""""""""

.. note::

    Caracterul ``.`` reprezintă un caracter special în cadrul unei expresii regulate.
    Nu îl confundați cu directorul curent (reprezentat tot de caracterul ``.``) în contextul navigării sistemului de fișiere.

În cadrul unei expresii regulate, caracterul ``.`` poate fi înlocuit cu orice caracter.

Rulăm comanda din exemplul de mai jos:

.. code-block:: bash

    student@uso:~$ egrep "a.a" demo-regex.txt
    Ioana
    aaa
    aaabbb
    Ana are mere

Citim expresia regulată de mai sus în următorul mod: șirul ``a``, urmat de orice caracter, urmat de șirul ``a``.
Astfel, observăm cum caracterul ``.`` a înlocuit, pe rând, caracterele ``n``, ``a``, ``a`` și `` `` (space).

Caracterul special ``+``
""""""""""""""""""""""""

În cadrul unei expresii regulate, caracterul ``+`` urmează întotdeauna un caracter sau o expresie și spune că expresia sau caracterul din stânga lui apare cel puțin o dată în patternul căutat.

Rulăm comanda din exemplul de mai jos:

.. code-block:: bash

    student@uso:~$ egrep "aa+" demo-regex.txt
    aa
    aaa
    aaabbb

Citim expresia regulată de mai sus în următorul mod: șirul ``a``, urmat de caracterul ``a`` cel puțin o dată.
Astfel, observăm cum expresia a înlocuit orice șir care conținea cel puțin două apariții ale caracterului ``a``.

Pentru a specifica numărul de apariții pentru o expresie, aceasta trebuie încadrată între paranteze rotunde ``(EXP)+``, ca în exemplul de mai jos:

.. code-block:: bash

    student@uso:~$ egrep "(ab)+" demo-regex.txt
    aaabbb

Citim expresia regulată de mai sus în următorul mod: șirul ``ab`` trebuie să apară cel puțin o dată.

Caracterul special ``*``
""""""""""""""""""""""""

În cadrul unei expresii regulate, caracterul ``*`` urmează întotdeauna un caracter sau o expresie și spune că expresia sau caracterul din stânga lui apare de oricâte ori, sau poate lipsi cu totul.

Rulăm comanda din exemplul de mai jos:

.. code-block:: bash

    student@uso:~$ egrep "ab*" demo-regex.txt
    Ana
    Ama
    Ioana
    a
    aa
    aaa
    aaabbb
    Ana are mere
    Ana mere are

Citim expresia regulată de mai sus în următorul mod: șirul ``a``, urmat de caracterul ``b`` de oricâte ori.
Astfel, observăm cum expresia a înlocuit orice șir care conținea cel puțin o apariție a caracterului ``a``.

Caracterul special ``?``
""""""""""""""""""""""""

În cadrul unei expresii regulate, caracterul ``?`` urmează întotdeauna un caracter sau o expresie și spune că expresia sau caracterul din stânga lui apare cel mult o dată.

Rulăm comanda din exemplul de mai jos:

.. code-block:: bash

    student@uso:~$ egrep "a?" demo-regex.txt
    Ana
    Ama
    Ioana
    a
    aa
    aaa
    aaabbb
    Ana are mere
    Ana mere are
    USO RUL3Z

Citim expresia regulată de mai sus în următorul mod: șirul ``a`` apare cel mult o dată.
Astfel, observăm cum expresia a înlocuit orice șir care conținea cel mult o apariție a caracterului ``a``; textul "USO RUL3Z" respectă regula întrucât nu conține niciun caracter ``a``.

Caracterul special ``|``
""""""""""""""""""""""""

În cadrul unei expresii regulate, caracterul ``|`` separă două expresii și spune că poate să se potrivească expresia din stânga sau din dreapta lui.

Rulăm comenzile din exemplul de mai jos:

.. code-block:: bash

    student@uso:~$ egrep "Ana|Ama" demo-regex.txt
    Ana
    Ama
    Ana are mere
    Ana mere are
    student@uso:~$ egrep "(Ana)|(Ama)" demo-regex.txt
    Ana
    Ama
    Ana are mere
    Ana mere are

Citim expresia regulată de mai sus în următorul mod: șirul ``Ana`` **sau** șirul ``Ama``.
Astfel, observăm cum expresia a înlocuit orice șir care conținea fie ``Ana``, fie ``Ama``.
Mai observăm că cele două comenzi sunt echivalente.

Sintaxa specială ``[]``
"""""""""""""""""""""""

În cadrul unei expresii regulate, folosim sintaxa ``[]`` pentru a defini o listă de caractere care pot fi folosite în înlocuire.
Această sintaxă înlocuiește exact un caracter din lista oferită.
Ca și pentru globbing, sintaxa ``[]`` nu ne limitează la a oferi enumarații de caractere, și accepta și intervale, cum observăm în exemplul de mai jos:

.. code-block:: bash

    student@uso:~$ egrep "A[a-z]a" demo-regex.txt
    Ana
    Ama
    Ana are mere
    Ana mere are

Citim expresia regulată de mai sus în următorul mod: șirul ``A``, urmat de un caracter din intervalul ``a-z``, urmat de caracterul a.
Astfel, observăm cum expresia a înlocuit șirurile ``Ana`` și ``Ama``.

Exerciții
"""""""""

TODO