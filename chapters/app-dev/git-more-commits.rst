#############
Noi comiteri
#############

******************************
1) Repetarea pașilor anteriori
******************************

a. Creare un branch separat
===========================

`git checkout -b <new-branch>`

b. Modificarea fișierului README
================================

modificat folosit nano un fișier

c. Revenire la un alt branch fără comiterea schimbărilor curente
================================================================

`git stash` + `git checkout master`

d. Crearea unui al doilea commit pe branch-ul master
====================================================

`git add` + `git commit -m` + `git push`

e. Revenirea la branch-ul cu modificări și comiterea schimbărilor
=================================================================

`git stash pop` + `git add` + `git commit` + `git commit`

**********************************
2) Modificarea mesajului de commit
**********************************

`git rebase -i HEAD~n` + `git push --force`
