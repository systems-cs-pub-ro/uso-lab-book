# Prelucrare interactivă cu Vim

## contact.csv

Realizăm o copie a fișierului `names.txt`:

```
$ cp names.txt contact.csv
```

Apoi edităm folosind Vim:

```
$ vi contact.csv
```

Apoi realizăm, în Vim, următoarele acțiuni:

* ``dd``: șterge prima linie, cea de comentariu
* ``qa``: pornește o înregistrare în macro-ul ``a``
* ``0``: ne asigurăm că suntem la început de linie
* ``y$``: copiază linia curentă (nume și prenume)
* ``A``: intră în modul insert la sfârșitul liniei
* ``,``: introdu caracterul virgulă
* ``Esc``: intră în modul ecran
* ``p``: lipește linia copiată
* ``F,``: adu cursorul la virgulă
* ``gu$``: trece conținutul la minuscule
* ``f<Space>``: adu cursorul la spațiu
* ``r.``: înlocuiește caracterul spațiu cu punct
* ``A``: intră în modul insert la sfârșitul liniei
* ``@example.com``: adaugă șirul ``@example.com`` la sfârșitul liniei
* ``Esc``: revino în modul ecran
* ``0``: mergi la începutul liniei
* ``j``: mergi o linie jos
* ``q``: încheie înregistrarea macro-ului ``a``
* ``49@a``: repetă înregistrarea de 49 de ori

## email.txt

Realizăm o copie a fișierului `contacts.csv`:

```
$ cp contact.csv email.txt
```

Apoi edităm folosind Vim:

```
$ vi email.txt
```

Apoi realizăm, în Vim, următoarele acțiuni:

* ``qa``: pornește o înregistrare în macro-ul ``a``
* ``0``: ne asigurăm că suntem la început de linie
* ``f,``: adu cursorul la virgulă
* ``s<Space>``: înlocuiește caracterul curent cu spațiu și intră în modul insert
* ``Esc``: intră în modul ecran
* ``A``: intră în modul insert la sfârșitul liniei
* ``>,``: introdu caracterul ``>,``
* ``Esc``: revino în modul ecran
* ``0``: mergi la începutul liniei
* ``j``: mergi o linie jos
* ``q``: încheie înregistrarea macro-ului ``a``
* ``49@a``: repetă înregistrarea de 49 de ori
* ``gg``: revino la începutul fișierului
* ``qb``: pornește o înregistrare în macro-ul ``b``
* ``0``: ne asigurăm că suntem la început de linie
* ``J``: alăturarea liniei curente cu următoarea linie
* ``0``: mergi la începutul liniei
* ``q``: încheie înregistrarea macro-ului ``a``
* ``48@a``: repetă înregistrarea de 48 de ori
* ``$``: mergi la finalul liniei
* ``x``: ștergi virgula de la finalul liniei
