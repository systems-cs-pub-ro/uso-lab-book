Sumar - Cheatsheet
==================

Editor de text
--------------

Editoare cu interfață grafică - Sublime
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

`Cheatsheet Sublime`_

Editor în linia de comandă - nano
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

`Cheatsheet nano`_

.. _Cheatsheet Sublime: https://www.shortcutfoo.com/app/dojos/sublime-text-3-win/cheatsheet
.. _Cheatsheet nano : https://www.nano-editor.org/dist/latest/cheatsheet.html



Redirectare
-----------

Redirectare simplă
^^^^^^^^^^^^^^^^^^

Dacă la folosirea unei direcționări simple (``>``) și fișierul:

1. Există și e gol, atunci scrie în el;

.. code-block:: bash

    student@uso:~$ ls -l USO
    -rw-r--r-- 1 student student 0 Sep 28 16:34 USO
    student@uso:~$ cat USO
    student@uso:~$ echo "USO RULLZ" > USO
    student@uso:~$ cat USO
    USO RULLZ

2. Există și are conținut, atunci suprascrie/înlocuiește conținutul;

.. code-block:: bash

    student@uso:~$ cat ELTH
    ELTH rullz
    student@uso:~$ echo "USO is the b3st" > ELTH
    student@uso:~$ cat ELTH
    USO is the b3st

3. Nu există, atunci fișierul este creat și se scrie ieșirea comenzii în el.

.. code-block:: bash

    student@uso:~$ ls ELTH
    ls: cannot access ELTH: No such file or directory
    student@uso:~$ echo "ELTH rullz" > ELTH
    student@uso:~$ cat ELTH
    ELTH rullz


Redirectare prin anexare
^^^^^^^^^^^^^^^^^^^^^^^^

Dacă la folosirea unei redirectări prin anexare (``>>``) și fișierul:

1. Există și este gol, atunci scrie în el;

.. code-block:: bash

    student@uso:~$ ls -l materii
    -rw-r--r-- 1 student student 0 Sep 28 17:00 materii
    student@uso:~$ cat materii
    student@uso:~$ echo "USO RL ELTH" >> materii
    student@uso:~$ cat materii
    USO RL ELTH

2. Există și are conținut, atunci scrie la sfârșitul fișierului;

.. code-block:: bash

    student@uso:~$ cat materii
    USO RL ELTH
    student@uso:~$ echo "EGC SO2" >> materii
    student@uso:~$ cat materii
    USO RL ELTH
    EGC SO2

3. Nu există, atunci fișierul este creat și se scrie ieșirea comenzii în el.

.. code-block:: bash

    student@uso:~$ rm materii
    student@uso:~$ ls -l materii
    ls: cannot access materii: No such file or directory
    student@uso:~$ echo "USO RL EGC" >> materii
    student@uso:~$ cat materii
    USO RL EGC



