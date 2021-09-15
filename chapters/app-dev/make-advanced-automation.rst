Aprofundarea folosirii fișierelor Makefile
==========================================

Variabile
-----------------

Nu cred că variabilele au nevoie de o introducere. Au fost cu noi de la începutul carierei noastre de programatori și sunt aici să ne facă viața mai ușoară, fiind placeholdere pentru valorile noastre.
În Makefile-uri, variabilele acționează identic cu variabilele din bash, adică fiind doar înlocuiri textuale.

Astfel, putem simplifica un Makefile de tipul:

.. _app_dev_phony_makefile:

    all: make_exec
    
    make_exec: Fisier_cu_nume_foarte_foarte_foarte_foarte_lung.o
        gcc -o exec Fisier_cu_nume_foarte_foarte_foarte_foarte_lung.c

    TODO.o: Fisier_cu_nume_foarte_foarte_foarte_foarte_lung.c
        gcc -c Fisier_cu_nume_foarte_foarte_foarte_foarte_lung.c
    clean:
        rm exec
        rm *.o

cu ceva mai simplu:

.. _app_dev_phony_makefile:

    NAME=Fisier_cu_nume_foarte_foarte_foarte_foarte_lung

    all: make_exec
    
    make_exec: $(NAME).o
        gcc -o exec $(NAME).c

    TODO.o: $(NAME).c
        gcc -c $(NAME).c
    clean:
        rm exec
        rm *.o

Sintaxa: PLACEHOLDER=text

Inlocuirea este doar la nivel textual, deci textul poate fi reprezentat de orice:

* FLAGS=-Wall -Wextra -C99 -g
* COMPILER=gcc
* EXECUTABLE_NAME=exec
* FISIER=TODO
* Etc...

*Se recomandă numirea variabilelor acestea cu litere mari.*

Pentru utilizare, ca și în bash, se folosește semnul $ urmat de paranteze rotunde în jurul numelui variabilei, astfel: $(NUME_VARIABILA).

Exemplu: 

.. _app_dev_phony_makefile:

    all: $(FISIER).c
        $(COMPILER) -o $(EXECUTABLE_NAME) $(FISIER).c $(FLAGS)

Targetul `.PHONY`
-----------------

În mod implicit, targets-urile Makefile sunt „targets de fișiere” - sunt utilizate pentru a construi fișiere din alte fișiere.
Make presupune că ținta sa este *un fișier* și acest lucru face ca scrierea Makefiles să fie relativ ușoară.

Exemplu:
.. _app_dev_phony_makefile:

    all: make_exec
    
    make_exec: TODO.o
        gcc -o exec TODO.c

    TODO.o: TODO.c
        gcc -c TODO.c
    clean:
        rm exec
        rm *.o

.. _app_dev_understand_using_phony_makefile:

Dacă scrieți o regulă a cărui cod nu va crea fișierul țintă, codul va fi executat de fiecare dată când ținta este chemată. În cazul nostru, targetul clean nu are un fișier de care depinde (asemenea make_exec sau TODO.o), așa că va rula de fiecare dată când va fi chemat prin 'make clean'.
De aici reiese o problema a Makefile-urilor: ele nu vor chema niciodată un target care este 'up-to-date'. Ce înseamnă asta?
Pentru un fișier .c la care nu am adus modificări, acesta rămâne 'up-to-date', deci nu va fi recompilat, ceea ce este un lucru bun, fiindcă nu este nevoie să recompilam un fișier asupra căruia nu am adus modificări.
Dar, dacă în folderul curent avem un fișier cu numele target-ului nostru, de exemplu un fișier cu numele 'clean', ce se va întâmpla?
Atâta timp când fișierul nu este modificat, acesta va rămâne 'up-to-date', iar comanda 'make clean' nu va mai funcționa, pentru că va identifica fișierul care nu a fost modificat cu numele 'clean' în loc de a executa codul dorit.

Soluția se află în target-ul **PHONY**; Acesta specifică faptul că target-urile introduse după acesta **nu** au o legătură directă cu fișierele.

Adăugarea targetului `.PHONY`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Observăm cum suntem protejați de recompilarea fișierului cu extensia .c datorită targetului TODO.o care afișează mesajul "make: 'TODO.o' is up to date." în cazul în care chemăm 'make TODO.O' în timp ce fișierul există.

Exemplu:

.. _app_dev_phony_makefile:

    all: make_exec
    
    make_exec: TODO.o
        gcc -o exec TODO.c

    TODO.o: TODO.c
        gcc -c TODO.c
    clean:
        rm exec
        rm *.o

    .PHONY: clean


Acum, adăugând ultima linie în Makefile, target-ul clean nu va mai fi considerat un fișier (datorita lui PHONY), astfel că putem avea un fișier numit 'clean' și tot putem rula comanda 'make clean'.

Observație legată de targetul PHONY: Dacă adăugăm, separat cu spațiu, alte nume pe lângă 'clean' de mai sus, și aceste target-uri vor fi considerate non-fișiere.
Atenție, PHONY trebuie folosit cu grijă! Dacă am adaugă pe lângă 'clean' și targetul 'TODO.o', am pierde protecția împotriva recompilarii nenecesare și deci am anula utilitatea Makefile-ului.