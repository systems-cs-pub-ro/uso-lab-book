.. _improve_cli_improve_shell_summary:

Sumar: O înțelegere mai bună a shellului
========================================

Configurarea shellului bash
---------------------------

Fișierul de configurare al shellului **BASH** este ``~/.bashrc``.
Atunci când un utilizator pornește un shell bash, conținutul fișierului ``~/.bashrc`` este citit și sunt aplicate configurările specifice utilizatorului.

Valorile variabilelor ``HISTSIZE`` și ``HISTFILESIZE`` limitează numărul maxim de comenzi, respectiv linii, din fișierul ``~/.bash_history``.

Un alias este un nume (*placeholder*) care înlocuiește un șir de caractere.
Pentru o organizare mai bună, este recomandat ca utilizatorul să-și definească aliasurile în fișierul ``~/.bash_aliases``.

Execuția comenzilor
-------------------

Înlănțuirea comenzilor
^^^^^^^^^^^^^^^^^^^^^^

Atunci când își încheie execuția, orice proces întoarce un cod de eroare, care este un număr: valoarea ``0`` semnifică că acesta și-a încheiat execuția cu succes, iar orice ală valoare indică o eroare.


Pentru a înlănțui comenzi în terminalul bash avem trei operatori disponibili:

* Operatorul ``;`` - este folosit pentru separarea comenzilor, indiferent de cum s-au executat acestea.
* Operatorul binar ``&&`` (și logic) - execută a doua comandă doar dacă precedenta s-a executat cu succes.
* Operatorul binar ``||`` (sau logic) - execută a doua comandă doar dacă prima s-a terminat cu eșec.

Atunci când folosim operatorul ``|`` preluăm rezultatul comenzii din stânga operatorului și îl oferim ca intrare comenzii aflate în dreapta operatorului.
Operatorul ``|`` ne permite să prelucrăm datele de interes, trecându-le prin mai multe utilitare, fiecare cu un scop bine definit.

Redirectări
^^^^^^^^^^^

Folosim operatorul ``>`` pentru a redirecta **STDOUT** sau **STDERR** într-un fișier.
Pentru a redirecta ieșirea standard folosim sintaxa ``cmd > nume-fișier``.
Pentru a redirecta ieșirea standard a erorilor folosim sintaxa ``cmd 2> nume-fișier``.

Implicit, operatoru ``>`` șterge (trunchează) conținutul fișierului destinație.
Dacă vrem să păstrăm conținutul fișierului și să adăugăm rezultatul redirectării în continuarea acestuia, folosim operatorul ``>>``.

Folosim sintaxa ``&> cale/către/nume-fișier`` pentru a redirecta atât STDERR, cât și STDOUT, în fișierul primit ca argument.

Fișiere speciale
""""""""""""""""

* Fișierul ``/dev/null`` este un fișier care ignoră orice este scris în el.

* Fișierul ``/dev/zero`` este un generator de octeți.
  Acesta generează atâția octeți cu valoarea zero (**0**) [#dev-zero]_ cât îi sunt ceruți.

* Fișierul ``/dev/urandom`` este un alt generator de octeți.
  Acesta generează atâția octeți cu valoare random cât îi sunt ceruți.
