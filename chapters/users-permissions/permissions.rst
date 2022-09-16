.. _users_perms_permissions_in_fs:

Permisiuni în sistemul de fișiere
=================================

Un proces aparținând unui utilizator (adică având un anumit câmp UID) are anumite permisiuni în sistem.
Permisiunile (sau drepturile sau privilegiile) se referă la acțiuni pe care utilizatorul le poate efectua în cadrul sistemului;
aceste acțiuni se vor efectua prin intermediul unor procese aparținând utilizatorului.
Utilizatorul privilegiat (superuser, ``root``) are permisiuni complete în sistem și poate realiza orice acțiuni.
Un utilizator neprivilegiat (așa cum este utilizatorul ``student``) poate executa doar un subset al acestora;
acțiunile considerate critice sau sensibile nu pot fi executate de un utilizator neprvilegiat;
spunem că utilizatorul nu are permisiunile necesare;
acest lucru îl putem observa în linia de comandă prin primirea unui mesaj de tipul ``Permission denied``, ca atunci când utilizatorul ``student`` dorește vizualizarea conținutului fișierului ``/etc/shadow``:

.. code-block:: bash

    student@uso:~$ cat /etc/shadow
    cat: /etc/shadow: Permission denied

Permisiunile unui utilizator pot fi cel mai adesea configurate.
Adică unui utilizator îi pot fi acordate sau revocate permisiuni pentru realizarea unor acțiuni.
Numim această acțiune **autorizare**.

Cea mai frecventă țință de configurare a permisiunilor o reprezintă sistemul de fișiere.
Însemnând configurarea accesului unui utilizator la anumite fișiere / directoare.
De exemplu, putem configura ca un utilizator să nu aibă deloc acces la un fișier, sau doar acces de citire, sau acces de citire și de scriere.
În restul acestei secțiuni vom discuta despre permisiuni în sistemul de fișiere.
Alte tipuri de permisiuni (și configurarea acestora) vor fi descrise în secțiunea :ref:`users_perms_advanced`.

.. _users_perms_permissions_in_fs_view:

Vizualizarea permisiunilor
--------------------------

Cel mai direct mod de a vizualiza permisiunile în sistemul de fișiere este cu opțiunea ``-l`` (*long listing*) a comenzii ``ls``, ca în cazul comenzii de mai jos:

.. code-block:: bash

    student@uso:~/.../users-permissions/support/permissions$ ls -l
    total 8
    -rw-rw-r-- 1 student student 34 Dec 26 18:34 hello.sh
    ---------- 1 student student  0 Dec 26 18:34 noperm
    -r-------- 1 student student 20 Dec 26 18:35 readonly
    --w------- 1 student student  0 Dec 26 18:36 writeonly

Comanda ``ls -l`` afișează, pentru fiecare intrare, permisiunile acesteia.
Permisiunile sunt indicate de primele caractere afișate pe fiecare linie, mai puțin primul caracter.
Primul caracter reprezintă tipul intrării, în vreme ce următoarele 9 caractere sunt permisiunile.
În cazul fișierului ``hello.sh`` permisiunile sunt ``rw-rw-r--``, în vreme ce în cazul fișierului ``readonly`` permisiunile sunt ``r--------``.
Pe moment vom discuta strict despre primele 3 caractere din permisiuni; aceste caractere dau cel mai adesea permisiunile utilizatorului.
În Secțiunea TODO vom discuta cumulat despre toate cele 9 caractere din permisiuni.

Cum este de așteptat din numele fișierelor:

* fișierul ``noperm`` nu are nici o permisiune: primele 3 caractere de permisiune sunt ``---``
* fișierul ``readonly`` are doar permisiune de citire: primele 3 caractere de permisiune sunt ``r--``
* fișierul ``writeonly`` are doar permisiune de scriere: primele 3 caractere de permisiune sunt ``-w-``

Cele 3 caractere corespund celor 3 tipuri de permisiuni:

* ``r`` (*read*): permisiune de citire
* ``w`` (*write*): permisiune de scriere
* ``x`` (*execute*): permisiune de execuție

Verificarea permisiunilor
^^^^^^^^^^^^^^^^^^^^^^^^^

Aceste permisiuni sunt aplicate în momentul în care executăm acțiuni concrete pe fișiere.
Astfel, pentru a verifica în mod concret permisiunile pe fișiere, folosim comenzi precum cele de mai jos:

.. code-block:: bash

    student@uso:~/.../users-permissions/support/permissions$ cat readonly
    seeing is believing
    student@uso:~/.../users-permissions/support/permissions$ echo test > readonly
    bash: readonly: Permission denied
    student@uso:~/.../users-permissions/support/permissions$ cat writeonly
    cat: writeonly: Permission denied
    student@uso:~/.../users-permissions/support/permissions$ echo test > writeonly
    student@uso:~/.../users-permissions/support/permissions$ cat noperm
    cat: noperm: Permission denied
    student@uso:~/.../users-permissions/support/permissions$ echo test > noperm
    bash: noperm: Permission denied
    student@uso:~/.../users-permissions/support/permissions$ ./hello.sh
    bash: ./hello.sh: Permission denied

Am folosit, în comenzile de mai sus:

* comanda ``cat`` pentru a afișa continutul unui fișier și pentru a verifica, astfel, permisiunea de citire.
  Putem vizualiza conținutul fișierului ``readonly``, care are permisiune de citire, dar nu al fișierelor ``writeonly`` și ``noperm`` care nu au permisiune de citire.
* redirectarea ieșirii comenzii ``echo test`` pentru a scrie conținut într-un fișier și pentru a verifica, astfel, permisiunea de scriere.
  Putem scrie conținut în fișierul ``writeonly``, care are permisiune de scriere, dar nu în fișierele ``readonlyonly`` și ``noperm`` care nu au permisiune de scriere.
* prefixul ``./`` în fața unui fișier pentru a executa acel fișier și pentru a verifica, astfel, permisiunea de execuție.
  Fișierul ``hello.sh`` nu are permisiune de execuție, astfel câ încercarea de a îl executa va eșua.
  La fel ar fi cazul și celorlalte fișiere, nici unul dintre care nu are permisiune de execuție.

Observăm că în cazul unor comenzi eșuate din cauza lipsei de permisiuni, mesajul afîșat este mereu același: *Permission denied**.

Alte moduri de vizualizare a permisiunilor
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Pe lângă comanda ``ls -l`` un alt mod de a verifica permisiunile unui fișier este folosind comanda ``stat``:

.. code-block:: bash

    student@uso:~/.../users-permissions/support/permissions$ stat writeonly
      File: writeonly
      Size: 5         	Blocks: 8          IO Block: 4096   regular file
    Device: 10305h/66309d	Inode: 534501      Links: 1
    Access: (0200/--w-------)  Uid: ( 1000/  student)   Gid: ( 1000/  student)
    Access: 2021-12-26 18:34:56.615303322 +0200
    Modify: 2021-12-30 19:35:31.859546113 +0200
    Change: 2021-12-30 19:35:31.859546113 +0200
     Birth: -
    student@uso:~/.../users-permissions/support/permissions$ stat readonly
      File: readonly
      Size: 20        	Blocks: 8          IO Block: 4096   regular file
    Device: 10305h/66309d	Inode: 534504      Links: 1
    Access: (0400/-r--------)  Uid: ( 1000/  student)   Gid: ( 1000/  student)
    Access: 2021-12-30 19:35:04.035618222 +0200
    Modify: 2021-12-26 18:35:23.044215182 +0200
    Change: 2021-12-26 18:35:32.164529854 +0200
     Birth: -

Linia ``Access:`` afișează permisiunile.
Observăm că permisiunile sunt precedate de o valoare numerică (``0200`` și ``0400``).
Vom discuta despre această valoare numerică, numită forma numerică (în octal) a permisiunilor în Secțiunea :ref:`user_perm_permissions_numeric`.

Exerciții
^^^^^^^^^

* Creați fișierul ``myfile`` folosind comanda ``touch``.
  Vizualizați permisiunile implicite (*default*) ale fișierului.
  Verificați permisiunile.

* Vizualizați permisiunile fișierului ``bye.sh`` din directorul de suport.
  Verificați permisiunile.

* Vizualizați permisiunile fișierului ``dec31.sh`` din directorul de suport.
  Verificați permisiunile.
  Observați că, și dacă are permisiune de execuție, fișierul nu poate fi executat dacă nu are și permisiune de citire.

.. _users_perms_permissions_in_fs_dir:

Permisiuni pe directoare
------------------------

Am discutat până acum permisiunile pe fișiere.
Cele trei permisiuni (citire, scriere și execuție se pot aplica și pe directoare):

.. code-block:: basho

    student@uso:~/.../support/permissions/demo-dir$ ls -l
    total 20
    d--x------ 2 student student 4096 Dec 30 20:20 exec-dir
    dr-x------ 2 student student 4096 Dec 30 20:20 read-exec-dir
    drw------- 2 student student 4096 Dec 30 20:20 read-write-dir
    drwx------ 2 student student 4096 Dec 30 20:20 read-write-exec-dir
    d-wx------ 2 student student 4096 Dec 30 20:20 write-exec-dir

Cele trei permisiuni pe directoare au următorul rol:

* permisiunea de citire: conținutul directorului poate fi afișat
* permisiunea de scriere: conținutul directorului poate fi modificat (pot fi create și șterse intrări din director)
* permisiunea de execuție: directorul poate fi parcurs, poate fi parte a unei căi

Verificarea permisiunilor pe directoare
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Verificăm permisiunile pe directoare folosind comenzile de mai jos:

* ``ls <director>``: Afișează conținutul directorului, adică intrările din acel director (fișiere, subdirectoare etc.).
  Necesită permisiune de citire pe director.
* ``ls <director>/a.txt``: Afișează calea către fișierul ``a.txt`` din cadrul directorului.
  Necesită permisiune de execuție pe director.
  Fără permisiuni de execuție, directorul nu poate fi parte a unei căi.
* ``cat <director>/a.txt``: Afișează conținutul fișierului ``a.txt`` din cadrul directorului.
  Necesită permisiune de execuție pe director **și** drept de citire pe fișierul ``a.txt``.
* ``touch <director>/c.txt``: Creează o intrare în director, în forma unui fișier cu numele ``c.txt``.
  Necesită permisiune de scriere **și** de execuție pe director.
* ``rm <director>/c.txt``: Șterge intrarea numită ``c.txt`` din director.
  Necesită permisiune de scriere **și** de execuție pe director.
* ``ls <director>/<TAB><TAB>``: Afișează conținutul posibil pentru completarea căilor din director.
  Necesită permisiune de citire **și** de execuție pe director.

Astfel, verificăm permisiunile pe directoarele ``read-exec-dir`` și ``read-write-dir`` folosind comenzile de mai jos:

.. code-block:: bash

    student@uso:~/.../support/permissions/demo-dir$ ls exec-dir/
    ls: cannot open directory 'exec-dir/': Permission denied
    student@uso:~/.../support/permissions/demo-dir$ cat exec-dir/a.txt
    test-a
    student@uso:~/.../support/permissions/demo-dir$ cat exec-dir/b.txt
    test-b
    student@uso:~/.../support/permissions/demo-dir$ touch exec-dir/c.txt
    touch: cannot touch 'exec-dir/c.txt': Permission denied
    student@uso:~/.../support/permissions/demo-dir$ rm exec-dir/a.txt
    rm: cannot remove 'exec-dir/a.txt': Permission denied

    student@uso:~/.../support/permissions/demo-dir$ ls read-exec-dir/
    a.txt  b.txt
    student@uso:~/.../support/permissions/demo-dir$ ls read-exec-dir/a.txt
    read-exec-dir/a.txt
    student@uso:~/.../support/permissions/demo-dir$ cat read-exec-dir/a.txt
    test-a
    student@uso:~/.../support/permissions/demo-dir$ touch read-exec-dir/c.txt
    touch: cannot touch 'read-exec-dir/c.txt': Permission denied
    student@uso:~/.../support/permissions/demo-dir$ rm read-exec-dir/a.txt
    rm: cannot remove 'read-exec-dir/a.txt': Permission denied

Exerciții
^^^^^^^^^

.. _users_perms_permissions_in_fs_mod:

Modificarea permisiunilor
-------------------------

.. _users_perms_permissions_in_fs_groups:

Gruparea utilizatorilor
-----------------------

.. _users_perms_permissions_in_fs_numeric:

Formatul numeric al permisiunilor
---------------------------------

.. _users_perms_permissions_in_fs_find:

Căutarea fișierelor după permisiuni
-----------------------------------
