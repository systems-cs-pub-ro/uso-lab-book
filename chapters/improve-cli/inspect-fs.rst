Inspectarea sistemului de fișiere
=================================


Cea mai importantă comandă
--------------------------

Așa cum spuneam mai devreme, marele avantaj al utilizării terminalului este că ne ajută să rezolvăm sarcini foarte rapid.
Rezolvăm sarcini folosind utilitarele pe care le avem disponibile în linia de comandă, fie că acestea fac parte din sistemul nostru sau le-am instalat.

Cel mai important utilitar pe care îl avem la dispoziție este ``man``.
Utilitarul ``man`` ne deschide pagina de manual în care este documentat un alt utilitar pe care dorim să-l folosim.

.. code-block:: bash

    student@uso:~$ man
    What manual page do you want?

Putem consulta însăși pagina de manual a utilitarului ``man``

.. code-block:: bash

    student@uso:~$ man man

Vom fi întâmpinați de următorul program interactiv:

.. code-block:: bash

    MAN(1)                        Manual pager utils                        MAN(1)

    NAME
           man - an interface to the on-line reference manuals

    SYNOPSIS
           man  [-C  file]  [-d]  [-D]  [--warnings[=warnings]]  [-R encoding] [-L
           locale] [-m system[,...]] [-M path] [-S list]  [-e  extension]  [-i|-I]
           [--regex|--wildcard]   [--names-only]  [-a]  [-u]  [--no-subpages]  [-P
           pager] [-r prompt] [-7] [-E encoding] [--no-hyphenation] [--no-justifi‐
           cation]  [-p  string]  [-t]  [-T[device]]  [-H[browser]] [-X[dpi]] [-Z]
           [[section] page[.section] ...] ...
           man -k [apropos options] regexp ...
           man -K [-w|-W] [-S list] [-i|-I] [--regex] [section] term ...
           man -f [whatis options] page ...
           man -l [-C file] [-d] [-D] [--warnings[=warnings]]  [-R  encoding]  [-L
           locale]  [-P  pager]  [-r  prompt]  [-7] [-E encoding] [-p string] [-t]
           [-T[device]] [-H[browser]] [-X[dpi]] [-Z] file ...
           man -w|-W [-C file] [-d] [-D] page ...
           man -c [-C file] [-d] [-D] page ...
           man [-?V]

     Manual page man(1) line 1 (press h for help or q to quit)

Observăm că ultima linie din terminal, **Manual page man(1) line 1 (press h for help or q to quit)**, ne oferă mai multe informații:

* Ne aflăm pe prima linie din prima pagină a manualului
* Putem apăsa tasta ``h`` pentru a acesa meniul de ajutor
* Putem apăsa tasta ``q`` pentru a ieși din manual

Navigarea prin paginile manualului
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Pentru a naviga prin pagina de manual putem folosi tastele ``Arrow Down`` și ``Arrow Up`` pentru a naviga, cu câte o linie, în jos, respectiv în sus, în pagină.
Putem folosi tastele ``Pg Dn`` și ``Pg Up`` pentru a naviga, cu câte un ecran de terminal, în jos și în sus în pagină.
Pentru a naviga la începutul paginii putem folosi tasta ``g``, iar pentru a naviga la sfârșitul paginii folosim tasta ``G``.

.. note::

    Putem folosi tastele ``j`` și ``k`` ca alternative pentru ``Arrow Down`` și ``Arrow Up``.
    Astfel suntem mai rapizi pentru că nu ne mai mutăm mâna de pe tastele caractere.

De cele mai multe ori, atunci când consultăm pagina de manual a unui utilitar suntem interesați să aflăm dacă acesta expune o anumită funcționalitate și cum o putem folosim.
Decât să citim linie cu linie în căutarea funcționalității dorite, putem să folosim funcția de căutare a manualului:

#. Pentru a porni funcția de căutare apăsăm tasta ``/`` în sesiunea interactivă din ``man``.
#. În continuare vom introduce textul pe care dorim să-l căutăm: poate să fie un cuvântul cheie pe care îl știm deja sau orice text care sperăm că ne duce la rezultatul dorit.
#. Acum apăsăm tasta ``Enter``.
   Vom fi duși la primul rezultat care se potrivește căutării, dacă acesta există.
#. Dacă vrem să navigăm la următorul rezultat apăsăm tasta ``n``.
   Dacă vrem să navigăm la un rezultat anterior apăsăm tasta ``N``.

.. note::

    Căutarea are loc de la poziția curentă în pagină către sfârșitul paginii.
    Dacă am navigat deja în interiorul paginii, trebuie să avem în vedere că rezultatul de interes al căutării noastre se poate alfa undeva între începutul paginii și poziția noastră curentă.
    Putem folosi tasta ``?`` pentru a porni o căutare de la poziția curentă către începutul paginii.
    Alternativ, putem naviga la începutul paginii prin apăsarea unei singure taste (``g``) și apoi pornim căutarea ``/`` de acolo.

.. note::

    Căutarea este case-sensitive.
    Putem să schimbăm acest comportament prin introducerea opțiunii ``-I`` în sesiunea interactivă, înainte de a porni căutarea.
    Dacă doriți să aflați mai multe despre opțiunile pe care le putem introduce apăsați tasta ``h`` într-o sesiune interactivă și căutați textul "OPTIONS".

Interpretarea paginii de manual
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

La o primă vedere, textul paginii de manual poate fi intimidant; unele utilitare au mai multe opțiuni și argumente, unele opționale, altele nu.
O să trecem prin syntaxă și o să vedem că lucrurile sunt mult mai simple decât par.
Să analizăm pagina de manual a utilitarului ``ls``; ``man ls``:

.. code-block:: bash

    LS(1)                            User Commands                           LS(1)

    NAME
           ls - list directory contents

    SYNOPSIS
           ls [OPTION]... [FILE]...

    DESCRIPTION
           List  information  about  the FILEs (the current directory by default).
           Sort entries alphabetically if none of -cftuvSUX nor --sort  is  speci‐
           fied.

           Mandatory  arguments  to  long  options are mandatory for short options
           too.

           -a, --all
                  do not ignore entries starting with .

           -A, --almost-all
                  do not list implied . and ..

           --author
     Manual page ls(1) line 1 (press h for help or q to quit)

#. Prima secțiune care ne interesează este "DESCRIPTION".
   Citim descrierea și ne dăm seama dacă utilitarul ne va ajuta în rezolvarea sarcinii pe care o avem.
   În cazul utilitarului ``ls``, descrierea ne informează că acesta afișează informații despre fișierele din calea indicată, sau din directorul curent atunci când nu specificăm o cale.
   Informațiile sunt sortate alfabetic, dacă utilizatorul nu specifică altceva prin opțiunile disponibile.

#. Cea de-a doua secțiune care ne interesează este "SYNOPSIS".
   Aceasta ne spune cum putem să rulăm utilitarul, ce opțiuni și argumente sunt opționale (pot lipsi) și ce opțiuni și argumente sunt obligatorii.

   .. code-block:: bash

       SYNOPSIS
              ls [OPTION]... [FILE]...

   Sintaxa **[ ]** ne spune că acea categorie este opțională.
   Astfel, pentru ``ls``, deducem că atât opțiunile (``[OPTION]...``) cât și argumentele (``[FILE]...``, calea către fișiere sau directoare) sunt opționale.
   Cele trei puncte ``...`` înseamnă mai multe din categoria precedentă: deci ``[OPTION]...`` înseamnă că nu suntem limitați la o singură opțiune, dar opțiunile pot să și lipsească în totalitate datorită **[ ]**.

   .. note::

       Am menționat că o comandă poate avea atât opțiuni, cât și argumente.
       Opțiunile îi spun unei comenzi cum să își modifice comportamentul, și de obicei sunt precedate de ``-`` (ex. ``-l``, ``--verbose``, etc.).
       Argumentele îi spun unei comenzi pe ce să acționeze.

       În exemplul de mai jos:

       .. code-block:: bash

           student@uso:~$ ls -l Desktop/

       Avem utilitarul ``ls`` care primește opțiunea ``-l`` și argumentul ``Desktop/``.

#. Ultima observație pe care o facem este că opțiunile unei comenzi pot avea o formă prescurtată, ``-a``, sau o formă lungă, ``--all``.
   Nu este obligatoriu ca o opțiune să expună ambele forme, deși majoritatea o fac.
   Opțiunile în formă prescurtată pot fi concatenate și precedate de un singur ``-``, ca în exemplul de mai jos:

   .. code-block:: bash

       student@uso:~$ ls -la Desktop/

Utilizarea secțiunilor din manual
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

În descrierea manualului (``man man``) este specificat faptul că manualul este împărțit în diferite secțiuni:

.. code-block:: bash

    The table below shows the section numbers of the manual followed by the types of pages they contain.

    1   Executable programs or shell commands
    2   System calls (functions provided by the kernel)
    3   Library calls (functions within program libraries)
    4   Special files (usually found in /dev)
    5   File formats and conventions eg /etc/passwd
    6   Games
    7   Miscellaneous (including macro packages and conventions), e.g. man(7), groff(7)
    8   System administration commands (usually only for root)
    9   Kernel routines [Non standard]

Ce este important de reținut aici este că folosind ``man`` putem afla informații despre funcții de bibliotecă și de sistem, și multe altele, nu doar despre utilitare și comenzi shell.
Totul este mai clar cu un exemplu.
Dacă rulăm comanda ``man printf`` se va deschide pagina următoare din manual:

.. code-block:: bash

    PRINTF(1)                        User Commands                       PRINTF(1)

    NAME
           printf - format and print data

    SYNOPSIS
           printf FORMAT [ARGUMENT]...
           printf OPTION

    DESCRIPTION
           Print ARGUMENT(s) according to FORMAT, or execute according to OPTION:

           --help display this help and exit

           --version
                  output version information and exit

           FORMAT controls the output as in C printf.  Interpreted sequences are:

           \"     double quote

           \\     backslash

     Manual page printf(1) line 1 (press h for help or q to quit)

Această pagină este pentru utilitarul ``printf``.
Observați prima linie:

.. code-block:: bash

    PRINTF(1)                        User Commands                       PRINTF(1)

Textul **PRINTF(1)** ne spune că ne uităm la pagina de manual a utilitarului ``printf`` din secțiunea **(1)** a manualului.
Exact cum ne spune descrierea din manual:

.. code-block:: bash

    1   Executable programs or shell commands

Dacă vrem să accesăm pagina de manual a funcției ``printf`` a bibliotecii standard C, folosim comanda ``man 3 printf`` și vom fi găsi pagina următoare din manual:

.. code-block:: bash

    PRINTF(3)                  Linux Programmer's Manual                 PRINTF(3)

    NAME
           printf,   fprintf,   dprintf,  sprintf,  snprintf,  vprintf,  vfprintf,
           vdprintf, vsprintf, vsnprintf - formatted output conversion

    SYNOPSIS
           #include <stdio.h>

           int printf(const char *format, ...);
           int fprintf(FILE *stream, const char *format, ...);
           int dprintf(int fd, const char *format, ...);
           int sprintf(char *str, const char *format, ...);
           int snprintf(char *str, size_t size, const char *format, ...);

           #include <stdarg.h>

           int vprintf(const char *format, va_list ap);
           int vfprintf(FILE *stream, const char *format, va_list ap);
           int vdprintf(int fd, const char *format, va_list ap);
           int vsprintf(char *str, const char *format, va_list ap);
           int vsnprintf(char *str, size_t size, const char *format, va_list ap);

     Manual page printf(3) line 1 (press h for help or q to quit)

Observăm că s-a căutat în secțiunea **(3)** din manual:

.. code-block:: bash

    3   Library calls (functions within program libraries)

Sumar: Inspectarea paginilor de manual
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Navigarea prin paginile manualului: search (/, ?, n, N), go up (g), go down (G), help (h) în timp ce folosim comanda man pt a afla mai multe despre cum o putem folosi mai bine; bonus: j/k pt navigare jos/sus
* Prezentarea secțiunilor din manual: ``man printf`` vs ``man 3 printf``.
* Prezentarea pachetului ``tldr`` - poate fi util pentru cazurile uzuale, dar nu trebuie să ne fie frică să căutăm în ``man`` pentru detalii


Comanda ``cd``
--------------

Shortcut-uri pt cd: `cd` echivalent cu `cd ~`, `cd -` pt a sări la calea anterioară.

* Recapitulare căi absolute vs căi relative?


Comanda ``ls``
--------------

``ls, ls -a, ls -l, ls -ld``

Globbing
^^^^^^^^

Ce este globbing?

Folosire caractere ``*``, ``?``, [seturi] și {liste,grupuri}, escaping folosind ``“`` ex.
::

	ls “[USO] file”


``find`` și ``locate``
----------------------

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


``file`` și ``touch``
---------------------

În contextul ăsta arătăm că touch actualizează data ultimei modificări pentru un fișier existent


Bonus: procfs
-------------
