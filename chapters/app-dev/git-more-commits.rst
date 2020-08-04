Crearea unui nou commit
=======================

1) Repetarea pașilor anteriori
------------------------------

a. Crearea unui branch separat
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

``git checkout -b <new-branch>``

b. Modificarea fișierului README
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

modificat folosit nano un fișier

c. Revenirea la alt branch fără crearea unui nou commit cu schimbărilor curente
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

``git stash`` + ``git checkout master``

d. Crearea unui al doilea commit pe branch-ul master
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

``git add`` + ``git commit -m`` + ``git push``

e. Revenirea la branch-ul cu modificări și crearea unui nou commit
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

``git stash pop`` + ``git add`` + ``git commit`` + ``git commit``
``git stash list`` ``git stash show -p`` ``git stash apply``
Poți să faci apply/pop și la altceva decât vârful stivei stash folosind ``git stash pop stash@{2}``.

2) Modificarea mesajului de commit
----------------------------------

``git rebase -i HEAD~n`` + ``git push --force``
