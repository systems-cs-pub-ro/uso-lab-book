Extra - Sistemul de fișiere
===========================

Căutarea fișierelor în sistemul de fișiere
------------------------------------------

Se poate întâmpla să vrem să aflăm dacă într-o ierarhie de fișiere găsim un anumit fișier și, dacă există, vrem să aflăm unde se află.
Spre exemplu, serviciul ``ssh`` folosește un fișier de configurare numit ``ssh_config``, dar nu mai ținem minte calea exactă până la acel fișier.

Linux ne oferă două utilitare, ``locate`` și ``find``, care pot fi de ajutor în situația descrisă mai sus.


Folosirea utilitarului ``find``
"""""""""""""""""""""""""""""""

În mod obișnuit, numele fișierelor de configurare pentru servicii se termină în extensia ``conf``.
Găsim toate fișierele de configurare ale serviciului ``ssh`` de pe sistem folosind comanda ``find``:

.. code-block:: bash

    student@uso:~/comenzi$ sudo find / -iname "*ssh*conf"
    /usr/share/upstart/sessions/ssh-agent.conf
    /usr/lib/tmpfiles.d/sshd.conf
    /etc/init/ssh.conf

Am căutat în calea ``/`` (*root*) orice fișier ce conține ``ssh`` și se termină cu ``conf``.
Am folosit comanda ``sudo`` pentru că suntem un utilizator neprivilegiat și nu putem căuta în directorul (*root*).

Utilitarul ``find`` caută în ierarhia de fișiere care începe de la calea dată ca parametru în jos. În cazul nostru, de la ``/`` (root) în jos, adică în tot sistemul de fișiere.

Mai multe informații și exemple de utilizări vom vedea în capitolul #TODOref_capitol_edi 


Folosirea utilitarului ``locate``
"""""""""""""""""""""""""""""""""

Atunci când vrem să căutăm într-o ierarhie mare de fișiere, utilitarul ``find`` nu este cea mai bună soluție deoarece este încet.

Utilitarul ``locate`` ne poate ajuta în astfel de situații.

Acesta funcționează în 2 pași:

* Crearea și actualizarea unei baze de date folosind comanda ``updatedb``.
  Aceasta conține intrări cu toate fișierele din sistem și locatia acestora.
* Căutarea folosind ``locate``.
  Această căutare se reduce la interogarea bazei de date create anterior cu ``updatedb``.


Performanța utilitarului este foarte bună, superioară lui ``find``.
Partea negativă este că la fiecare căutare trebuie folosit utilitarul ``updatedb``.

Încercăm să căutăm fișierul ``pwd`` în sistemul de fișiere folosind ``locate``:

.. code-block:: bash

    student@uso:~/comenzi$ sudo updatedb
    student@uso:~/comenzi$ locate "*ssh*conf"
    /etc/init/ssh.conf
    /usr/lib/tmpfiles.d/sshd.conf
    /usr/share/upstart/sessions/ssh-agent.conf

Actualizăm baza de date folosind ``updatedb`` și apoi căutăm fișierul de configurare cu utilitarul ``locate``.
Răspunsul comenzii este instant.


Acum ne dorim să găsim toate arhivele de tip ``tar`` de pe stația noastră. Vom folosi iar utilitarul ``locate`` alături
de șirul de caractere ``*.tar``.

.. code-block:: bash

    student@uso:~$ locate *.tar
    /home/student/inregistrari.tar
    /home/student/usr_bin.tar

Acesta este un presupus output al utilitarului ``locate``. Au fost găsite arhivele ``înregistrări.tar`` și ``usr_bin.tar``
pe care le aveam în sistemul de fișiere de la secțiunea anterioară.

Găsim mai multe informații și exemple în capitolul todo_ref_edi 

Variabila de mediu PATH
-----------------------

Până acum am învățat câteva comenzi utile: ``ls``, ``cd``, ``find``, ``locate``.

Utilitarele sunt de fapt **programe** (*executabile*) care se află undeva în sistemul de fișiere.

Shell-ul știe să ruleze utilitarele din orice loc în care ne aflăm (din ierarhia de fișiere).
Se întâmplă acest lucru pentru că shell-ul are o listă de câteva directoare în care se uită după utilitarele pe care le folosim.
Spre exemplu, atunci când rulăm utilitarul ``ls``, el caută programul ``ls`` în lista pe care o are, îl găsește și îl rulează.

Această listă se găsește în *variabila de mediu* [#]_ ``PATH``.


Afișarea variabilei PATH din sistem
"""""""""""""""""""""""""""""""""""

Afișăm valoarea variabilei de mediu ``PATH`` a sistemului folosind utilitarul ``echo``.

.. code-block::

    $ echo $PATH
    /usr/local/bin:/usr/bin:/bin:/usr/games

Variabila ``PATH`` are patru căi din sistem, despărțite de caracterul ``:``.
Astfel, sistemul verifică dacă utilitarul este prezent în calea ``/usr/local/bin``. Dacă nu-l găsește, merge la următoarea calea ``/usr/bin``.
Se caută utilitarul la toate căile disponibile. Dacă nu-l găsește va apărea în shell-ul curent un mesaj de eroare.

.. note::
    Un utilitar poate fi la mai multe căi din PATH, dar va fi executat utilitarul din cea mai din stânga cale (prima, dacă nu a doua, etc.).

Căutarea utilitarelor în sistemul de fișiere
--------------------------------------------

Există cazuri când vrem să găsim locația exactă a unui utilitar: vrem să aflăm ce permisiuni are, cine îl deține sau ce dimensiune are.

Folosirea utilitarului ``which``
""""""""""""""""""""""""""""""""

Acest utilitar identifică calea programelor din sistem.

Căutăm calea la care se află utilitarul ``ls`` folosind comanda ``which``:

.. code-block::

    student@uso:~$ which ls
    /bin/ls
    student@uso:~$ which pwd
    /bin/pwd
    student@uso:~$ which man
    /usr/bin/man 


``which`` folosește variabila de mediu ``PATH`` pentru a găsi utilitarul cerut și va afișa rezultatele în ordinea directoarelor din ``PATH``.

Aflăm mai multe detalii despre utilitarul ``which`` în capitolul #TODOtodo_edi_which.


Exerciții
"""""""""

* Redenumiți utilitarul ``pwd`` în ``pwd_backup``.
  Puteți să mai executați comanda ``pwd``?
  Dar ``pwd_backup``?


.. [#] Variabilele de mediu sunt variabile care descriu mediul în care sunt executate programele. 
    Ele sunt folosite de aplicații pentru a răspunde la întrebări cum ar fi: Care este numele calculatorului pe care sunt instalată?
    Care este numele contului de utilizator care mă execută?
    Care este folderul meu de lucru?
    Unde se află fișierele temporare pe calculator?
