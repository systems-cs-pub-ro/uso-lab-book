.. _users_perms_processes:

Utilizatori și procese
======================

Acțiunile unui cont de utilizator în cadrul sistemului de operare sunt realizate de procesele deținute de acel utilizator.
Un cont de utilizator nu există ca entitate de sine stătătoare, ci este un atribut al unui proces.

Așa cum am indicat și în secțiunea :ref:`users_perms_privileged_id`, un cont utilizator este identificat de un număr (**UID**);
numele este folosit doar de oameni pentru identificarea facilă;
sistemul de operare este preocupat doar de număr / UID.
Un proces aparține unui cont utilizator dacă acel proces are atributul UID corespunzător acelui cont de utilizator.
Ceea ce înseamnă că, în momentul creării, un proces primește un UID.
Spunem, informal, că acel utilizator deține acel proces.

Un caz particular sunt procesele shell, procese interactive.
Spunem, informa, că un utilizator poate rula comenzi sau că are acces în sistem, atunci când există un shell cu UID-ul acelui cont de utilizator.
Cel mai adesea, shellul este primul proces care aparține unui utilizator.
Apoi shellul creează alte procese aparținând acelui utilizator.
Shellul este cel mai adesea creat la autentificarea utilizatorului.

.. _users_perms_processes_auth:

Autentificarea utilizatorilor
-----------------------------

Autentificarea unui utilizator (*login*, *authentication*) în sistem presupune următoarea secvență de pași:

#. Furnizarea unor elemente de autentificare (numite și credențiale - *login credentials*), în mod tipic un **nume de utilizator** (*username*) și o **parolă** (*password*)
#. Verificarea credențialelor de sistemul de operare
#. În cazul verificării cu succes, crearea unui proces cu UID-ul utilizatorului astfel autentific, cel mai adesea un proces shell

Furnizarea credențialelor
^^^^^^^^^^^^^^^^^^^^^^^^^

Primul pas se realizează într-o interfața de autentificare (grafică sau în linia de comandă).
Se furnizează un prompt unde utilizatorul transmite credențialele.

Un mod de a simula acest prompt în linia de comandă este cu ajutorul comenzii ``login``, comandă care este apelată în momentul autentificării CLI:

.. code-block:: bash

    student@uso:~$ sudo login
    uso login: student
    Password: 
    student@uso:~$

Avem creat astfel, un nou proces shell.
E o abordare strict didactică, având acum un shell creat dintr-un shell existent, pentru același utilizator.

Comanda ``login`` poate fi folosită și transmițând ca argument numele de utilizator:

.. code-block:: bash

    student@uso:~$ sudo login student
    Password:
    student@uso:~$

Pentru a închide shellul nou creat folosim comanda ``exit`` sau comanda ``logout`` sau combinația de taste ``Ctrld+d``.

Este nevoie de folosirea ``sudo`` în fața comenzii ``login`` pentru că această comandă este privilegiată: are acces la baza de date autentificare, folosită în pasul de verificare a credențialelor.

Verificarea credențialelor
^^^^^^^^^^^^^^^^^^^^^^^^^^

Verificarea credențialelor este realizată de interfața de autentificare, în general printr-un proces de autentificare, precum ``login``.
Acest proces citește credențialele și apoi le validează cu o bază de date de autentificare (*authentication database*) disponibilă în sistem.
Această baza de date de autentificare este o resursă critică a sistemului; accesul la această bază de date, chiar și de citire, este considerat o acțiune critică ce poate fi realizată doar privilegiat.
De aceea, comanda ``login`` trebuie rulată în mod privilegiat și trebuie prefixată de ``sudo``.

Baza de date de autentificare este o resursă critică pentru că reține credențialele tuturor utilizatorilor disponibili în sistem.
Faza de verificare presupune compararea credențialelor furnizate cu cele din baza de date de autentificare.
Dacă aceasta nu s-ar realiza privilegiat, orice utilizator ar putea avea acces la credențialele celorlalți utilizatori (posibil inclusiv ``root``);
ceea ce ar fi o problemă de securitate în sistem.

În Linux, baza de date de autentificare este în mod tipic fișierul ``/etc/shadow``:

.. code-block:: bash

    razvan@uso:~$ ls -l /etc/shadow
    -rw-r----- 1 root shadow 1334 Jul  2  2020 /etc/shadow

Observăm că acest fișier poate fi accesat doar de utilizatorul ``root`` și de grupul ``shadow``.
Vom discuta despre permisiuni de acces și grupuri în secțiunile următoare.

.. note:: Conturi de utilizator fără parolă

    Anumite conturi de utilizator pot să nu aibă parolă.
    Ceea ce înseamnă că acele conturi nu pot fi accesate în acest mod: autentificare cu parolă.
    Pot fi însă autentificate în alte moduri, cum ar fi schimbarea utilizatorului.

Crearea unui proces
^^^^^^^^^^^^^^^^^^^

Ulterior autentificării, se creează un prim proces care are UID-ul utilizatorului autentificat.
Acest prim proces este configurabil, cel mai adesea este shellul (grafic sau CLI - depinzând de modul de autentificare).

În cazul autentificării în linia de comandă, procesul creat este descris în fișierul ``/etc/passwd``:

.. code-block:: bash

    student@uso:~$ grep student /etc/passwd
    student:x:1000:1000:Student User,,,:/home/student:/bin/bash

Acest fișier conține informații despre un utilizator: numele de utilizator, UID-ul său, directorul home și primul proces pornit în cazul autentificării (adesea shellul).
În cazul utilizatorul ``student``, conform așteptărilor, primul proces este creat din executabilul ``/bin/bash``, corespunzător shellului Bash.

După autentificare există un proces în sistem care aparține unui cont de utilizator.
Dacă acest proces este shellul, spunem adesea că, un utilizator are acces în sistem.

.. note::

    Anumite conturi de utilizator (``daemon``, ``bin`` etc.) au configurat în fișierul ``/etc/passwd`` ca executabil pentru pornirea primului proces ``/bin/false`` sau ``/usr/sbin/nologin``.
    Acest lucru înseamnă că aceste conturi de utilizator nu pot fi accesate prin autentificare.
    Ci doar prin crearea, în moduri specifice, a unor procese cu UID-ul acelor utilizatori.
    Nu intrăm în detalii aici despre aceste moduri.

.. _users_perms_processes_view_manage:

Vizualizarea șî gestiunea informațiilor despre utilizatori
----------------------------------------------------------

În Linux, fișierul ``/etc/passwd`` reține informațiile despre conturile de utilizatori.
Fișierul ``/etc/shadow`` reține credențialele (parolele) despre conturile de utilizatori.

Fișierul ``/etc/passwd`` nu este critic și poate fi citit de oricine.
Fișierul ``/etc/shadow`` este critic și poate fi citit doar de utilizatorul privilegiat.
În continuare, fișierul ``/etc/passwd`` poate fi modificat doar de utilizatorul privilegiat: acțiunea de citire este necritică, dar cea de scriere este critică.

În mod obișnuit, principiile de securitate într-un sistem de operare, relativ la accesarea informațiilor despre conturile de utilizatori, sunt:

* Un utilizator neprivilegiat (obișnuit) poate să vizualizeze informațiile proprii, mai puțin parola.
* Un utilizator neprivilegiat (obișnuit) poate să modifice informațiile proprii, inclusiv parola.
* Un utilizator neprivilegiat (obișnuit) poate să vizualizeze informațiile altor utilizatori, mai puțin parola.
* Un utilizator neprivilegiat (obișnuit) **NU** poate să modifice informațiile altor utilizatori.
* Un utilizator (de orice tip) **NU** poate vizualiza parolele *plain-text* ale utilizatorilor.
  Parolele sunt ținute criptat.
* Un utilizator privilegiat poate să modifice orice informație a altor utilizatori, inclusiv parola.

Vizualizare
^^^^^^^^^^^

Așa cum am precizat în secțiunea :ref:`users_perm_privileged_id`, un utilizator poate folosi comenzile ``whoami`` și ``id`` pentru a afișa informații despre sine sau alți utilizatori.
Un alt mod este de a parcurge direct conținutul fișierului ``/etc/passwd``, fișier care este consultat și de aceste comenzi.
Un mod mai simplu este folosirea comenzii ``finger`` care afișează informații detaliate:

.. code-block:: bash

    student@uso:~$ finger student
    Login: student         			Name: Student User
    Directory: /home/student             	Shell: /bin/bash

Gestiune
^^^^^^^^

Un utilizator își poate modifica 3 informații:

* Shellul de login, folosind comanda ``chsh``
* Informațiile legate de nume, folosind comanda ``chfn``
* Parola, folosind comanda ``passwd``

Nu insistăm pe primele două, doar pe modificarea parolei.
Un utilizator își poate schimba parola prin simpla invocare a comenzii ``passwd``:

.. code-block:: bash

    student@uso:~$ passwd
    Changing password for student.
    (current) UNIX password:
    Enter new UNIX password:
    Retype new UNIX password:
    passwd: password updated successfully

Acum utilizator are o nouă parolă.

Evident, utilizatorul privilegiat poate schimba parolele tuturor utilizatorilor.

Exerciții: Gestiunea utilizatorului curent
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Din contul utilizatorului curent (``student``), folosiți comanda ``passwd`` pentru a schimba parola utilizatorului.
   **GRIJĂ MARE** să nu uitați parola schimbată.
   Folosiți într-un nou shell comanda ``sudo login student`` pentru a testa noua parolă.

#. Dintr-un shell de root folosiți comanda ``passwd student`` pentru a schimba parola utilizatorului student
   **GRIJĂ MARE** să nu uitați parola schimbată.
   Folosiți într-un nou shell comanda ``sudo login student`` pentru a testa noua parolă.

.. _users_perms_processes_process:

Vizualizarea proceselor
-----------------------

Putem vizualiza evoluția proceselor (privilegiate, neprivilegiate) folosind comanda ``ps`` pentru a înțelege funcționarea comenzilor și apartenența acestora la un anumit utilizator.

Comanda simplă ``ps`` afișează procesele din terminalul curent, în vreme ce comanda ``ps -f`` afișează inclusiv numele de utilizator:

.. code-block:: bash

    student@uso:~$ ps
      PID TTY          TIME CMD
    18900 pts/2    00:00:00 ps
    28892 pts/2    00:00:00 bash
    student@uso:~$ ps -f
    UID        PID  PPID  C STIME TTY          TIME CMD
    student   18907 28892  0 22:38 pts/2    00:00:00 ps -f
    student   28892 20845  0 14:02 pts/2    00:00:00 /bin/bash

Se afișează procesul shell (``bash``) și procesul ``ps`` însuși, ambele aparținând utilizatorului ``student``.

Putem personaliza afișarea pentru a prezenta și UID-ul:

.. code-block:: bash

    student@uso:~$ ps -o uid,user,pid,ppid,cmd
      UID USER       PID  PPID CMD
     1000 student   19083 28892 ps -o uid,user,pid,ppid,cmd
     1000 student   28892 20845 /bin/bash

Folosirea comenzii ``ps`` ajută la înțelegerea comenzilor ``sudo`` sau ``su``.

Atunci când creăm un shell privilegiat folosind ``sudo bash``, avem următoarea situație:

.. code-block:: bash

    student@uso:~$ ps -f
    UID        PID  PPID  C STIME TTY          TIME CMD
    student   19153 28892  0 22:46 pts/2    00:00:00 ps -f
    student   28892 20845  0 14:02 pts/2    00:00:00 /bin/bash

    student@uso:~$ sudo bash

    root@uso:~# ps -H
      PID TTY          TIME CMD
    19154 pts/2    00:00:00 sudo
    19155 pts/2    00:00:00   bash
    19163 pts/2    00:00:00     ps

    root@uso:~# ps -f
    UID        PID  PPID  C STIME TTY          TIME CMD
    root     19154 28892  0 22:46 pts/2    00:00:00 sudo bash
    root     19155 19154  0 22:46 pts/2    00:00:00 bash
    root     19173 19155  0 22:46 pts/2    00:00:00 ps -f

    root@uso:~# pstree -Aup 28892
    bash(28892,student)---sudo(19154,root)---bash(19155)---pstree(19198)

    root@uso:~# exit
    exit

    student@uso:~$ ps -f
    UID        PID  PPID  C STIME TTY          TIME CMD
    student   19205 28892  0 22:47 pts/2    00:00:00 ps -f
    student   28892 20845  0 14:02 pts/2    00:00:00 /bin/bash

Observăm că există un proces ``sudo`` și un proces ``bash`` care aparțin utilizatorului ``root``.
Aceste procese sunt create în urma comenzii ``sudo bash``.
Procesul părinte (``PPID``) pentru procesul ``sudo`` este ``28892`` adică shellul inițial al utilizatorului ``student``, cel care a rulat comanda ``sudo bash``.
Practic dintr-un shell al utilizatorului ``student``, folosind ``sudo`` se generează un shell al utilizatorului ``root``.
Comanda ``pstree`` afișează ierarhia de procese și schimbările de conturi de utilizator.

O situație similară avem în cazul ``sudo su``:

.. code-block:: bash

    student@uso:~$ sudo su

    root@uso:/home/student# ps -H
      PID TTY          TIME CMD
    19432 pts/2    00:00:00 sudo
    19433 pts/2    00:00:00   su
    19434 pts/2    00:00:00     bash
    19445 pts/2    00:00:00       ps

    root@uso:/home/student# ps -f
    UID        PID  PPID  C STIME TTY          TIME CMD
    root     19432 28892  0 22:54 pts/2    00:00:00 sudo su
    root     19433 19432  0 22:54 pts/2    00:00:00 su
    root     19434 19433  0 22:54 pts/2    00:00:00 bash
    root     19455 19434  0 22:54 pts/2    00:00:00 ps -f

    root@uso:/home/student# pstree -Aup 28892
    bash(28892,student)---sudo(19432,root)---su(19433)---bash(19434)---pstree(19460)

    root@uso:/home/student# exit

    student@uso:~$

Exerciții: Vizualizarea proceselor
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Realizați un scenariu în care accesați contul ``root`` apoi contul ``student`` și apoi iar contul de ``root``.
Afișați procesele create la fiecare pas.
Folosiți comanda ``pstree`` ca să afișați arborescența de procese astfel create.

Apoi închideți procesele astfel create (folosind ``exit``, ``logout`` sau ``Ctrl+d``).
Afișați, la fiecare pas, ierarhia de procese.
