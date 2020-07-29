O înțelegere mai bună a shell-ului
==================================


1) Custom is better
-------------------

Totul este mai bun cu un fișier de configurare

* Prezentare ``alias`` și noțiunea de fișier de configurare: cel mai important, deocamdată: ``.bashrc``. Observare alias-uri existente: ``ls``, ``ll``, ``grep``; și definirea de noi alias-uri
* Utilizarea comenzii ``source`` pentru încărcarea ``.bashrc``


a. Exerciții
^^^^^^^^^^^^

1. Alias pentru search & replace recursiv cu ``find --exec sed -i -e ...``

#. Alias pentru eliminare leading/trailing/extra whitespaces


2) Execuția comenzilor
----------------------

* Terminarea (cu succes) a unei comenzi: ``echo $?``
	* Înlănțuirea comenzilor în funcție de succes/eșec. Ex.
	::

		apt update && apt install -y cmd && cmd 

* Înlănțuirea comenzilor folosind pipe
	* Exemplu utilizare ``xargs``

* Redirectări (reminder)
	* În fișiere și în void (``/dev/null``)
	* Din generatoare ``/dev/zero``, ``/dev/urandom``
	* Selecția stream-urilor de ieșire (``out`` și ``err``), și combinarea lor (``&>``)


a. Exerciții
^^^^^^^^^^^^

1. Clonați repo folosind ``git``. Rulează o anumită comandă, sau un șir de comenzi doar dacă s-a modificat ceva în repo git log pt a vedea dacă s-au făcut modificări în repo build și pus binare generate în ``~/bin``

#. Căutat în repo/cod sursă după un simbol (`grep -nr <simbol>`). Deschis vim la locația unde a fost găsit simbolul.

#. Implementarea unui alias pt `rm` care muta fișierele în `~/Trash`
	* Adăugare intrare în crontab care șterge periodic (1/zi) fișierele mai vechi de T (ex. 30 zile)
	* Utilizare ``find | xargs`` sau ``find --exec`` pentru rezolvare

#. Lansarea în execuție a unui proces care supraviețuiește închiderii terminalului părinte. Inspectarea acestui proces (``lsof``, ``ps``). Trimiterea unor semnale. Oprirea lui. Un mod de a notifica utilizatorul de terminarea cu succes a procesului (mail?)


3) Shell scripting
------------------

* Variabile de mediu: ce sunt, la ce le folosim și care sunt variabilele uzuale (``$HOST``, ``$USER``)
	* ``$PATH`` - la ce este folosit; cum adăugăm ceva la ``$PATH``, ce face export și de ce este util, cum facem ca modificarea ``$PATH`` să fie persistentă (edităm în ``.bashrc``)

* Definirea de variabile cu valori statice (x=42) sau dinamice (x=`ls -l`)

* Oneliners

* Control flow în bash: ``if``, ``for``, ``while read``, ``test``

* Bouns: Definirea de funcții în ``.bashrc``


a. Exerciții
^^^^^^^^^^^^

1. Snippeturi pentru a crea fișiere: sursa main, fișiere header care au ``#ifndef/define/endif __PLACEHOLDER__``, ``Makefile`` etc. Modificarea placeholder-elor cu nume date de utilizator.

#. Creat un director template pentru a fi folosit în inițializarea structurii unor noi proiecte (boilerplate).
	* Generează directoare pt ``src/, build/, gen/, res/`` și fișier ``Readme`` etc.
	* Search and replace după anumite cuvinte placeholder: ex. Numele proiectului în fișierul ``Readme``.
	* Mutat totul într-un script.
	* Script-ul trebuie să primească ca argumente: numele proiectului, repo către github, autor, etc.

#. Scrie un script care generează un fișier Makefile pentru fișierele sursă din directorul curent. Script-ul trebuie să primească tipul fișierelor sursă (`c, cpp, d, java`, etc.) și compilatorul pe care să-l folosească.
	* Pune script-ul în ``~/bin`` și actualizează variabila ``$PATH``.
	* Fă alias-uri pentru cazurile cele mai uzuale: ``c_make_init`` (pt C) și ``cpp_make_init`` pt (C++)

#. Mount în modul read-only al unei partiții (util pt cei care au dualboot și vor să-și monteze discul de Windows, D:\filme, etc).
	* Utilizare sshfs (mount la o partiție prin ssh) - util pt lucrat pe cluster pt cei care folosesc IDE-uri
	* Nu are ce căuta aici, dar nu știam unde să-l pun și nu voiam să uit de el