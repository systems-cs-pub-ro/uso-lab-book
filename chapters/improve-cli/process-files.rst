Prelucrarea fișierelor 
======================


1) Crearea și ștergerea fișierelor
----------------------------------

* ``touch``, ``echo > file``, ``mkdir -p``
* ``rm``
	* ``-f``
	* ``-r``
	* ``rm -r`` vs ``rmdir``
* ``tar``, ``zip``, ``unzip``
* ``wget`` și ``curl``


2) Prelucrarea datelor
----------------------

* ``wc``, ``cut``, ``tr``
* ``awk``
* ``sed``
	* inplace replacement ``-i -e``
	* search & replace recursiv cu ``find --exec sed -i -e ...``


a .Exerciții
^^^^^^^^^^^^

1. Avem două fișiere care conțin informații pe coloane. Să se unească cele două fișiere, într-unul singur, păstrându-se structura pe coloane.

#. Se dă un fișier text, în format csv, cu informații despre persoane (nume, prenume, adresă, etc.) Extras informații despre persoanele din fișier și schimbată ordinea coloanelor. Eliminare leading/trailing/extra whitespaces. Sortare după diferite chei. Eliminare duplicate. Adăugare informații default pentru fiecare intrare (ex. cetățenie, angajator, etc.)

#. Urmărirea evoluției unui proces (ex. ``watch top``)
	* Consum de memorie, utilizare CPU, utilizare disk (1)
	* Formatare date: transformare (``cut``, ``tr``, ``awk``, etc.) din snapshots la 2s de informații pe linii, în csv pe coloane
	* Generare grafice cu informațiile de la (1) folosind ``gnuplot``


3) Bune practici pentru editarea fișierelor (reminder)
------------------------------------------------------

* Prezentarea conceptului de ``fg`` (foreground) și ``bg`` (background)
* După ce am editat un fișier îl trimitem în background (nu îl închidem) prin ``ctrl+z``. Verificăm ce ne interesa (ex. Compilăm și rulăm fișierul. Avem o eroare segfault). Folosim ``fg`` pentru a aduce în foreground fișierul text și reluăm editatul. Acum avem avantajul că isoricul modificărilor nu s-a pierdut, ex. putem da undo
* Dacă edităm mai multe fișiere în paralel, folosim comanda jobs pt a vedea fișierele deschise în background și un index asociat. Folosim ``fg #index`` pentru a aduce în prim plan fișierul indicat de indexul respectiv
* Bonus: pentru cei care vor să învețe ``vim`` -> comanda ``vimtutor``
	* Prezentarea conceptului de plugin de snippets: ex. ``Ultisnips`` pt ``vim``


4) Rularea comenzilor cu privilegii elevate
-------------------------------------------

* ``su`` și ``sudo``
	* Verificat mesajul de eroare al comenzilor. Nu trebuie dat cu ``sudo`` atunci când apare o eroare
	* Aici aș pune mai mult accent pe faptul că nu vrei să stai logat ca root (faci o greșeală ca zeu și ai stricat tot sistemu) și nu arunci cu sudo la orice eroare pe care o primești de la o comandă