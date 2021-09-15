Exercițîi suplimentare
======================

Pregătirea mediului de lucru
----------------------------

În această secțiune vom exersa cunoștiințele acumulate despre GitHub în timp ce vom învăța despre utilizarea bibliotecilor statice și dinamice.

Pentru asta, clonati repository-ul de la adresa https://github.com/(TO DO) ce conține:
* un fișier sursă *.c* cu funcția main
* un fișier header *.h* ce implementează o funcție ușoară și un fișier *.c* asociat acestui header
* un Makefile minimal.
De acestea ne vom ajuta să înțelegem practic cele două tipuri de biblioteci existente.

Ce sunt bibliotecile
---------------------------------------------
Aceeași utilitate pe care o au și funcțiile din limbajul C, aceea de a permite scrierea unui cod modularizat și reutilizabil, în același sens funcționează și bibliotecile, permit reutilizarea codului sursă.
Pe scurt, bibliotecile reprezintă un pachet de funcțîi precompilate care te ajută în dezvoltarea mai rapidă a programelor, pentru că tu să nu rescrii acele funcțîi de la zero. Printre cele mai cunoscute biblioteci de C reamintim: stdio.h, strîng.h, stdlib.h, math.h.
Însă, este de avut în vedere faptul că bibliotecile nu sunt executabile, ci doar fișiere de tip header ce includ în procesul de linkeditare fișierul obiect asociat lor, permițându-ți să foloseșți conținutul acestora.

În limbajul C, regăsim două tipuri de biblioteci: *statice* și *dinamice*.
* Diferența majoră dintre ele este faptul că cele statice sunt incluse în fișierul executabil final în compile-time, combinând munca ta cu librăria, în timp ce bibliotecile dinamice sunt combinate la run-time, astfel că nu au nevoie de recompilare sau relink-uire.
* O altă diferență rezultată din prima este faptul că bibliotecile statice sunt mai rapide, deoarece codul binar este inclus direct în cod, dar rezultă și dezavantajul faptului că executabilul final va avea o dimensiune mult mai mare. În schimb, în cazul bibliotecilor dinamice, ele 'trăiesc' independent de program și doar oferă funcțiile care sunt apelate, rezultând un executabil de dimensiuni mai mici,
cu costul timpului care va fi mai mare, datorită faptului că acea funcție trebuie căutată în acesta librărie de fiecare dată.
* În final, avantajul folosirii unei biblioteci dinamice este faptul că poate fi folosită de mai multe procese în același timp, în timp ce o bibliotecă statică este legată de un singur proces.


Crearea unei biblioteci statice și utilizarea ei
---------------------------------------------

Crearea unei biblioteci statice este mai simplă decât a unei biblioteci dinamice.

În trecut, pentru librării precum math, adăugam comenzii de compilare opțiunea: -lm (l - opțiunea de linkuire, m - numele bibliotecii noastre).
În același fel o să procedăm și acum.

Pași:
- Creăm un fișier obiect din fișierul ce implementează funcțiile noastre: gcc -c functions.c
- Arhivam fișierul obiect utilizând comanda: 'ar rcs liball.a functions.o'
# ar - achieve # rcs (c - create / update, r - insert files (replace existing), s - sorted index - pentru acces mai rapid la funcțiile din librăria nou creată).

Utilizare: gcc -o exec main.c -L -lall (L - opțiune ce indică căutarea în fișierul curent, l - opțiunea de linkurile, all - numele pe care l-am dat noi arhivei: *lib* + **all**).

Bibliotecile statice se numesc *archive libraries*, de acolo extensia '.a' a fișierului liball.

Exercițiu
------------------------------------------------------------------------
Adăugați opțiunea de link-uire și în Makefile.

Crearea unei biblioteci dinamice
--------------------------------

Pași:
* Creăm fișierul obiect: gcc -o functions.c 
* Adăugăm fișierului obiect opțiunea 'shared': gcc functions.o -shared -o liball.so.
* În final, fiindcă bibliotecile dinamice pot fi utilizate de mai multe procese în același timp, trebuie să îi facem cunoscută locația către variabilă de mediu (Environmental Variables) LD_LIBRARY_PATH. Rulăm comandă: export LD_LIBRARY_PATH=.:$LD_LIBRARY_PATH.

Utilizare: gcc -o exec main.c liball.so

Bibliotecile dinamice se mai numesc și shared objects, de acolo extensia '.so' a fișierului liball.

Exercițiu
------------------------------------------------------------------------
Adăugați o regulă nouă în Makefile pentru crearea bibliotecii dinamice

Self-Study
------------------------------------------------------------------------
1. Scrieți propria bibliotecă în care să implementați o funcție similară funcției sqrt din math.h.
Că orice inginer, uneori trebuie să ne rezolvăm singuri problemele.
Documentați-va despre LD_PRELOAD și vedeți cum puteți să faceți astfel încât să folosiți *propria* funcție sqrt, chiar dacă executabilul vostru este legat și la biblioteca math.
Testați asta afișând și un scurt mesaj pentru a arată că sqrt-ul vostru a fost chemat, nu cel al bibliotecii math.

Hint: Dacă setați LD_PRELOAD către locația unei fișier de tip shared-objects(librărie dinamică, cu extensia .so), acel fișier va fi prioritizat în defavoarea oricăror altele. Comandă: LD_PRELOAD=/path/to/my/library.so

2. Pentru o aprofundare mai vastă a GitHub și a posibilităților oferite de acesta, documentați-va despre Github Gist.
