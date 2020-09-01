.. _improve_cli_inspect_fs:

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

Bonus: Utilizarea pachetului ``tldr``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Utilitarul ``tldr`` (too long, didn't read) oferă o versiune simplificată a paginilor de manual.
Acesta ne va arăta un rezumat al utilizării unei comenzi cu opțiunile cele mai des folosite în comunitate.

.. code-block:: bash

    student@uso:~$ tldr ls
    ls
    List directory contents.

     - List files one per line:
       ls -1

     - List all files, including hidden files:
       ls -a

     - Long format list (permissions, ownership, size and modification date) of all files:
       ls -la

     - Long format list with size displayed using human readable units (KB, MB, GB):
       ls -lh

     - Long format list sorted by size (descending):
       ls -lS

     - Long format list of all files, sorted by modification date (oldest first):
       ls -ltr

.. note::

    Acesta trebuie tratat ca un cheatsheet accesibil din linie de comandă.
    ``tldr`` nu elimină utilizarea paginilor ``man``, dar ne ajută să găsim rapid opțiunile uzuale.
    Acestea fiind spuse, vă recomandăm ca întotdeaună să citiți și să înțelegeți din paginile ``man`` ce efect au opțiunile unei comenzi înainte de a le folosi.
    Feriți-vă să rulați comenzi orbește, pentru că așa ați găsit pe StackOverflow, tldr, etc.
    Întotdeauna asigurați-vă că ați înțeles cum și de ce rulați comanda și abia apoi treceți la fapte.

Utilizarea pachetului ``tldr``
""""""""""""""""""""""""""""""

Instalați pachetul ``tldr`` pe mașina voastră.

#. Accesați pagina ``tldr`` a utilitarului ``ls``.

#. Accesați pagina ``tldr`` a utilitarului ``zip``.

#. Accesați pagina ``tldr`` a utilitarului ``tar``.

#. Accesați pagina ``tldr`` a utilitarului ``git``.

#. Accesați pagina ``tldr`` a utilitarului ``man``.

Sumar: Inspectarea paginilor de manual
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Navigarea prin paginile manualului: search (/, ?, n, N), go up (g), go down (G), help (h) în timp ce folosim comanda man pt a afla mai multe despre cum o putem folosi mai bine; bonus: j/k pt navigare jos/sus
* Prezentarea secțiunilor din manual: ``man printf`` vs ``man 3 printf``.
* Prezentarea pachetului ``tldr`` - poate fi util pentru cazurile uzuale, dar nu trebuie să ne fie frică să căutăm în ``man`` pentru detalii


Navigarea sistemului de fișiere: comanda ``cd``
-----------------------------------------------

Comanda ``cd`` este una dintre cele mai folosite comenzi.
Funcționalitatea este în numele ei, **cd** fiind o abreviere pentru **change directory**.
Este esențial să ne simțim foarte comfortabili atunci când navigăm prin sistemul de fișiere.

Navigarea eficientă folosind ``cd``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Întotdeauna când deschidem un terminal o facem pentru că vrem să realizăm o sarcină: vrem să redenumim rapid ultimele poze făcute cu telefonul de la genericul **DCIM1001** la ceva util **Excursie Sinaia, Ian 2020, 1001**, vrem să ne testăm proiectul și să urcăm modificările pe GitHub, etc.

Pentru a ne realiza sarcina, vrem să navigăm în directorul în directorul în care ne-am salvat pozele.
Primul pas este să aflăm directorul curent în care ne aflăm.
Facem asta folosind comanda ``pwd``, acronim pentru print working directory.

.. code-block:: bash

    student@uso:~$ pwd
    /home/student

Observăm că ne aflăm în directorul **home** al utilizatorului **student**.
Ne vom muta în directorul în care avem pozele

.. code-block:: bash

    student@uso:~$ cd Pictures/Sinaia/
    student@uso:~/Pictures/Sinaia$

.. note::

    Observați că rezultatul comenzii ``pwd`` este o cale absolută ``/home/student``.
    O cale absolută este o cale care începe cu ``/``, adică cu directorul **root** care este rădăcina sistemului nostru de fișiere.

    Observați calea oferită comenzii ``cd``: ``Pictures/Sinaia/``.
    Aceasta nu începe cu directorul rădăcină ``/``, deci este o cale relativă la directorul în care ne aflam, adică relativă la ``/home/student``.

Acum ne aflăm în directorul pozelor.
Verificăm folosind ``pwd``

.. code-block:: bash

    student@uso:~/Pictures/Sinaia$ pwd
    /home/student/Pictures/Sinaia

În cazul de față, această verificare este redundantă deoarece avem această informație afișată în prompt: ``student@uso:~/Pictures/Sinaia``.
Remarcați faptul că în prompt, calea este afișată ``~/Pictures/Sinaia``.
Este afișată așa deoarece caracterul ``~`` (tilda) este o scurtătură pentru directorul home al utilizatorului curent, în cazul nostru ``/home/student``.

.. tip::

    Scurtătura ``~`` este disponibilă pentru orice comandă, nu doar pentru ``cd``.
    De înlocuirea ei se ocupă terminalul înainte de a executa comanda.

Putem să revenim în directorul nostru home folosindu-ne de scurtătura ``~``

.. code-block:: bash

    student@uso:~/Pictures/Sinaia$ cd ~
    student@uso:~$

Un mijloc și mai scurt prin care putem să revenim în directorul nostru home este să executăm comanda ``cd`` fără nici un argument.

.. note::

    Comenzile ``cd`` și ``cd ~`` sunt echivalente.
    În practică, folosim comanda ``cd`` simplă pentru a naviga în directorul home al utilizatorului curent.

Folosim ``~`` pentru a construi o cale absolută, care are ca punct de plecare directorul home al utilizatorului curent, așa cum putem vedea în exemplul de mai jos:

.. code-block:: bash

    student@uso:~/workspace/uni/programming/labs/lab01$ pwd
    /home/student/workspace/uni/programming/labs/lab01
    student@uso:~/workspace/uni/programming/labs/lab01$ cd ~/Pictures/Sinaia
    student@uso:~/Pictures/Sinaia$ cd -
    student@uso:~/workspace/uni/programming/labs/lab01$ cd ../../../../../Pictures/Sinaia
    student@uso:~/Pictures/Sinaia$

Observăm că sintaxa ``cd ~/Pictures/Sinaia`` este mult mai scurtă și simplă de urmărit față de alternativa ``cd ../../../../../Pictures/Sinaia``.

În exemplul de mai sus am folosit o altă scurtătură pusă la dispoziție de comanda ``cd``, anume ``cd -``.
Comanda ``cd -`` are ca efect navigarea în directorul anterior, așa cum am văzut în exemplul anterior când am folosit-o pentru a reveni în directorul ``/home/student/workspace/uni/programming/labs/lab01``.

Exersarea navigării în cardul sistemului de fișiere
"""""""""""""""""""""""""""""""""""""""""""""""""""

Prin exercițiile care urmează o să ne exersăm mâna astfel încât să devenim cât mai comfortabili cu navigarea prin sistemul de fișiere.
Trebuie să ne fie foarte clar când folosim o cale absolută, când folosim una relativă și să devenim din ce în ce mai rapizi.

.. tip::

    O să folosim tasta ``Tab`` de fiecare dată când navigăm prin sistemul de fișiere.
    Nu doar că ne ajută să scriem mai rapid calea, dar în cazul în care nu se execută funcția de auto-complete înseamnă că cel mai probabil avem o greșeală undeva în calea introdusă manual.

.. note::

    Dacă nu aveți pe sistem una din căile folosite în exerciții, creați-o.

#. Navigați în directorul rădăcină (``/``) al sistemului vostru.
   De aici, navigați în directorul ``/home/student/Pictures`` (folosiți tasta ``Tab`` pentru auto-completion).
   Reveniți în directorul rădăcină folosind ``-``.
   Reveniți în directorul ``Pictures/`` folosind ``-``.
   Navigați în directorul home folosind doar comanda ``cd``.

#. Navigați în directorul ``~/workspace/uni/programming/labs/lab01``.
   De aici, navigați în directorul ``~/workspace/uni/programming/`` folosind o cale relativă (Obs: calea voastră **NU** trebuie să înceapă cu directorul rădăcină, ``/``).
   Navigați în directorul ``~/Downloads`` folosind o cale relativă.
   Reveniți în directorul ``~/workspace/uni/programming/labs/lab01``.

#. Navigați în directorul ``~/Documents`` folosind o cale absolută (Obs: calea voastră **trebuie** să înceapă cu directorul rădăcină, ``/``).
   Navigați în directorul ``~/Desktop`` folosind o cale absolută.
   Navigați în directorul ``~/Music`` folosind o cale relativă.


Explorarea sistemului de fișiere: comanda ``ls``
------------------------------------------------

Comanda ``ls`` este și ea una dintre cele mai folosite comenzi.
Funcționalitatea este în numele ei, **ls** fiind o abreviere pentru **list**.
Folosim ``ls`` pentru a afișa mai multe informații despre conținutul unui director sau despre fișiere.

Comanda poate fi folosită fără nici un argument, ca în exemplul de mai jos:

.. code-block:: bash

    student@uso:~$ ls
    Desktop    Downloads  Pictures  Templates  examples.desktop  vm-actions-log.txt
    Documents  Music      Public    Videos     uso.git           workspace

Observă că ``ls`` ne-a afișat conținutul directorului în care ne aflăm, în exemplul de mai sus este directorul home (``~``).
``ls`` poate să primească ca argument calea către unul sau mai multe fișiere și directoare, așa vedem în exemplul de mai jos:

.. code-block:: bash

    student@uso:~$ ls workspace/ Downloads/ examples.desktop nonexistent
    ls: cannot access 'nonexistent': No such file or directory
    examples.desktop

    Downloads/:

    workspace/:
    hello  uso-lab-book

Atunci când argumentul este un director, ne este afișat conținutul acestuia, așa cum se întâmplă pentru directoarele ``workspace/`` și ``Downloads``.
Atunci când argumentul este un fișier, acesta este afișat, așa cum este cazul pentru ``examples.desktop``.
Observăm că în cazul folosim ca argument o cale către un fișier sau director care nu există (``nonexistent`` în exemplul de mai sus) utilitarul ``ls`` nu își oprește execuția.
Acesta afișează un mesaj de eroare pentru argumentul în cauză și apoi își continuă execuția cu restul argumentelor.

Afișarea fișierelor ascunse
^^^^^^^^^^^^^^^^^^^^^^^^^^^

În mediul linux, un fișier este ascuns dacă numele său începe cu caracterul ``.`` (punct).
În mod implicit, utilitarul ``ls`` omite fișierele ascunse.
Pentru a afișa fișierele ascunse folosim opțiunea ``-a`` (all).

.. code-block:: bash

    student@uso:~$ ls -a
    .              .emacs.d         .ssh                       Pictures
    ..             .gconf           .sudo_as_admin_successful  Public
    .ICEauthority  .gitconfig       .tmux                      Templates
    .bash_aliases  .gnome2          .tmux.conf                 Videos
    .bash_history  .gnome2_private  .vim                       examples.desktop
    .bash_logout   .gnupg           .viminfo                   uso.git
    .bashrc        .java            .vimrc                     vm-actions-log.txt
    .cache         .lesshst         Desktop                    workspace
    .config        .local           Documents
    .dbus          .mozilla         Downloads
    .emacs         .profile         Music

Observăm că avem o mulțime de fișiere ascunse prezente în directorul nostru home.
Multe dintre acestea sunt fișiere de configurare (``.bashrc``, ``.vimrc``, etc.) folosite de diferite programe instalate pe sistemul nostru.
Vom vorbi mai multe despre acestea în viitorul apropriat.

Afișarea informațiilor extinse despre fișiere
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

De cele mai multe ori suntem interesați să aflăm mai multe informații despre fișiere: cum ar fi tipul fișierului, permisiuni, ownership, dimensiunea și data ultimei modificări.
Toate acestea sunt afișate prin utilizarea opțiunii ``-l``:

.. code-block:: bash

    student@uso:~$ ls -l
    total 60
    drwxr-xr-x  2 student student 4096 aug  6  2018 Desktop
    drwxr-xr-x  3 student student 4096 aug 20  2018 Documents
    drwxr-xr-x  2 student student 4096 aug 11 19:35 Downloads
    drwxr-xr-x  2 student student 4096 aug  6  2018 Music
    drwxr-xr-x  3 student student 4096 aug 31 23:26 Pictures
    drwxr-xr-x  2 student student 4096 aug  6  2018 Public
    drwxr-xr-x  2 student student 4096 aug  6  2018 Templates
    drwxr-xr-x  2 student student 4096 aug  6  2018 Videos
    -rw-r--r--  1 student student 8980 aug  6  2018 examples.desktop
    drwxr-xr-x 14 student student 4096 aug 20  2018 uso.git
    -rw-r--r--  1 student student 4827 aug 21  2018 vm-actions-log.txt
    drwxr-xr-x  4 student student 4096 aug 13 18:38 workspace

Vom analiza informațiile afișate pentru directorul **Desktop**.

.. code-block:: bash

    drwxr-xr-x  2 student student 4096 aug  6  2018 Desktop

#. Vom începe cu prima coloană din exemplul de mai sus: ``drwxr-xr-x``.
   Aceasta este formată din zece caractere care formează patru grupuri:

   #. Primul grup este format dintr-un singur caracter, și denotă tipul fișierului.
      În cazul de față, caracterul ``d`` ne informează că ne uităm la un fișier de tip director.
      În cazul fișierelor obișnuite (text, imagini, etc.) primul caracter este ``-``, așa cum putem observa în cazul fișierului ``examples.desktop``.

   #. Cel de-al doilea grup este format din următoarele trei caractere și denotă permisiunile pe care le are utilizatorul care deține fișierul asupra fișierului.
      Caracterele sunt în ordine ``r`` (read) permisiuni de citire, ``w`` (write) permisiuni de scriere și ``x`` (execute) permisiuni de rulare.
      Dacă utilizatorul nu are o anumită permisiune, caracterul corespunzător este înlocuit de caracterul ``-``.
      Spunem că aceste permisiuni se aplică pentru **User**.

   #. Cel de-al treilea grup este format din următoarele trei caractere și denotă permisiunile pe care le au membrii grupului care dețin fișierul asupra fișierului.
      Permisiunile rămân din setul ``rwx``.
      Spunem că aceste permisiuni se aplică pentru **Group**.

   #. Cel de-al patrulea grup este format din ultimele trei caractere și denotă permisiunile pe care le are orice utilizator care nu deține fișierul și nici nu face parte din grupul care deține fișierul.
      Permisiunile rămân din setul ``rwx``.
      Spunem că aceste permisiuni se aplică pentru **Others**.

   Acum, pe baza informațiilor din prima coloană, putem spune următoarele despre fișierul Desktop:

   #. Acesta este un fișier de tip director (``d``)
   #. Utilizatorul care îl deține are drepturi de citire (``r``), scriere (``w``) și execuție (``x``)
   #. Grupul care îl deține are drepturi de citire (``r``), **NU** are drepturi de scriere (``-``) și are drepturi de execuție (``x``)
   #. Iar orice alt utilizator are drepturi de citire (``r``), **NU** are drepturi de scriere (``-``) și are drepturi de execuție (``x``).

   .. note::

       Pentru a putea deschide un director este necesar să avem drepturi de execuție (``x``) asupra acestuia.
       Trebuie să avem drepturi de execuție indiferent că vrem să navigăm în interiorul său, să afișăm conținutul directorului sau să creăm noi fișiere și directoare în cadrul acestuia.

#. Cea de-a treia coloană ne spune care este utilizatorul care deține fișierul.
   Astfel observăm că directorul **Desktop** este deținut de către utilizatorul ``student``.
   Asta înseamnă că permisiunile ``rwx`` corespund utilizatorului ``student``.

#. Cea de-a patra coloană ne spune care este grupul care deține fișierul.
   Astfel observăm că directorul **Desktop** este deținut de către grupul ``student``.
   Asta înseamnă că permisiunile ``r-x`` se aplică oricărui utilizator care este membru al grupului ``student``.

#. Cea de-a cincea coloană ne arată dimensiunea fișierului, exprimată în octeți.
   Putem să-i cerem utilitarului ``ls`` să ne afișeze dimensiunea folosind multiplii (K(ilo), M(ega), G(iga), etc) utilizând opțiunea ``-h`` (human readable)

   .. code-block:: bash

       student@uso:~$ ls -lh
       total 60K
       drwxr-xr-x  2 student student 4,0K aug  6  2018 Desktop
       [...]

#. Ultimele coloane ne arată data ultimei modificări, în ordinea lună, zi, an.

Afișarea informațiilor extinse despre un fișier de tip director
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

Am observat că, în mod implicit, utilitarul ``ls`` ne afișază informații despre conținutul unui director atunci când primește calea către un director ca argument:

.. code-block:: bash

    student@uso:~$ ls -l Desktop/
    total 0
    -rw-r--r-- 1 student student 0 sep  2 19:39 todos.txt

Pentru a-i specifica lui ``ls`` că suntem interesați de informații despre fișierul de tip director, și nu despre conținutul său, folosim opțiunea ``-d``.

.. code-block:: bash

    student@uso:~$ ls -ld Desktop/
    drwxr-xr-x 2 student student 4096 sep  2 19:39 Desktop/

#. Afișați conținutul directoarelor ``/home``, ``Downloads`` și ``/tmp``.

#. Aflați care sunt permisiunile pe care le are orice utilizator asupra directoarelor ``/home``, ``/home/student`` și ``/tmp``.

Selectarea multiplor fișiere folosind globbing
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Până acum am aplicat diferite comenzi fie pe fișiere individuale, fie pe întreg directorul.
Foarte des vom avea nevoie de un mijloc prin care să putem selecta un număr variabil de fișiere care au un nume care corespunde unui tipar (pattern) comun.

Să revenim la scenariul prezentat anterior: vrem să selectăm pozele din excursia din Sinaia.
În directorul în care avem pozele din excursie avem și alte poze de la alte evenimente.
Știm că pozele din excursie încep toate cu numele **DCIM** și apoi sunt urmate de un număr.
Ceea ce vrem să facem este să selectăm toate pozele al căror nume corespunde acestui tipar și să le mutăm într-un director separat.
Pentru asta folosim globbing, ca în exemplul de mai jos:

.. code-block:: bash

    student@uso:~/Pictures$ mv DCIM* excursie-Sinaia-2020/

Observăm argumentul pe care l-am dat comenzii ``mv``, și anume ``DCIM*``.
Expresia ``DCIM*`` este un exemplu de globbing: adică o expresie care descrie un tipar prin folosirea unor caractere speciale, așa cum este caracterul ``*``.
În cazul de față, expresia ``DCIM*`` înseamnă orice fișier care începe cu șirul de caractere ``DCIM``.

Caracterul special ``*``
""""""""""""""""""""""""

În sintaxa globbing, caracterul ``*`` poate fi înlocuit cu orice caracter de oricâte ori, sau poate lipsi cu totul.
În directorul vostru home (``~``), executați următoarele comenzi:

.. code-block:: bash

    student@uso:~$ ls
    Desktop    Downloads  Pictures  Templates  examples.desktop  vm-actions-log.txt
    Documents  Music      Public    Videos     uso.git           workspace

    student@uso:~$ ls -d D*
    Desktop  Documents  Downloads

    student@uso:~$ ls -d Music*
    Music

Observăm că în expresia ``D*``, caracterul ``*`` înglobează toate caracterele care urmează literei **D**: "esktop", "ocuments" și "ownloads".
Observăm că în cazul expresie ``Music*``, ``*`` nu ține locul nici unui caracter.


Caracterul special ``?``
""""""""""""""""""""""""

În sintaxa globbing, caracterul ``?`` înlocuiește exact un caracter, oricare ar fi acela.
În directorul vostru home (``~``), executați următoarele comenzi:

.. code-block:: bash

    student@uso:~$ ls -d Musi?
    Music

    student@uso:~$ ls -d Mus??
    Music

    student@uso:~$ ls -d Music?
    ls: cannot access 'Music?': No such file or directory

Observăm că expresiile ``Musi?`` și ``Mus??`` s-au înlocuit cu succes cu numele directorului ``Music``, dar expresia ``Music?`` a generat o eroare deoarece nu există nici un fișier **Music** urmat de un caracter.


Sintaxa specială ``[]``
"""""""""""""""""""""""

În sintaxa globbing, folosim sintaxa ``[]`` pentru a defini o listă de caractere care pot fi folosite în înlocuire.
Această sintaxă înlocuiește exact un caracter din lista oferită.
În directorul vostru home (``~``), executați următoarele comenzi:

.. code-block:: bash

    student@uso:~$ ls -d Mus[ijk]c
    Music

    student@uso:~$ ls -d Mus[abc]c
    ls: cannot access 'Mus[abc]c': No such file or directory

În expresia ``Musi[ijk]c``, i-am "spus" shellului că al patrulea caracter poate să fie oricare din lista ``[ijk]``.
În acest context, globbing a găsit cu succes numele fișierului **Music**.
În expresia ``Musi[abc]c``, i-am "spus" shellului că al patrulea caracter poate să fie oricare din lista ``[abc]``.
Deoarece nu avem niciun fișier numit **Musac**, **Musbc** sau **Muscc**, comanda ne-a afișat mesajul de eroare corespunzător.

Sintaxa ``[]`` nu ne limitează la a oferi enumarații de caractere, așa cum am făcut cu ``[ijk]`` sau ``[abc]``.
Sintaxa accepta și intervale, cum observăm în exemplul de mai jos:

.. code-block:: bash

    student@uso:~$ ls -d Mus[A-Za-z0-9]c
    Music

Citim expresia ``[A-Za-z0-9]`` în următorul mod: această expresie înlocuiește un caracter din intervalul ``A-Z`` sau din intervalul ``a-z`` sau din intervalul ``0-9``; cu alte cuvinte înlocuiește un caracter alfa-numeric.

.. note::

    Folosim forma ``A-Za-z`` pentru a spune orice caracter din alfabetul englez, indiferent dacă este majusculă sau nu.
    Nu putem folosi forma ``A-z`` datorită reprezentării caracterelor în tabelul ascii.
    Caracterele **A-Z** sunt reprezentate în intervalul **65-90**, iar caracterele **a-z** în intervalul **97-122** în tabelul ascii.
    Dacă am folosi forma **A-z**, i-am spune expresiei globbing să includă și caracterele din intervalul **91-96** din tabelul ascii în expresia noastră.

.. tip::

    Folosind sintaxa ``[]`` putem rescrie mutarea pozelor a.î. să o facem mai precisă:

    .. code-block:: bash

        student@uso:~/Pictures$ mv DCIM[0-9][0-9][0-9][0-9] excursie-Sinaia-2020/

    Cu expresia de mai sus vom muta toate pozele din intervalul **DCIM0000** - **DCIM9999**.


Sintaxa specială ``{}``
"""""""""""""""""""""""

În sintaxa globbing, folosim sintaxa ``{}`` pentru a defini o listă de cuvinte (grupuri de caractere) care pot fi folosite în înlocuire.
Această sintaxă înlocuiește exact un caracter din lista oferită.
În directorul vostru home (``~``), executați următoarele comenzi:

.. code-block:: bash

    student@uso:~$ ls -d {Downloads,Music}
    Downloads  Music

    student@uso:~$ ls -d {Down,Mus}*
    Downloads  Music

Citim expresia ``{Downloads,Music}``: în locul acestei expresii poate să existe cuvântul **Downloads** sau cuvântul **Music**.
Observăm că putem să combinăm orice elemente de globbing, așa cum am făcut în expresia ``{Down,Mus}*``.

Folosirea ad-litteram a caracterelor speciale
"""""""""""""""""""""""""""""""""""""""""""""

Există cazuri când numele fișierelor conțin caractere speciale.
Unele fișiere pot fi prefixate cu o categorie din care fac parte, ca în exemplul de mai jos:

.. code-block:: bash

    student@uso:~$ ls Documents/uni
    '[PC] Course 01.pdf'  '[USO] Course 01.pdf'  '[USO] Course 02.pdf'

În exemplul de mai sus, fișierele pdf de curs sunt prefixate cu numele materiei: [PC], [USO].
Vrem să îi spunem sintaxei de globbing că în acest caz, șirul **[USO]** nu trebuie tratat ca o expresie, ci ca un șir de caracter normale.
Pentru a face asta, încadrăm șirul între **"**:

.. code-block:: bash

    student@uso:~$ ls Documents/uni/"[USO]"*
    'Documents/uni/[USO] Course 01.pdf'  'Documents/uni/[USO] Course 02.pdf'

Citim expresia ``"[USO]"*``: orice fișier al cărui nume începe cu șirul de caractere **[USO]** și este urmat de orice caracter.
Operația prin care eliminăm semnificația specială a unui caracter poartă numele de **escaping**; cu alte cuvinte, informal, spunem că am făcut escaping semnificației speciale a sintaxei ``[]``.
Termenul vine de la cuvântul **escape** (a scăpa), și exprimă că scăpăm de semnificația specială a unui caracter / set de caractere.


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
