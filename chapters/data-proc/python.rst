.. _data_proc_python:

Introducere în Python
=====================

Python [#python]_ este unul dintre cele mai folosite limbaje de programare.
Avantajele sale sunt simplitatea sintaxei, portabilitatea pe diferite platforme și dezvoltarea rapidă prin prezența a numeroase biblioteci.
Fiind un limbaj interpretat, Python nu este un limbaj care excelează la capitolul viteză.
Acolo unde însă nu este critică viteza de rulare sau resursele consumate, Python este o opțiune foarte bună.
O astfel de opțiune este partea de prelucrare a datelor.
Python este unul dintre limbajele cele mai folosite pentru prelucrarea datelor și în ceea de numim "știința datelor" (*Data Science*)
Utilitatea Python în zona de prelucrare a datelor este conferită de sintaxa sa facilă, suport în prelucrarea șirurilor și prezența structurilor și a operațiilor pentru date de tot felul.

Cea mai recentă versiune de Python, cu sintaxă corespunzătoare este Python3.
Există mici diferențe între Python3 și versiunea anterioară, Python2.
În această carte folosim și recomandăm Python3.


.. _data_proc_python_syntax:

Sintaxa Python
--------------

Python are o sintaxă care seamănă cu limbajul C, dar este simplificată.
Definițiile de variabile și de funcții, instrucțiunile de bază, apelurile de funcții sunt similare cu cele ale limbajului C.

Particularitățile sintaxei Python sunt:

* Nu există acolade pentru blocuri de cod.
  Un nou bloc de cod este definit prin indentare.
  În exemplul de mai jos:

  .. code-block:: python

      if value == 1:
          item = 20
          weight = 10

  variabila ``item`` va avea valoarea ``20``, iar variabila ``weight`` va avea valoarea ``10`` dacă variabila ``value`` are valoarea ``1``.

  Altfel, în exemplul de mai jos:

  .. code-block:: python

      if value == 1:
          item = 20
      weight = 10

  doar variabila ``item`` va avea valoarea ``20`` dacă variabila ``value`` are valoarea ``1``.
  Variabila ``weight`` va avea mereu valoarea ``10``.

* Un bloc de cod începe prin finalizarea sintaxei cu ``:`` (două puncte, *colon*).
  Blocurile ``if``, ``for``, clasele sau funcțiile se încheie cu ``:``.

* Funcțiile se definesc cu ajutorul cuvântului cheie ``def``:

  .. code-block:: python

      def print_message(name):
          print("Hi, " + name)

* O linie de cod se încheie prin ``Enter``.
  Nu există finalizare folosind ``;`` (punct și virgulă, *semi-colon*), ca în C.

* Operatorul ``+`` poate fi folosit pentru a concatena șiruri.

* Există suport nativ pentru liste, dicționare.
  În exemplul de mai jos, ``my_list`` este o listă și ``my_dict`` este dicționar.

  .. code-block:: python

      my_list = ["give", "me", "banners"]
      my_dict = {'name': 'John', 'surname': 'Wick', 'style': 'italian', 'buttons': 2}

* Nu există tipuri în declararea variabile.
  Tipul variabilelor este detectat dinamic la rulare.


.. _data_proc_python_simple_examples:

Exemple simple în Python
------------------------

Să urmărim câteva exemple simple pentru acomodare cu sintaxa Python.
Fișierele de suport se găsesc în directorul ``support/python/`` din directorul acestui capitol:

.. code-block:: bash

    student@uso:~$ cd uso-lab-book/chapters/data-proc/support/python/

    student@uso:~/.../data-proc/support/python$ ls -F
    TODO

hello
^^^^^

Fișierul ``hello.py`` afișează mesajul *Hello, World!*.
Este un fișier simplu, cu un apel al funcției ``print()``.

.. code-block:: python

    #!/usr/bin/env python3

    print("Hello, World!")

Prima linie, de tip *shebang* indică interpretorul folosit.
Se va căuta în mediul de lucru (*environment*) interpretorul Python3.

Pentru rularea scriptului, invocăm interpretorul Python:

.. code-block:: bash

    student@uso:~/.../data-proc/support/python$ python hello.py
    Hello, World!

Putem verifica versiunea interpretorului:

.. code-block:: bash

    student@uso:~/.../data-proc/support/python$ python --version
    Python 3.6.9

Este recomandat ca, atunci când dezvoltăm cod Python, să facem o verificare a stilului codului.
Pentru aceasta folosim utilitarul ``pycodestyle``:

.. code-block:: bash

    student@uso:~/.../data-proc/support/python$ pycodestyle hello.py
    student@uso:~/.../data-proc/support/python$

Dacă nu sunt probleme de stil ale codului, nu se va afișa nimic.

.. important::

    Dacă nu este prezent pe sistem, utilitarul ``pycodestyle`` poate fi instalat folosind comanda:

    .. code-block:: bash

        $ pip install --user pycodestyle

hello_main
^^^^^^^^^^

Fișierul ``hello_main.py`` afișează mesajul *Hello, World!* definind funcția ``main()``:

.. code-block:: python

    def main():
        print("Hello, World!")

Funcția ``main()`` este apelată printr-o construcție specifică limbajului Python:

.. code-block:: python

    if __name__ == "__main__":
        main()

Această construcție este utilă în cazul folosirii sistemului de module în Python.
Un modul poate fi apelat direct (caz în care numele său este ``__main__``) sau poate fi importat de alt modul.
Această construcție duce la invocarea funcției ``main`` doar când modulul curent Python (``hello_main.py``) este apelat direct:

.. code-block:: bash

    student@uso:~/.../data-proc/support/python$ python hello_main.py
    Hello, World!

Tot în acest fișier am adăugat o construcție de tipul Docstring [#docstring]_:

.. code-block:: python

    """
    Simple stupid program: print "Hello, World!" at standard output.
    """

Se recomandă plasarea construcțiilor de tipul Docstring la începutul fiecărui modul Python, la începutul fiecărei clase și la începutul fiecărei funcții.
Rolul lor este de a documenta respectiva componentă.

sum_n
^^^^^

Fișierul ``sum100.py`` afișează suma primelor ``100`` de numere naturale:

.. code-block:: bash

    student@uso:~/.../data-proc/support/python$ python sum100.py
    sum(1,100): 5050

Pentru a parcurge numerele de la ``1`` la ``100`` folosim construcția ``range()`` [#range]_ din Python:

.. code-block:: python

    for i in range(1, 101):
        sum += i

Construcția ``range()`` primește 2 argumente: elementul de start inclusiv (începem de la ``1``) și elementul de oprire exclusiv (ne oprim exclusiv la ``101``).

Ca de obicei, verificăm stilul programului:

.. code-block:: bash

    student@uso:~/.../data-proc/support/python$ pycodestyle sum100.py
    student@uso:~/.../data-proc/support/python$

sum_n_arg
^^^^^^^^^

În fișierul ``sum100.py`` nu avem configurabilă limita pentru care se face suma (*hard-coded*).
Preferăm să trimitem limita (numărul de elemente pentru care se face suma) ca argument în linia de comandă.
Facem acest lucru în fișierul ``sum_n_arg.py``:

.. code-block:: bash

    student@uso:~/.../data-proc/support/python$ python sum_n_arg.py 10
    sum(1,10): 55
    student@uso:~/.../data-proc/support/python$ python sum_n_arg.py 100
    sum(1,100): 5050
    student@uso:~/.../data-proc/support/python$ python sum_n_arg.py 1000
    sum(1,1000): 500500

Accesul la argumentele în lini de comandă se realizează prin intermediul listei ``sys.argv``.
Fiecare element din listă este un argument: ``sys.argv[0]`` este numele programului iar ``sys.argv[1]`` este argumentul efectiv.
Folosirea argumentele necesită importarea modulului ``sys``:

.. code-block:: python


    import sys

    [...]
        if len(sys.argv) != 2:
            usage(sys.argv[0])
            sys.exit(1)

Dacă numărul de argumente în linia de comanandă (lungimea listei -- ``len(sys.argv)``) nu este ``2``, atunci este apelată funcția ``usage()``:

.. code-block:: python

    def usage(argv0):
        print("Usage: {} <num>".format(argv0), file=sys.stderr)

Funcția ``usage()`` primește ca argument numele programului și afișează un mesaj de ajutor pentru utilizator.
Funcția poate inițializa parametrul ``file`` la valoarea ``sys.stderr`` pentru a afișa mesajul la ieșirea de eroare standard (*standard error*).
Altfel, în mod implicit, mesajul este afișat la ieșirea standard (*standard output*).

Pentru formatarea mesajelor folosim metoda ``format()`` specifică șirurilor [#format]_.
Astfel, putem folosi construcții de tipul ``{}`` pentru a preciza locuri în care vor fi expandate argumente ale metodei ``format()``.
Folosim ``format()`` și în afișarea sumei numerelor:

.. code-block:: python

    print("sum(1,{}): {}".format(n, sum))

Argumentul primit (``sys.argv[1]``) este interpretat ca șir.
Pentru a-l converti la întreg, folosim funcționalitatea Python de conversie, folosind ``int()`` [#int]_.
Această conversie poate genera excepții, dacă șirul nu poate fi convertit.
De aceea verificăm generarea unei excepții [#exceptions]_ printr-un block ``try ... except``:

.. code-block:: python

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("Argument is not an integer.", file=sys.stderr)
        sys.exit(1)

Ca de obicei, verificăm stilul programului:

.. code-block:: bash

    student@uso:~/.../data-proc/support/python$ pycodestyle sum_n_arg.py
    student@uso:~/.../data-proc/support/python$

cat
^^^

Fișierul ``cat.py`` afișează conținutul unui fișier primit ca argument și un mesaj de ajutor dacă nu este transmis un argument:

.. code-block:: bash

    student@uso:~/.../data-proc/support/python$ python cat.py
    Usage: cat.py <file>
    student@uso:~/.../data-proc/support/python$ python cat.py sum_n_arg.py
    #!/usr/bin/env python

    import sys


    def usage(argv0):
        print("Usage: {} <num>".format(argv0), file=sys.stderr)
    [...]

Secvența care realizează citirea și afișarea fișierului este:

.. code-block:: python

    with open(fname) as f:
        lines = f.readlines()
        for l in lines:
            print(l.rstrip())

Folosirea cuvântului cheie ``with`` duce la deschiderea unui bloc de lucru cu fișierul.
``f`` este handle-ul fișierului ce va fi închis automat la finalul blocului ``with``.
Se obține lista de linii din fișier folosind ``f.readlines()`` și apoi este parcursă folosind ``for``.
Pentru fiecare linie sunt eliminate spațiile albe (caracterele ``newline``) de la finalul fiecărei linii, folosind metoda ``rstrip()`` a șirului (de la ``right side strip``).

Ca de obicei, verificăm stilul programului:

.. code-block:: bash

    student@uso:~/.../data-proc/support/python$ pycodestyle cat.py
    student@uso:~/.../data-proc/support/python$

num_lines
^^^^^^^^^

Fișierul ``num_lines.py`` afișează numărul de linii ale unui fișier primit ca argument:

.. code-block:: bash

    student@uso:~/.../data-proc/support/python$ python num_lines.py num_lines.py
    Number of lines in num_lines.py is 32.
    student@uso:~/.../data-proc/support/python$ python num_lines.py cat.py
    Number of lines in cat.py is 32.
    student@uso:~/.../data-proc/support/python$ python num_lines.py sum_n_arg.py
    Number of lines in sum_n_arg.py is 29.

Conținutul său este similar cu cel al fișierului ``cat.py``.
Partea care diferă este cea care contorizează numărul de linii, folosind funcția ``len()`` pe lista de linii citită din fișier:

.. code-block:: python

    num = len(lines)
    print("Number of lines in {} is {}.".format(fname, num))

Ca de obicei, verificăm stilul programului:

.. code-block:: bash

    student@uso:~/.../data-proc/support/python$ pycodestyle num_lines.py
    student@uso:~/.../data-proc/support/python$

tac
^^^

Fișierul ``tac.py`` afișează în linie inversă liniile unui fișier primit ca argument:

.. code-block:: bash

    student@uso:~/.../data-proc/support/python$ python tac.py num_lines.py
        main()
    if __name__ == "__main__":


            print("Number of lines in {} is {}.".format(fname, num))
    [...]

Conținutul său este similar cu cel al fișierului ``cat.py``.
Partea care diferă este cea care obține liniile fișierului, în linie inversă, folosindu-se de sintaxa Python ``[::-1]``:

.. code-block:: python

    lines = f.readlines()[::-1]

Ca de obicei, verificăm stilul programului:

.. code-block:: bash

    student@uso:~/.../data-proc/support/python$ pycodestyle tac.py
    student@uso:~/.../data-proc/support/python$


.. _data_proc_python_data_structures:

Structuri de date în Python
---------------------------

Python este un limbaj puternic și util în zona de prelucrare a datelor datorat structurilor de date [#data_structures]_ pe care le oferă și a operațiilor facile cu acestea.
În Python putem ușor lucra cu șiruri, liste, tupluri, dicționare.

Mai jos arătăm exemple de declarare și folosire a structurilor de date Python.
Pentru aceasta folosim consola interactivă Python, prin rularea comenzii ``python``:

.. code-block:: bash

    student@uso:~/.../data-proc/support/python$ python
    [...]
    Type "help", "copyright", "credits" or "license" for more information.
    >>>

Promptul ``>>>`` este locul unde putem introduce instrucțiuni Python.

Șiruri
^^^^^^

Șirurile sunt un tip de date specific în Python.

Șirurile pot fi concatenate folosind operatorul ``+``.
Se pot obține subșiruri prin indexarea lor, ca în exemplele de mai jos, rulate în consola Python:

.. code-block:: bash

    >>> my_str = "this is the way"
    >>> my_str
    this is the way
    >>> my_str[0]
    t
    >>> my_str[0:2]
    th
    >>> my_str[2:3]
    i
    >>> my_str[5:7]
    is
    >>> full = my_str[12:] + ".org"
    >>> full
    way.org
    >>> full[:-4]
    way
    >>> full[::-1]
    gro.yaw

Avem mai multe construcții pentru a obține secvențe de șiruri:

* Un index numeric obține caracterul de la acea poziție.
  Indexul poate fi negativ caz în care se contorizează de la coadă la cap.
* O secvența de tipul ``[x:y]`` selectează subșirul de la poziția ``x`` până la poziția ``y-1``.
  Indexurile pot fi negative.
* O secvență de tipul ``[x:]`` selectează subșirul de la poziția ``x`` până la sfârșit, în vreme ce o secvență de forma ``[:y]`` selectează subșirul de la început până la poziția ``y``.
  Indexurile pot fi negative.
* O secvență de tipul ``[x:y:z]`` selectează cu pasul ``z``.
  Dacă ``z`` este ``-1`` selectează de la coadă la cap, furnizând astfel, o inversare a unui șir sau subșir.

În mod implicit, șirurile sunt imutabile, adică nu pot fi modificate.
Un șir nou se creează de la zero folosind, eventual, părți din alte șir.
Astfel, dacă urmărim să modificăm direct un șir, vom obține eroare:

.. code-block:: bash

    >>> full[0] = 'b'
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: 'str' object does not support item assignment

Lungimea unui șir se obține folosind funcția ``len()``:

.. code-block:: bash

    >>> len(full)
    7
    >>> len(full[0])
    1
    >>> len(full[0:2])
    2

Elementele (caracterele) unui șir pot fi parcurse într-o buclă ``for``:

.. code-block:: bash

    >>> for c in full:
    ...     print("char: '{}', ascii: {} (0x{:02x})".format(c, ord(c), ord(c)))
    ...
    char: 'w', ascii: 119 (0x77)
    char: 'a', ascii: 97 (0x61)
    char: 'y', ascii: 121 (0x79)
    char: '.', ascii: 46 (0x2e)
    char: 'o', ascii: 111 (0x6f)
    char: 'r', ascii: 114 (0x72)
    char: 'g', ascii: 103 (0x67)

Funcția ``ord()`` afișează valoarea ASCII numerică aferentă unui caracter.

Șirurile pot fi împărțite în subșiruri pe baza unui caracter separator, folosin metoda ``split()``:

.. code-block:: bash

    >>> my_str.split(' ')
    ['this', 'is', 'the', 'way']

Rezultatul este o listă de subșiruri.

Tupluri
^^^^^^^

În Python variabilele pot fi grupate în tupluri, similar unei structuri de date simple, cu mai multe câmpuri:

.. code-block:: bash

    >>> student = ('John', 'Smith', 'john.smith@example.com')

Similar șirurilor, tuplurile sunt imutabile.
Nu le putem modifica dar putem extrage elemente sau secvențe de elemente:

.. code-block:: bash

    >>> print(student[0])
    John
    >>> print(student[1])
    Smith
    >>> print(student[0:2])
    ('John', 'Smith')
    >>> for f in student:
    ...     print(f)
    ...
    John
    Smith
    john.smith@example.com

Putem converti un tuplu la o listă folosind funcția ``list()``:

.. code-block:: bash

    >>> student_as_list = list(student)
    >>> student_as_list
    ['John', 'Smith', 'john.smith@example.com']

Tuplurile și listele, prezentate mai jos, sunt destul de similare, cu diferența că listele sunt mutabile (pot fi modificate) și că există un număr mai mare de metode built-in pentru liste [#list_vs_tuple]_.

Liste
^^^^^

Listele sunt, în general, o secvență de element de același tip.
Putem avea liste de întregi, liste de șiruri, liste de tupluri sau liste de liste.
Totuși, deși nu este ceva obișnuit, listele pot avea și elemente de tipuri diferite.

Operațiile uzuale pe șiruri și tupluri sunt prezente și pe liste:

.. code-block:: bash

    >>> food = ['pizza', 'pasta', 'lasagna', 'risotto', 'rigatoni']
    >>> len(food)
    5
    >>> food[0]
    'pizza'
    >>> food[0:2]
    ['pizza', 'pasta']
    >>> food[::-1]
    ['rigatoni', 'risotto', 'lasagna', 'pasta', 'pizza']

Spre deosebire de șiruri și tupluri, listele sunt mutabile.
Putem modifica elemente din listă sau putem adăuga sau șterge elemente:

.. code-block:: bash

    >>> food
    ['pizza', 'pasta', 'bruschetti', 'risotto', 'rigatoni']
    >>> food.append('caprese')
    >>> food
    ['pizza', 'pasta', 'bruschetti', 'risotto', 'rigatoni', 'caprese']
    >>> food.insert(2, 'gelato')
    >>> food
    ['pizza', 'pasta', 'gelato', 'bruschetti', 'risotto', 'rigatoni', 'caprese']

Listele pot fi sortate:

.. code-block:: bash

    >>> food
    ['pizza', 'pasta', 'gelato', 'bruschetti', 'risotto', 'rigatoni', 'caprese']
    >>> sorted(food)
    ['bruschetti', 'caprese', 'gelato', 'pasta', 'pizza', 'rigatoni', 'risotto']
    >>> sorted(food, reverse=True)
    ['risotto', 'rigatoni', 'pizza', 'pasta', 'gelato', 'caprese', 'bruschetti']
    >>> food.sort()
    >>> food
    ['bruschetti', 'caprese', 'gelato', 'pasta', 'pizza', 'rigatoni', 'risotto']
    >>> food.reverse()
    >>> food
    ['risotto', 'rigatoni', 'pizza', 'pasta', 'gelato', 'caprese', 'bruschetti']

Funcția ``sorted()`` întoarce o listă sortată.
Folosind argumentul ``reverse=True`` sortarea poate fi inversată.

Funcția internă ``sort()`` sortează lista *in-place*, adică se modifică lista.
În mod similar, funcție internă ``reverse()`` inversează lista *in-place*.

Ca și celelalte structuri, listele pot fi parcurse folosind ``for``:

.. code-block:: bash

    >>> for f in food:
    ...     print(f)
    ...
    risotto
    rigatoni
    pizza
    pasta
    gelato
    caprese
    bruschetti

List Comprehension
""""""""""""""""""

Un mod rapid de a crea liste este folosind funcționalitatea de *list comprehension* [#list_comprehension]_:

.. code-block:: bash

    >>> sq_list = [x**2 for x in range(10)]
    >>> sq_list
    [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


.. code-block:: bash

    >>> select_food = [f for f in food if 'r' in f]
    >>> select_food
    ['risotto', 'rigatoni', 'caprese', 'bruschetti']

*List comprehension* este o metodă rapidă și compactă de a crea liste din elemente existente.

Dicționare
^^^^^^^^^^

Dicționarele sunt o structură asociativă: asociază o valoare (*value*) la o cheie (*key*).
Elementele unui dicționar sunt așadar perechi cheie-valoare (*key-value*).
Indexarea unui dicționar (accesul la un element) este realizată prin cheie (*key*) nu printr-un index numeric cum este cazul șirurilor, tuplurilor sau listelor:

.. code-block:: bash

    >>> preferences = {'food': 'houmous', 'car': 'audi', 'film': 'interstellar', 'place': 'istanbul'}
    >>> preferences['food']
    'houmous'
    >>> preferences['place']
    'istanbul'
    >>> preferences['place'] = 'rome'
    >>> preferences
    {'food': 'houmous', 'car': 'audi', 'film': 'interstellar', 'place': 'rome'}

La fel ca listele, dicționarele sunt mutabile: putem înlocui un element dintr-un dicționar, cum am înlocuit în secvența de comenzi de mai sus valoarea pentru cheia ``place``.

La parcurgerea implicită a unui dicționar, se vor obține cheile.
Altfel, putem folosi metoda internă ``items()`` pentru a parcurge simultan cheile și valorile:

.. code-block:: bash

    >>> for k in preferences:
    ...     print("k: {}, v: {}".format(k, preferences[k]))
    ...
    k: food, v: houmous
    k: car, v: audi
    k: film, v: interstellar
    k: place, v: rome
    >>> for k, v in preferences.items():
    ...     print("k: {}, v: {}".format(k, v))
    ...
    k: food, v: houmous
    k: car, v: audi
    k: film, v: interstellar
    k: place, v: rome

Valorile unui dicționar pot fi convertite într-o listă.

.. code-block:: bash

    >>> l = list(preferences)
    >>> l
    ['food', 'car', 'film', 'place']

Sortarea unui dicționar se aplică pe cheile sale:

.. code-block:: bash

    >>> sorted(preferences)
    ['car', 'film', 'food', 'place']
    >>> dict(sorted(preferences.items()))
    {'car': 'audi', 'film': 'interstellar', 'food': 'houmous', 'place': 'rome'}

Pentru sortarea după valori, va trebui să apelăm la expresii Lambda [#lambda_expressions]_:

.. code-block:: bash

    >>> sorted(preferences.items(), key=lambda item: item[1])
    [('car', 'audi'), ('food', 'houmous'), ('film', 'interstellar'), ('place', 'rome')]
    >>> dict(sorted(preferences.items(), key=lambda item: item[1]))
    {'car': 'audi', 'food': 'houmous', 'film': 'interstellar', 'place': 'rome'}

Contrucția ``item[1]`` este echivalentul valorii, în vreme ce ``item[0]``` ar fi echivalentul cheii.

Sumar
^^^^^

Python dispune de mai multe tipuri de date: șiruri, liste, tupluri, dicționare.
În prelucrarea datelor (adesea de tip șir) putem folosi liste, tupluri sau dicționare.
Fiecare tip de date are avantaje și dezavantaje.
Alegerea între aceste tipuri de date ține de formatul datelor și de operațiile de care avem nevoie pentru acestea.
Este posibil să combinăm aceste tipuri de date și să avem liste de tupluri, dicționare de liste etc.
Pentru cazuri de utilizare mai complexe, se poate ajunge la folosirea claselor [#class]_ ca tipuri de date mai complexe.

.. _data_proc_python_proc_examples:

Exemple de prelucrare în Python
-------------------------------

exemplele din secțiunea precedentă în Python


.. _data_proc_python_tasks:

Exerciții
---------

exercițiile din secțiunea precedentă în Python

.. rubric:: Note de subsol

.. [#python]

    https://www.python.org/

.. [#docstring]

    https://www.python.org/dev/peps/pep-0257/

.. [#range]

    https://docs.python.org/3/library/functions.html#func-range

.. [#format]

    https://pyformat.info/

.. [#int]

    https://docs.python.org/3/library/functions.html#int

.. [#exceptions]

    https://docs.python.org/3/tutorial/errors.html

.. [#data_structures]

    https://docs.python.org/3/tutorial/datastructures.html

.. [#list_vs_tuple]

    https://www.upgrad.com/blog/list-vs-tuple/

.. [#list_comprehension]

    https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions

.. [#class]

    https://docs.python.org/3/tutorial/classes.html

.. [#lambda_expressions]

    https://docs.python.org/3/tutorial/controlflow.html#lambda-expressions
