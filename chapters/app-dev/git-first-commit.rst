#############
Primul commit
#############

*******************
1) Branch-ul master
*******************

``git branch`` + explicat că pot exista mai multe branch-uri simultan. De adăugat că este best practice să existe câte un branch pentru fiecare feature/bug/fix.

****************************************************
2) Adăugarea unui README și a unui fișier .gitignore
****************************************************

Crearea unui fișier ``README.md`` și un ``.gitignore``.

**************************
3) Crearea primului commit
**************************

a. Verificarea stării clonei
============================

``git status`` + explicații pe output

b. Adăugarea (stage) fișierelor
===============================

``git add`` + ``git status`` + explicații pe output

c. Crearea commitului local cu un mesaj corespunzător
=====================================================

``git fetch`` și cum git pull == git fetch + git merge
``git pull --ff-only`` la bune practici
``git pull`` + explicații (de ce trebuie să dăm mai întâi pull și după aceea push)
``git commit -m "bla"`` + bune practici pentru a scrie un mesaj de commit bun

d. Publicarea commitului pe respository-ul la distanță
======================================================

``git push`` + verificare pe GitHub că apar schimbările.

e. Verificarea istoricului de commituri
=======================================

``git log`` pentru a vedea toate commit-urile făcute pe acest respository