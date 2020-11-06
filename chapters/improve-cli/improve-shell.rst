O înțelegere mai bună a shellului
=================================


Configurarea shellului bash
---------------------------

Așa cum am menționat în secțiunea Configurarea rulării aplicațiilor, modul în care o aplicație rulează este configurabil.
Fișierul de configurare al shellului **BASH** este ``~/.bashrc``.
Fiecare în directorul home al fiecărui utilizator se găsește un fișier ``.bashrc``.
Există câte un fișier ``.bashrc`` în directorul home al fiecărui utilizator pentru a le permite utilizatorilor să își personalizeze comportamentul shellului lor bash, fără a intra în conflict cu configurările bash ale altor utilizatori din sistem.
Atunci când un utilizator pornește un shell bash, conținutul fișierului ``~/.bashrc`` este citit și sunt aplicate configurările specifice utilizatorului.

Modificarea dimensiunii istoricului
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Inspectăm conținutul fișierului ``~/.bashrc`` folosind comanda următoare:

.. code-block:: bash

    student@uso:~$ less ~/.bashrc

În sesiunea interactivă ``less`` căutăm după cuvântul ``HISTSIZE``:

.. code-block:: bash

    [...]
    # for setting history length see HISTSIZE and HISTFILESIZE in bash(1)
    HISTSIZE=1000
    HISTFILESIZE=2000
    [...]

Shellul bash reține istoricul de comenzi în fișierul ``~/.bash_history`` din directorul home al fiecărui utilizator.
Valorile variabilelor ``HISTSIZE`` și ``HISTFILESIZE`` limitează numărul maxim de comenzi, respectiv linii, din fișierul ``~/.bash_history``.
Dacă vrem să avem un istoric nelimitat putem seta valoarea variabilelor la un număr negativ.

**Exercițiu**: Deschideți fișierul ``~/.bashrc`` în editorul preferat și atribuiți valoarea ``-1`` pentru ``HISTSIZE`` și ``HISTFILESIZE``.
Salvați modificările făcute.

.. warning::

    Atenție!
    **Nu** trebuie să existe spațiu între numele variabilei, ``=`` și valoarea atribuită.

.. tip::

    Pentru a afla mai multe despre valorile ``HISTSIZE`` și ``HISTFILESIZE`` accesați pagina de manual a terminalului bash (``man bash``) și căutați după numele variabilelor.


Vizualizarea aliasurilor predefinite
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Pentru a înțelege ce este un ``alias``, rulăm comanda de mai jos:

.. code-block:: bash

    student@uso:~$ alias ls
    alias ls='ls --color=auto'

Observăm că un alias este un nume (placeholder) care înlocuiește un șir de caractere.
Atunci când scriem în terminal numele unei comenzi, dacă numele scris este un alias, numele comenzii va fi înlocuit cu șirul de caractere definit în alias.
Cu alte cuvinte, atunci când executăm comanda ``ls`` în terminalul bash, defapt executăm comanda ``ls --color=auto``.
Opțiunea ``--color=auto`` este cea care ne colorează rezultatul comenzii ``ls``.

Pentru a vedea toate aliasurile definite în instanța curentă de bash, folosim comanda ``alias``, ca în exemplul de mai jos:

.. code-block:: bash

    student@uso:~$ alias
    alias alert='notify-send --urgency=low -i "$([ $? = 0 ] && echo terminal || echo error)" "$(history|tail -n1|sed -e '\''s/^\s*[0-9]\+\s*//;s/[;&|]\s*alert$//'\'')"'
    alias boot-cli='systemctl set-default multi-user.target'
    alias boot-gui='systemctl set-default graphical.target'
    alias cal='ncal -M'
    alias egrep='egrep --color=auto'
    alias fgrep='fgrep --color=auto'
    alias gigt='git'
    alias gpre='grep'
    alias grep='grep --color=auto'
    alias grpe='grep'
    alias gti='git'
    alias l='ls -CF'
    alias la='ls -A'
    alias ll='ls -alF'
    alias ls='ls --color=auto'
    alias ncal='ncal -M

Observăm că atât ``grep`` cât și ``egrep`` au câte un alias pentru opțiunea ``--color``, care în cazul acesta face highlight expresiei găsite.
Putem defini un alias și pentru un typo pe care îl facem des, așa cum este cazul pentru ``gti``, un alias pentru comanda ``git``.

O parte din aceste aliasuri sunt definite în fișierul ``~/.bashrc``, iar altele în fișierul ``~/.bash_aliases``.
Putem observa asta folosind comanda următoare:

.. code-block:: bash

    student@uso:~$ grep alias ~/.bashrc
    # enable color support of ls and also add handy aliases
        alias ls='ls --color=auto'
        #alias dir='dir --color=auto'
        #alias vdir='vdir --color=auto'
        alias grep='grep --color=auto'
        alias fgrep='fgrep --color=auto'
        alias egrep='egrep --color=auto'
    [...]

    student@uso:~$ cat ~/.bash_aliases
    alias grep='grep --color=auto'
    alias grpe='grep'
    alias gpre='grep'
    alias gti='git'
    [...]

Conținutul fișierului ``~/.bash_aliases`` este inclus de către fișierul ``~/.bashrc`` la pornirea shellului bash.
Astfel, pentru o organizare mai bună, este recomandat ca utilizatorul să-și definească aliasurile în fișierul ``~/.bash_aliases``.

Definirea unui alias
^^^^^^^^^^^^^^^^^^^^

Utilitarul ``xdg-open`` primește calea către un fișier și deschide fișierul respectiv cu aplicația asociată tipului de fișier.
Astfel, comanda ``xdg-open image.png`` va deschide imaginea **image.png** cu aplicația asociată deschiderii formatului **PNG**.
Putem să folosim și un URL ca argument al comenzii ``xdg-open``; astfel, comanda ``xdg-open https://www.google.com`` va deschide pagina Google în browserul vostru implicit.

Ne dorim să definim aliasul ``go`` pentru comanda ``xdg-open``.
Adăugați linia ``alias go='xdg-open'`` în fișierul ``~/.bash_aliases`` și salvați modificările.

Dacă încercăm să folosim aliasul proaspăt definit, vom primi o eroare similară cu cea de mai jos:

.. code-block:: bash

    student@uso:~$ go https://www.google.com

    Command 'go' not found, did you mean:

      command 'go' from snap go (1.15.3)
      command 'mco' from deb mcollective-client
      command 'mgb' from deb mathicgb
      command 'mgp' from deb mgp
      command 'mgt' from deb mgt
    [...]

Acest lucru se întâmplă din cauză că fișierul ``~/.bashrc`` este citit atunci când pornim o instanță de bash (când deschidem un terminal).
Ca să recitim fișierul, și să aplicăm modificările, folosim comanda ``source`` ca în exemplul de mai jos:

.. code-block:: bash

    student@uso:~$ source ~/.bashrc
    student@uso:~$ go https://www.google.com

Comanda ``source ~/.bashrc`` a avut ca efect citirea și aplicarea modificărilor definite în fișierul ``.bashrc`` și fișierele pe care acesta le include.


Execuția comenzilor
-------------------

Încheierea execuției unei comenzi
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Atunci când rulăm o comandă aceasta își poate încheia execuția în două moduri: cu succes sau cu eșec.
Atunci când își încheie execuția, orice proces întoarce un cod de eroare, care este un număr:

* Dacă numărul întors are valoarea ``0``, procesul și-a încheiat execuția cu succes.
* Dacă numărul întors are orice altă valoare, procesul și-a încheiat execuția cu eroare, iar codul întors poate fi folosit pentru a afla mai multe informații despre eroarea pe care a întors-o procesul.
  În pagina ``man`` a utilitarului ``ls`` este specificat:

  .. code-block:: bash

     Exit status:
            0      if OK,

            1      if minor problems (e.g., cannot access subdirectory),

            2      if serious trouble (e.g., cannot access command-line argument).

Pentru a vedea codul cu care și-a încheiat execuția o comandă folosim sintaxa ``$?``.
Urmărim exemplul de mai jos:

.. code-block:: bash

    student@uso:~$ ls Desktop/
    todos.txt
    student@uso:~$ echo $?
    0
    student@uso:~$ ls non-existent
    ls: cannot access 'non-existent': No such file or directory
    student@uso:~$ echo $?
    2

Observăm că în cazul fișierului inexistet, comanda ``ls non-existent`` a întors valoarea ``2``, așa cum era specificat și în pagina de manual.

Înlănțuirea comenzilor în funcție de succes sau eșec
""""""""""""""""""""""""""""""""""""""""""""""""""""

De multe ori vrem să executăm o succesiune de comenzi pentru a realiza o sarcină.
De exemplu, atunci când vrem să instalăm o aplicație o rulăm trei comenzi:

* O să actualizăm indexul surselor de pachete folosind ``apt update``
* O să instalăm pachetul care conține aplicația folosind ``apt install``
* O să rulăm aplicația pentru a valida că instalarea a fost cu succes.

Preferăm să înlănțuim cele trei comenzi într-una singură pentru că astfel putem să pornim tot acest proces, să plecăm de la calculator, iar când ne întoarcem avem tot sistemul pregătit.

Pentru a înlănțui comenzi în terminalul bash avem trei operatori disponibili:

* Operatorul ``;`` - este folosit pentru separarea comenzilor, dar nu ține cont dacă comenzile anterioare au fost executate cu succes sau nu.
  Urmărim exemplul de mai jos:

  .. code-block:: bash

     student@uso:~$ mkdir operators/demo; cd operators/demo
     mkdir: cannot create directory ‘operators/demo’: No such file or directory
     -bash: cd: operators/demo: No such file or directory

  În exemplul de mai sus, comanda ``mkdir`` a eșuat deoarece nu a găsit directorul ``operators`` în care să creeze directorul ``demo``. Cu toate acestea, operatorul ``;`` doar separă comenzile între ele, așa că și comanda ``cd operators/demo`` a fost executată, și și aceasta a eșuat deoarece nu există calea ``operators/demo``.

  Folosim operatorul ``;`` pentru a înlănțui comenzi care sunt independente unele de altele, și deci execuția lor nu depinde de succesul unei comenzi precedente.

* Operatorul binar ``&&`` (și logic) - execută a doua comandă doar dacă precedenta s-a executat cu succes.
  Exemplul anterior devine:

  .. code-block:: bash

     student@uso:~$ mkdir operators/demo && cd operators/demo
     mkdir: cannot create directory ‘operators/demo’: No such file or directory

  Observăm că din moment ce comanda ``mkdir`` a eșuat, comanda ``cd`` nu a mai fost executată.

* Operatorul binar ``||`` (sau logic) - execută a doua comandă doar dacă prima s-a terminat cu eșec.
  Urmărim exemplul de mai jos:

  .. code-block:: bash

     student@uso:~$ (ls -d operators || mkdir operators) && ls -d operators
     ls: cannot access 'operators': No such file or directory
     operators
     student@uso:~$ (ls -d operators || mkdir operators) && ls -d operators
     operators
     operators

  În exemplul de mai sus, prima comandă ``ls`` a eșuat, așa că a fost executată comanda ``mkdir`` și apoi a fost executată ultima comandă ``ls``.
  La cea de-a doua rulare, a fost executată cu succes prima comandă ``ls``, așa că comanda ``mkdir`` nu a mai fost executată, și apoi a fost executată ultima comandă ``ls``.

Pentru a rezolva scenariul de la care am plecat inițial, putem rula:

.. code-block:: bash

    sudo apt update && sudo apt install -y cowsay && cowsay "Howdy"

Comanda de mai sus va actualiza indexul pachetelor sursă, va instala pachetul ``cowsay`` și va rula comanda ``cowsay`` pentru a valida instalarea.
O astfel de înlănțuire de comenzi este numită oneliner.

Exerciții
"""""""""

#. Scrieți un oneliner cu ajutorul căruia descărcați arhiva tar de la adresa TODO, creați directorul ``~/operators/demo/tar`` și apoi dezarhivați conținutul în directorul creat.
#. Actualizați onelinerul anterior a.î. după dezarhivare să pornească compilarea proiectului folosind comanda ``make build``.

Înlănțuirea comenzilor folosind operatorul ``|`` (pipe)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Așa cum am descoperit în secțiunile și capitolele anterioare, în mediul Linux avem multe utilitare care rezolvă o nevoie specifică: ``ls`` afișează informații despre fișiere, ``ps`` despre procese, ``grep`` filtrează, etc.
Toate acestea au la bază filozofia mediului Linux: "do one thing and do it well".
Ca întodeauna, frumusețea stă în simplitate: avem o suită de unelte la dispoziție, fiecare capabilă să rezolve rapid o sarcină dată; pentru a rezolva o problemă mai complexă trebuie doar să îmbinăm uneltele.

Operatorul ``|`` (pipe) ne ajută să facem acest lucru.
Atunci când folosim operatorul ``|`` preluăm rezultatul comenzii din stânga operatorului și îl oferim ca intrare comenzii aflate în dreapta operatorului.

Am folosit de mai multe ori operatorul ``|`` până acum:

* Am afișat informații despre procesele din sistem și am filtrat după numele unui proces:

  .. code-block:: bash

      student@uso:~$ ps -aux | grep firefox
      student  15211  0.5 17.6 3090808 359960 pts/1  Sl   00:14   0:40 /usr/lib/firefox/firefox https://www.google.com
      student  15557  0.0  5.3 2591440 108220 pts/1  Sl   00:14   0:05 /usr/lib/firefox/firefox -contentproc -childID 2 -isForBrowser -prefsLen 6264 -prefMapSize 228098 -parentBuildID 20201027185343 -appdir /usr/lib/firefox/browser 15211 true tab
      student  15623  0.0  7.1 2625192 145232 pts/1  Sl   00:14   0:02 /usr/lib/firefox/firefox -contentproc -childID 4 -isForBrowser -prefsLen 7129 -prefMapSize 228098 -parentBuildID 20201027185343 -appdir /usr/lib/firefox/browser 15211 true tab
      student  15647  0.0  5.9 2629464 120896 pts/1  Sl   00:14   0:02 /usr/lib/firefox/firefox -contentproc -childID 5 -isForBrowser -prefsLen 7129 -prefMapSize 228098 -parentBuildID 20201027185343 -appdir /usr/lib/firefox/browser 15211 true tab
      student  15699  0.0  6.5 2613656 133844 pts/1  Sl   00:14   0:01 /usr/lib/firefox/firefox -contentproc -childID 6 -isForBrowser -prefsLen 9473 -prefMapSize 228098 -parentBuildID 20201027185343 -appdir /usr/lib/firefox/browser 15211 true tab
      student  15726  0.0  3.7 2567444 77320 pts/1   Sl   00:14   0:00 /usr/lib/firefox/firefox -contentproc -childID 7 -isForBrowser -prefsLen 9473 -prefMapSize 228098 -parentBuildID 20201027185343 -appdir /usr/lib/firefox/browser 15211 true tab
      student  16922  0.0  0.0  15972  1040 pts/0    S+   02:18   0:00 grep --color=auto firefox

* Am extras primele zece procese care consumă cel mai mare procent de memorie:

  .. code-block:: bash

      student@uso:~$ ps -aux --sort=-%mem | head -11
      USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
      student  15211  0.5 17.7 3090808 362316 pts/1  Sl   00:14   0:40 /usr/lib/firefox/firefox https://www.google.com
      student   8263  0.1 13.8 3515972 283712 tty1   Sl+  nov06   0:43 /usr/bin/gnome-shell
      student   8763  0.0  8.2 1405448 168436 tty1   SLl+ nov06   0:10 /usr/bin/gnome-software --gapplication-service
      student  15623  0.0  7.1 2625192 145452 pts/1  Sl   00:14   0:03 /usr/lib/firefox/firefox -contentproc -childID 4 -isForBrowser -prefsLen 7129 -prefMapSize 228098 -parentBuildID 20201027185343 -appdir /usr/lib/firefox/browser 15211 true tab
      student  15699  0.0  6.5 2613656 133844 pts/1  Sl   00:14   0:01 /usr/lib/firefox/firefox -contentproc -childID 6 -isForBrowser -prefsLen 9473 -prefMapSize 228098 -parentBuildID 20201027185343 -appdir /usr/lib/firefox/browser 15211 true tab
      student  15647  0.0  5.9 2629464 120896 pts/1  Sl   00:14   0:02 /usr/lib/firefox/firefox -contentproc -childID 5 -isForBrowser -prefsLen 7129 -prefMapSize 228098 -parentBuildID 20201027185343 -appdir /usr/lib/firefox/browser 15211 true tab
      student  15557  0.0  5.3 2591440 108220 pts/1  Sl   00:14   0:05 /usr/lib/firefox/firefox -contentproc -childID 2 -isForBrowser -prefsLen 6264 -prefMapSize 228098 -parentBuildID 20201027185343 -appdir /usr/lib/firefox/browser 15211 true tab
      student  15726  0.0  3.7 2567444 77320 pts/1   Sl   00:14   0:00 /usr/lib/firefox/firefox -contentproc -childID 7 -isForBrowser -prefsLen 9473 -prefMapSize 228098 -parentBuildID 20201027185343 -appdir /usr/lib/firefox/browser 15211 true tab
      student   8106  0.0  3.6 756452 73800 tty1     Sl+  nov06   0:04 /usr/lib/xorg/Xorg vt1 -displayfd 3 -auth /run/user/1000/gdm/Xauthority -background none -noreset -keeptty -verbose 3
      student   8631  0.0  2.5 886656 52380 ?        Ssl  nov06   0:00 /usr/lib/evolution/evolution-calendar-factory

Până acum am efectuat procesări text pe rezultatul unor comenzi.
Folosind operatorul ``|`` și utilitarul ``xargs`` putem să folosim rezultatul pe post de argument pentru altă comandă, ca în exemplul de mai jos:

.. code-block:: bash

    student@uso:~$ find . -maxdepth 1 -type f | xargs ls -l
    -rw------- 1 student student    10992 nov  6 14:56 ./.ICEauthority
    -rw-r--r-- 1 student student      297 nov  7 00:18 ./.bash_aliases
    -rw------- 1 student student    43604 nov  5 02:34 ./.bash_history
    -rw-r--r-- 1 student student      220 aug  6  2018 ./.bash_logout
    -rw-r--r-- 1 student student     3824 aug 13 19:04 ./.bashrc
    -rw-r--r-- 1 student student     3159 aug 20  2018 ./.emacs
    -rw-r--r-- 1 student student       87 aug 21  2018 ./.gitconfig
    -rw------- 1 student student      361 nov  7 02:40 ./.lesshst

Comanda din exemplul de mai sus afișează informații în format lung despre toate fișierele din directorul curent, excluzând directoarele.

Dacă folosim opțiunea ``-p`` a utilitarului ``xargs``, acesta o să ne afișeze ce comandă urmează să execute și așteaptă confirmarea noastră prin apăsarea tastei ``y`` (yes) sau ``n`` (no).
Este recomandat să folosiți opțiunea ``-p`` atunci când vă scrieți onelinerul pentru a verifica că comanda pe care urmează să o executați este corectă.
În exemplul următor ne dorim să mutăm toate arhivele ``.tar`` în directorul ``archives``:

.. code-block:: bash

    student@uso:~$ ls *.tar | xargs -p mv archives
    mv archives courses.tar labhidden.tar uso.tar wiki.tar ?...n

Cu ajutorul opțiunii ``-p`` am putut să observăm că comanda nu are sintaxa dorită și am anulat execuția ei.
Problema este că avem destinația (``archives``) înaintea arhivelor care trebuie mutate.

Pentru a rezolva această problemă folosim opțiunea ``-I str``, ca mai jos:

.. code-block:: bash

    student@uso:~$ ls *.tar | xargs -I str -p mv str archives
    mv courses.tar archives ?...n
    mv labhidden.tar archives ?...n
    mv uso.tar archives ?...n
    mv wiki.tar archives ?...n

Opțiunea ``-I`` va înlocui șirul de caractere ``str`` cu numele arhivelor primite din pipe, așa cum observăm mai sus.
Șirul de caractere placeholder poate să fie orice, nu neapărat ``str``; comanda ``ls *.tar | xargs -I {} -p mv {} archives`` produce aceelași rezultat.

Redirectări - TODO
^^^^^^^^^^^^^^^^^^

* În fișiere și în void (``/dev/null``)
* Din generatoare ``/dev/zero``, ``/dev/urandom``
* Selecția stream-urilor de ieșire (``out`` și ``err``), și combinarea lor (``&>``)


Exerciții - TODO
^^^^^^^^^^^^^^^^

#. Clonați repo folosind ``git``. Rulează o anumită comandă, sau un șir de comenzi doar dacă s-a modificat ceva în repo git log pt a vedea dacă s-au făcut modificări în repo build și pus binare generate în ``~/bin``

#. Căutat în repo/cod sursă după un simbol (`grep -nr <simbol>`). Deschis vim la locația unde a fost găsit simbolul.

#. Implementarea unui alias pt `rm` care muta fișierele în `~/Trash`
    * Adăugare intrare în crontab care șterge periodic (1/zi) fișierele mai vechi de T (ex. 30 zile)
    * Utilizare ``find | xargs`` sau ``find --exec`` pentru rezolvare

#. Lansarea în execuție a unui proces care supraviețuiește închiderii terminalului părinte. Inspectarea acestui proces (``lsof``, ``ps``). Trimiterea unor semnale. Oprirea lui. Un mod de a notifica utilizatorul de terminarea cu succes a procesului (mail?)


3) Shell scripting
------------------

Cred că secțiunea asta intră la capitolul de automatizare. N-aș mai băga-o aici că și așa mi se pare că am vorbit de foarte multe.

* Variabile de mediu: ce sunt, la ce le folosim și care sunt variabilele uzuale (``$HOST``, ``$USER``)
    * ``$PATH`` - la ce este folosit; cum adăugăm ceva la ``$PATH``, ce face export și de ce este util, cum facem ca modificarea ``$PATH`` să fie persistentă (edităm în ``.bashrc``)

* Pornirea mai multor instanțe de shell în aceelași terminal.

* Definirea de variabile cu valori statice (x=42) sau dinamice (x=`ls -l`)

* Oneliners

* Control flow în bash: ``if``, ``for``, ``while read``, ``test``

* Bouns: Definirea de funcții în ``.bashrc``


a. Exerciții
^^^^^^^^^^^^

1. Snippeturi pentru a crea fișiere: sursa main, fișiere header care au ``#ifndef/define/endif __PLACEHOLDER__``, ``Makefile`` etc. Modificarea placeholder-elor cu nume date de utilizator.

#. Creat un director template pentru a fi folosit în inițializarea structurii unor noi proiecte (boilerplate).
    * Generează directoare pt ``src/, build/, gen/, res/`` și fișier ``Readme`` etc.
    * Search and replace după anumite cuvinte placeholder: ex. Numele proiectului în fișierul ``Readme``.
    * Mutat totul într-un script.
    * Script-ul trebuie să primească ca argumente: numele proiectului, repo către github, autor, etc.

#. Scrie un script care generează un fișier Makefile pentru fișierele sursă din directorul curent. Script-ul trebuie să primească tipul fișierelor sursă (`c, cpp, d, java`, etc.) și compilatorul pe care să-l folosească.
    * Pune script-ul în ``~/bin`` și actualizează variabila ``$PATH``.
    * Fă alias-uri pentru cazurile cele mai uzuale: ``c_make_init`` (pt C) și ``cpp_make_init`` pt (C++)

#. Mount în modul read-only al unei partiții (util pt cei care au dualboot și vor să-și monteze discul de Windows, D:\filme, etc).
    * Utilizare sshfs (mount la o partiție prin ssh) - util pt lucrat pe cluster pt cei care folosesc IDE-uri
    * Nu are ce căuta aici, dar nu știam unde să-l pun și nu voiam să uit de el