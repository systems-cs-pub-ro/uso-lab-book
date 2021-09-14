Sumar - Cheatsheet
==================

Căi în ierarhia de fișiere
--------------------------

Calea curentă
^^^^^^^^^^^^^

.. code-block:: bash

    student@uso:~$ pwd
    /home/student


Cale relativă și cale absolută
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Cale relativă:

.. code-block:: bash

    student@uso:~$ ls -l comenzi/mkdir/
    total 8
    drwxr-xr-x 2 student student 4096 Sep 29 18:20 Avengers
    drwxr-xr-x 2 student student 4096 Sep 29 19:21 GameOfThrones

Cale absolută: 

.. code-block:: bash

    student@uso:~$ ls -l /home/student/comenzi/mkdir/
    total 8
    drwxr-xr-x 2 student student 4096 Sep 29 18:20 Avengers
    drwxr-xr-x 2 student student 4096 Sep 29 19:21 GameOfThrones



Schimbarea căii curente
^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    student@uso:/etc$ pwd
    /etc
    student@uso:/etc$ cd /usr
    student@uso:/usr$ pwd
    /usr

Scurtături de căi
^^^^^^^^^^^^^^^^^

Caracterul ``-``:

  .. code-block:: bash

    student@uso:~$ pwd
    /home/student
    student@uso:~$ cd /usr/bin/
    student@uso:/usr/bin$ pwd
    /usr/bin
    student@uso:/usr/bin$ cd -
    /home/student
    student@uso:~$ cd -
    /usr/bin
    student@uso:/usr/bin$ cd -
    /home/student
    student@uso:~$ cd -
    /usr/bin


Caracterul ``~``:

  .. code-block:: bash

    student@uso:/usr/bin$ cd /tmp/
    student@uso:/tmp$ pwd
    /tmp
    student@uso:/tmp$ cd ~
    student@uso:~$ pwd
    /home/student
    student@uso:~$ cd /usr/bin/X11/
    student@uso:/usr/bin/X11$ pwd
    /usr/bin/X11
    student@uso:/usr/bin/X11$ cd ~
    student@uso:~$ pwd
    /home/student

Interacțiunea cu fișiere în linia de comandă
--------------------------------------------


Ierarhie de fișiere
^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    student@uso:~/comenzi/mkdir$ tree -L 1 /
    /
    |-- bin
    |-- boot
    |-- dev
    |-- etc
    |-- home
    |-- initrd.img -> /boot/initrd.img-3.16.0-4-586
    |-- lib
    |-- lib64
    |-- libx32
    |-- lost+found
    |-- media
    |-- mnt
    |-- opt
    |-- proc
    |-- root
    |-- run
    |-- sbin
    |-- srv
    |-- sys
    |-- tmp
    |-- usr
    |-- var
    ``-- vmlinuz -> boot/vmlinuz-3.16.0-4-586

Afișarea conținutului unui director
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    student@uso:~/comenzi/mkdir/Avengers$ ls
    Captain America  Iron Man  Thor

.. code-block:: bash

    student@uso:~/comenzi/touch$ ls -l
    total 0
    -rw-r--r-- 1 student student 0 Sep 29 17:32 cities
    -rw-r--r-- 1 student student 0 Sep 29 17:25 cities in romania
    -rw-r--r-- 1 student student 0 Sep 29 17:33 romania


Crearea fișierelor
^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    student@uso:~$ ls cities
    ls: cannot access cities: No such file or directory
    student@uso:~$ touch cities
    student@uso:~$ ls cities
    cities

Crearea directoarelor
^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    student@uso:~/comenzi/mkdir$ mkdir GameOfThrones
    student@uso:~/comenzi/mkdir$ mkdir Avengers
    student@uso:~/comenzi/mkdir$ ls -l
    total 8
    drwxr-xr-x 2 student student 4096 Sep 29 17:43 Avengers
    drwxr-xr-x 2 student student 4096 Sep 29 17:43 GameOfThrones

Afișarea conținutului unui fișier
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    student@uso:~/comenzi/mkdir$ cat GameOfThrones/Arya
    A girl has no name

Ștergerea fișierelor
^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    student@uso:~/comenzi/mkdir$ ls Avengers/
    Captain America  Hulk  Iron Man  Thor
    student@uso:~/comenzi/mkdir$ rm Avengers/Hulk
    student@uso:~/comenzi/mkdir$ ls Avengers/
    Captain America  Iron Man  Thor

Ștergerea directoarelor
^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    student@uso:~/comenzi/mkdir$ mkdir LordOfTheRings
    student@uso:~/comenzi/mkdir$ ls -l
    total 12
    drwxr-xr-x 2 student student 4096 Sep 29 18:02 Avengers
    drwxr-xr-x 2 student student 4096 Sep 29 17:44 GameOfThrones
    drwxr-xr-x 2 student student 4096 Sep 29 18:09 LordOfTheRings
    student@uso:~/comenzi/mkdir$ rmdir "LordOfTheRings"
    student@uso:~/comenzi/mkdir$ ls -l
    total 8
    drwxr-xr-x 2 student student 4096 Sep 29 18:02 Avengers
    drwxr-xr-x 2 student student 4096 Sep 29 17:44 GameOfThrones

Redenumirea și mutarea fișierelor și directoarelor
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    student@uso:~/comenzi/mkdir$ ls
    GameOfThrones
    student@uso:~/comenzi/mkdir$ mv GameOfThrones ThroneOfGames
    student@uso:~/comenzi/mkdir$ ls
    ThroneOfGames

Copierea fișierelor și directoarelor
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash


    student@uso:~/comenzi/mkdir$ cp Avengers/Thor /tmp/
    student@uso:~/comenzi/mkdir$ ls /tmp/
    Thor  ssh-ApUMKI3HSJ

Fișiere și directoare ascunse
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    student@uso:~/comenzi/mkdir$ ls -al
    total 8
    drwxr-xr-x 5 student student 4096 Sep 29 18:41 .
    drwxr-xr-x 4 student student 4096 Sep 29 18:35 ..
    drwxr-xr-x 2 student student 4096 Sep 29 18:20 Avengers
    drwxr-xr-x 2 student student 4096 Sep 29 17:44 GameOfThrones

.. code-block:: bash

    student@uso:~/comenzi/mkdir/Avengers$ ls -l
    total 0
    -rw-r--r-- 1 student student 0 Sep 29 18:20 Captain America
    -rw-r--r-- 1 student student 0 Sep 29 18:20 Iron Man
    -rw-r--r-- 1 student student 0 Sep 29 18:20 Thor
    student@uso:~/comenzi/mkdir/Avengers$ touch .Hulk
    student@uso:~/comenzi/mkdir/Avengers$ ls -l
    total 0
    -rw-r--r-- 1 student student 0 Sep 29 18:20 Captain America
    -rw-r--r-- 1 student student 0 Sep 29 18:20 Iron Man
    -rw-r--r-- 1 student student 0 Sep 29 18:20 Thor
    student@uso:~/comenzi/mkdir/Avengers$ ls -al
    total 8
    drwxr-xr-x 2 student student 4096 Oct  6 16:44 .
    drwxr-xr-x 5 student student 4096 Sep 29 19:14 ..
    -rw-r--r-- 1 student student    0 Oct  6 16:44 .Hulk
    -rw-r--r-- 1 student student    0 Sep 29 18:20 Captain America
    -rw-r--r-- 1 student student    0 Sep 29 18:20 Iron Man
    -rw-r--r-- 1 student student    0 Sep 29 18:20 Thor

Afișarea tipului de fișier
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    student@uso:~$ file Picture.abc
    Picture.abc: PNG image data, 742 x 320, 8-bit/color RGBA, non-interlaced
    student@uso:~$ file index.rst
    index.rst: ASCII text
    student@uso:~$ file archive.tar
    archive.tar: POSIX tar archive (GNU) 


Legături (Links)
^^^^^^^^^^^^^^^^

.. code-block:: bash

    student@uso:~/comenzi/ls$ ln -s ~/comenzi/mkdir/ .
    student@uso:~/comenzi/ls$ ls -l
    total 0
    lrwxrwxrwx 1 student student 28 Oct  6 17:58 mkdir -> /home/student/comenzi/mkdir/

Execuția programelor
--------------------

.. code-block:: bash

    student@uso:~/comenzi$ ./my_ls
    executie  mkdir  my_ls	touch


Redirectări simple
------------------

.. code-block:: bash

    student@uso:~$ ls -lh
    total 9.0M
    -rw-r--r-- 1 student student 5.0M Aug 19 11:55 USO
    -rw-r--r-- 1 student student 3.0M Aug 19 11:55 RL
    -rw-r--r-- 1 student student 1.0M Aug 19 11:55 EGC
    student@uso:~$ ls -lh > lista_materii
    student@uso:~$ ls
    EGC lista_materii RL USO


Redirectări prin anexare
^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    student@uso:~$ ls >> lista_materii
    student@uso:~$ ls
    USO RL EGC lista_materii
    student@uso:~$ cat lista_materii
    total 9.2M
    -rw-r--r-- 1 student student 1.0M Aug 19 11:55 EGC
    -rw-r--r-- 1 student student 209K Aug 19 12:00 lista_materii
    -rw-r--r-- 1 student student 5.0M Aug 19 11:55 USO
    -rw-r--r-- 1 student student 3.0M Aug 19 11:55 RL
    EGC
    lista_materii
    RL
    USO


Redirectări de eroare
^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    student@uso:~$ ls
    EGC lista_materii RL USO
    student@uso:~$ cat S02
    cat: S02: No such file or directory
    student@uso:~$ cat S02 2> erori_materii
    student@uso:~$ cat erori_materii
    cat: S02: No such file or directory

Crearea arhivelor - ``tar``
---------------------------

.. code-block:: bash

    student@uso:~$ ls
    înregistrare_lab01.mov înregistrare_lab02.mov înregistrare_lab03.mov
    student@uso:~$ tar cvf înregistrări.tar înregistrare_lab01.mov înregistrare_lab02.mov înregistrare_lab03.mov
    înregistrare_lab01.mov
    înregistrare_lab02.mov
    înregistrare_lab03.mov
    student@uso:~$ ls -lh
    total 19M
    -rw-r--r-- 1 student student 5.0M Aug 19 11:55 înregistrare_lab01.mov
    -rw-r--r-- 1 student student 3.0M Aug 19 11:55 înregistrare_lab02.mov
    -rw-r--r-- 1 student student 1.0M Aug 19 11:55 înregistrare_lab03.mov
    -rw-r--r-- 1 student student 9.1M Aug 19 11:56 înregistrări.tar

Afișarea conținutului arhivelor - ``tar``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    student@uso:~$ tar tf înregistrări.tar
    înregistrare_lab01.mov
    înregistrare_lab02.mov
    înregistrare_lab03.mov

Extragerea fișierelor din arhive - ``tar``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    student@uso:~$ tar xvf înregistrări.tar
    înregistrare_lab01.mov
    înregistrare_lab02.mov
    înregistrare_lab03.mov
    student@uso:~$ ls -lh
    total 19M
    -rw-r--r-- 1 student student 5.0M Aug 19 11:55 înregistrare_lab01.mov
    -rw-r--r-- 1 student student 3.0M Aug 19 11:55 înregistrare_lab02.mov
    -rw-r--r-- 1 student student 1.0M Aug 19 11:55 înregistrare_lab03.mov
    -rw-r--r-- 1 student student 9.1M Aug 19 12:04 înregistrări.tar

Extragerea arhivelor la o cale specifică - ``tar``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    student@uso:~$ ls
    înregistrare_lab01.mov înregistrare_lab02.mov înregistrare_lab03.mov înregistrări.tar
    student@uso:~$ mkdir -p dezarhivare/tar
    student@uso:~$ tar xvf înregistrări.tar --directory dezarhivare/tar/
    înregistrare_lab01.mov
    înregistrare_lab02.mov
    înregistrare_lab03.mov
    student@uso:~$ tree
    .
    |-- dezarhivare
    |   ``-- tar
    |       |-- înregistrare_lab01.mov
    |       |-- înregistrare_lab02.mov
    |       ``-- înregistrare_lab03.mov
    |-- înregistrare_lab01.mov
    |-- înregistrare_lab02.mov
    |-- înregistrare_lab03.mov
    ``-- înregistrări.tar

    2 directories, 7 files

Adăugarea de noi fișiere la arhive - ``tar``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    student@uso:~$ tar rvf înregistrări.tar înregistrare_lab04.mov
    înregistrare_lab04.mov
    student@uso:~$ tar tf înregistrări.tar
    înregistrare_lab01.mov
    înregistrare_lab02.mov
    înregistrare_lab03.mov
    înregistrare_lab04.mov

Comprimare ``tar.gz``
^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    student@uso:~$ tar -czvf inregistrari.tar.gz inregistrare_lab01.mov inregistrare_lab02.mov inregistrare_lab03.mov
    inregistrare_lab01.mov
    inregistrare_lab02.mov
    inregistrare_lab03.mov
    student@uso:~$ ls -l
    -rw-r--r-- 1 student student   9441280 Sep 29 04:51 inregistrari.tar
    -rw-r--r-- 1 student student   9439133 Oct 12 18:55 inregistrari.tar.gz

Crearea arhivelor - ``zip``
---------------------------

.. code-block:: bash

    student@uso:~$ zip înregistrări.zip înregistrare_lab01.mov înregistrare_lab02.mov înregistrare_lab03.mov
      adding: înregistrare_lab01.mov (deflated 0%)
      adding: înregistrare_lab02.mov (deflated 0%)
      adding: înregistrare_lab03.mov (deflated 0%)
    student@uso:~$ ls
    înregistrare_lab01.mov înregistrare_lab02.mov înregistrare_lab03.mov înregistrări.zip

Afișarea conținutului arhivelor  - ``zip``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    student@uso:~$ zip -sf înregistrări.zip
    Archive contains:
      înregistrare_lab01.mov
      înregistrare_lab02.mov
      înregistrare_lab03.mov

Dezarhivarea arhivelor  - ``zip``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    student@uso:~$ ls
    înregistrare_lab01.mov înregistrare_lab02.mov înregistrare_lab03.mov înregistrări.zip
    student@uso:~$ rm înregistrare_lab01.mov înregistrare_lab02.mov  înregistrare_lab03.mov
    student@uso:~$ unzip înregistrări.zip
    Archive:  înregistrări.zip
      inflating: înregistrare_lab01.mov
      inflating: înregistrare_lab02.mov
      inflating: înregistrare_lab03.mov
    student@uso:~$ ls
    înregistrare_lab01.mov înregistrare_lab02.mov înregistrare_lab03.mov înregistrări.zip

Dezarhivarea arhivelor la o cale specifică - ``zip``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    student@uso:~$ mkdir -p dezarhivare/zip
    student@uso:~$ unzip înregistrări.zip -d dezarhivare/zip/
    Archive:  înregistrări.zip
      inflating: dezarhivare/zip/înregistrare_lab01.mov
      inflating: dezarhivare/zip/înregistrare_lab02.mov
      inflating: dezarhivare/zip/înregistrare_lab03.mov
    student@uso:~$ tree
    .
    |-- dezarhivare
    |   |-- zip
    |       |-- înregistrare_lab01.mov
    |       |-- înregistrare_lab02.mov
    |       ``-- înregistrare_lab03.mov
    |-- înregistrare_lab04.mov
    ``-- înregistrări.zip

    2 directories, 5 files

Adăugarea de noi fișiere la arhive - ``zip``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    student@uso:~$ zip -u înregistrări.zip înregistrare_lab04.mov
      adding: înregistrare_lab04.mov (deflated 0%)
    student@uso:~$ zip -sf înregistrări.zip
    Archive contains:
      înregistrare_lab01.mov
      înregistrare_lab02.mov
      înregistrare_lab03.mov
      înregistrare_lab04.mov
    Total 4 entries (16777216 bytes)
