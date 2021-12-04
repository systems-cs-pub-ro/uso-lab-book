.. _users_perms_privileged_access:

Accesul privilegiat
===================

În sistemul de operare există acțiuni critice (*critical / sensitive actions*): configurarea rețelei, instalarea de aplicații, adăugarea de noi conturi de utilizatori, configurarea serviciilor sistemului.
Aceste acțiuni afectează funcționarea sistemului de operare și pot cauza probleme (de funcționare, de securitate) la o utilizare necorespunzătoare;
de exemplu, configurarea greșită a rețelei poate duce la lipsa de conectivitate la Internet;
adăugarea unui cont nou poate permite accesul unor persoane nedorite la nivelul sistemului;
instalarea unei aplicații poate duce la rularea de malware la nivelul sistemului.
De aceea aceste acțiuni pot fi realizate doar într-un **mod privilegiat**.

Modul privilegiat este activat cel mai adesea prin accesarea unui **cont de utilizator privilegiat**.
Spunem, așadar, că pe un sistem avem conturi de utilizator obișnuite (*regular users*) și conturi de utilizator privilegiat (*privileged user*).
Utilizatorul privilegiat se mai numește **administrator**, **admin** sau **superuser**.
În Linux, utilizatorul privilegiat se numește **root**.

Un utilizator obișnuit nu poate realiza acțiuni critice;
doar utilizatorul privilegiat poate.
De aceea, va trebui să accesăm utilizatorul privilegiat pentru realizarea acțiunilor critice.

.. _users_perms_privileged_sudo:

Folosirea ``sudo``
------------------

Accesarea contului privilegiat se realizează cel mai simplu, în Linux, cu ajutorul comenzii ``sudo``.
De exemplu, dacă dorim să instalăm o aplicație din contul obișnuit, vom primi eroare:

.. code-block:: bash

    student@uso:~$ apt install nmap
    E: Could not open lock file /var/lib/dpkg/lock-frontend - open (13: Permission denied)
    E: Unable to acquire the dpkg frontend lock (/var/lib/dpkg/lock-frontend), are you root?

Această acțiune va reuși, însă, dacă prefixăm comanda cu ``sudo``:

.. code-block:: bash

    student@uso:~$ sudo apt install nmap
    Reading package lists... Done
    Building dependency tree
    Reading state information... Done
    nmap is already the newest version (7.60-1ubuntu5).
    0 upgraded, 0 newly installed, 0 to remove and 0 not upgraded.

.. important::

    Contul privilegiat (**root**) accesat prin intermediul comenzii ``sudo`` are putere deplină asupra sistemului.
    Poate realiza toate acțiunile posibile (critice sau necritice).
    De aceea, este riscantă accesarea acestui cont: o comandă rulată greșit poate duce la probleme grave la nivelul sistemului.

    O comandă celebră, destinată începătorilor, este ``sudo rm -rf /``.
    În mod amuzant, se spune că această comandă citește e-mailuri foarte rapid (*read mail really fast*).
    În realitate comanda șterge întregul sistem de fișiere, de la rădăcină (``/``), făcând sistemul nefuncțional și ducând la pierderea datelor.

    De aceea, contul privilegiat trebuie accesat cât mai rar, **doar atunci când este nevoie**.
    În mod implicit, un utilizator se autentifică în sistem cu un cont neprivilegiat (de exemplu ``student``), urmând să acceseze contul privilegiat (**root**) doar la nevoie.

Exercițiu: Acțiuni privilegiate
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Realizați următoarele acțiuni din contul de utilizator obișnuit ``student`` și vedeți care are nevoie de acces privilegiat.
Explicați de ce unele au nevoie de acces privilegiat.

* ``touch /home/student/a.txt``
* ``apt install strace``
* ``ip address show``
* ``cat /etc/passwd``
* ``cat /etc/shadow``
* ``touch /etc/test.conf``
* ``touch /tmp/my.data``
* ``service ssh restart``
* ``dmesg``
* ``dmesg -c``

Erori de permisiuni și alte erori
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

O confuzie frecventă apare între erorile de permisiuni și erorile de altă natură.
De exemplu, atunci când afișăm conținutul unui fișier, putem avea următoarele situații:

.. code-block:: bash

    student@uso:~$ cat /var/log/boot.log
    cat: /var/log/boot.log: Permission denied

    student@uso:~$ cat /var/log/kill/them/all.log
    cat: /var/log/kill/them/all.log: No such file or directory

Prima comandă afișează o eroare de permisiune (*Permission denied*).
A doua afișează o eroare de sistem de fișiere: fișierul care se dorește afișat nu există (*No such file or directory*).

Doar erorile de permisiune sunt "rezolvabile" folosind contul privilegiat, care are acces complet în sistem.
Celelalte tipuri de erori nu sunt rezolvate astfel, trebuie găsită sursa problemei.
Astfel că, dacă prefixăm cele două comenzi de mai sus cu ``sudo``, pentru folosirea contului privilegiat, vom obține:

.. code-block:: bash

    student@uso:~$ sudo cat /var/log/boot.log
    [  OK  ] Started Show Plymouth Boot Screen.
    [  OK  ] Started Forward Password Requests to Plymouth Directory Watch.
    [  OK  ] Reached target Local Encrypted Volumes.
    [...]
    student@uso:~$ sudo cat /var/log/kill/them/all.log
    cat: /var/log/kill/them/all.log: No such file or directory

Observăm că prima comandă, care afișase eroare de permisiune, funcționează acum.
În vreme ce a doua comandă, care afișase eroare de sistem de fișiere, nu își schimbă comportamentul: afișează în continuare aceeași eroare.

Exercițiu: Erori de permisiune și erori de alte tipuri
""""""""""""""""""""""""""""""""""""""""""""""""""""""

Rulați următoarele comenzi fără ``sudo``.
Aceste comenzi vor afișa mesaje de eroare.
Fără a folosi ``sudo``, stabiliți care comenzi generează erori de permisiuni (rezolvabile cu ``sudo``) și alte tipuri de erori (nerezolvabile folosind ``sudo``).
Apoi rulați folosind ``sudo`` pentru a confirma presupunerile.

* ``apt install sports-illustrated``
* ``ip address show ether114``
* ``kill $(pidof chainsaw)``
* ``netcat -l -p 700``
* ``chown student:student /home/student``
* ``chown student:student /home/search/and/destroy``
* ``userdel hariseldon``

În cazul comenzilor care afișează alte tipuri de erori, presupunând rezolvarea lor, este posibil, în continuare să fie nevoie de ``sudo``.
Care dintre comenzile de mai sus intră în această categorie?

Redirectare folosind sudo
^^^^^^^^^^^^^^^^^^^^^^^^^

Fie o situație în care dorim să scriem informație într-un fișier.
Să presupunem că dorim să scriem informația *All for the empire* în fișierul ``/home/student/zealot.txt``.
Avem două opțiuni:

#. Edităm fișierul folosind ``nano /home/student/zealot.txt``, scriem informația *All for the empire** și apoi salvăm.
#. Folosim comanda ``echo "All for the empire" > /home/student/zealot.txt``.

Ambele opțiuni vor funcționa, utilizatorul curent ``student`` (neprivilegiat) având permisiuni de editare / creare.

Dacă alegem un fișier la care utilizatorul curent nu are acces, intuiția ar fi să prefixăm comenzile de mai sus ``sudo``.
Adică, în cazul fișierului ``/etc/zealot.txt``, am realiza acțiunile:

#. Edităm fișierul folosind ``sudo nano /etc/zealot.txt``, scriem informația *All for the empire* și apoi salvăm.
#. Folosim comanda ``sudo echo "All for the empire" > /etc/zealot.txt``.

Prima comandă (folosirea editorului) funcționează.
A doua comandă însă nu funcționează.

A doua comandă nu funcționează pentru că doar comanda ``echo`` rulează în modul privilegiat.
Redirectarea (dată de operatorul ``>``) este realizată de proces shell, care aparține utilizatorului neprivilegiat ``student``.
Adică se deschide, cu ajutorul redirectării, fișierul ``/etc/zealot.txt`` cu permisiunile utilizatorului ``student``;
pentru că fișierul este deschis de un utilizator neprivilegiat, acțiunea eșuează.

Sunt două soluții:

#. Folosirea unui proces shell privilegiat.
#. Folosirea unei comenzi prefixată de comanda ``sudo``, comandă care să deschidă fișierul ``/etc/zealot.txt`` fără redirectare.
   În felul acesta fișierul va fi deschis în modul privilegiat.

Pentru prima variantă, folosim comenzile:

.. code-block:: bash

    student@uso:~$ sudo su
    root@uso:/home/student# echo "All for the empire" > /etc/zealot.txt

În această situație, a doua comandă este rulată cu permisiunile contului privilegiat (``root``).

Pentru a doua variantă, putem folosi comanda ``tee`` care primește ca argument un fișier în care scrie informație.
Prefixarea cu ``sudo`` va duce la rularea comenzii ``tee`` în mod privilegiat, adică și la deschiderea fișierului ``/etc/zealot.txt`` în mod privilegiat.
Comanda folosită este:

.. code-block:: bash

    student@uso:~$ echo "All for the empire" | sudo tee /etc/zealot.txt
    All for the empire

Comanda ``tee`` are ca efect scrierea informației în fișierul primit ca argument **și** la ieșirea standard.
Din acest motiv mesajul ``All for the empire`` apare **și** în fișierul ``/etc/zealot.txt`` **și** la ieșirea standard.

.. note:: Comanda ``tee`` în modul append

    În forma implicită de mai sus, comanda ``tee`` suprascrie conținutul fișierului primit ca argument.
    Dacă dorim să adăugăm conținut în fișier (*append*), folosim opțiunea ``-a`` a comenzii ``tee``:

    .. code-block:: bash

        student@uso:~$ echo "All for the empire" | sudo tee -a /etc/zealot.txt

Shell privilegiat
^^^^^^^^^^^^^^^^^

Adesea dorim realizarea mai multor acțiuni critice, în forma rulării mai multor comenzi.
Pentru aceasta, cel mai simplu este să folosim un proces shell care rulează în mod privilegiat.

Așa cum am văzut mai sus, folosim comanda ``sudo su`` pentru obținerea unui shell privilegiat:

.. code-block::

    student@uso:~$ sudo su
    root@uso:/home/student#

Promptul ne indică prezența shellului privilegiat:

* utilizatorul este ``root``, utilizatorul privilegiat
* promptul se încheie în caracterul ``#`` (*diez*), caracter care denotă, prin convenție, un shell privilegiat

Același efect poate fi obținut prin rularea comenzii ``sudo su root``:

.. code-block::

    student@uso:~$ sudo su root
    root@uso:/home/student#

Fiind mai mult de tastat, preferăm folosirea comenzii ``sudo su`` în loc de ``sudo su root``.

Un alt mod de a obține un shell de root este cu ajutorul comenzii ``sudo bash``, cu aceleași efecte ca mai sus:

.. code-block::

    student@uso:~$ sudo bash
    root@uso:/home/student#

Ambele comenzi (``sudo su``, respectiv ``sudo bash``), duc la rularea unor comenzi în mod privilegiat: comanda ``su`` este rulată privilegiat, comanda ``bash`` este rulată privilegiat.
Efectul este crearea unui proces shell Bash care rulează privilegiat;
și, deci, un shell în cadrul căruia putem rula comenzi în mod privilegiat.

Pentru a închide procesul shell care rulează în mod privilegiat folosim comenzile uzuale de închidere a shellului: ``exit``, ``logout`` sau combinația de taste ``Ctrl+d``.
După încheierea procesului shell privilegiat, vom reveni în procesul shell inițial.

.. note::

    Vom prezenta mai multe despre procese și utilizatori în secțiunea :ref:`users_perms_processes`.

    Vom prezenta detalii despre comanda ``su`` în secțiunea :ref:`users_perms_privileged_su`.

Exerciții: Shell privilegiat
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Folosiți, pe rând, comenzile ``sudo su`` și ``sudo bash`` pentru a obține un shell privilegiat.
   Apoi folosiți comanda ``exit`` sau comanda ``logout`` sau combinația de taste ``Ctrl+d`` pentru a închide shellul curent.

#. Folosiți comanda ``sudo su`` pentru a obține un shell privilegiat.
   În noul shell privilegiat folosiți comanda ``sudo su`` pentru a obține un nou shell privilegiat.
   Folosiți două instanțe de comenzi de închidere a shellului (``exit`` sau ``logout`` sau ``Ctrl+d``) pentru a reveni la shellul inițial (neprivilegiat).

.. _users_perms_privileged_id:

Identificarea utilizatorului
----------------------------

Promptul shellului este configurabil și poate să nu ofere informații despre utilizatorul curent.
Pentru siguranță, folosim comenzi dedicate pentru identificarea utilizatorului curent.

whoami
^^^^^^

Cea mai directă comandă, pentru afișarea numelui utilizatorului curent (*username*) este comanda ``whoami``:

.. code-block:: bash

    student@uso:~$ whoami
    student
    student@uso:~$ sudo whoami
    root

Rularea comenzii ``whoami`` duce la afișarea utilizatorului curent (``student``).
Prefixarea comenzii cu ``sudo`` duce la afișarea numelui utilizatorului privilegiat (``root``).

id
^^

O comandă care permite afișarea de informații despre utilizatori este comanda ``id``.
O utilizare simplă a comenzii afișează informații extinse despre utilizatorul curent:

.. code-block:: bash

    student@uso:~$ id
    uid=1000(student) gid=1000(razvan) groups=1000(student),4(adm),24(cdrom),27(sudo),30(dip),46(plugdev),116(lpadmin),126(sambashare),128(kvm),130(docker)

Pentru utilizatorul curent se afișează:

* identificatorul utilizatorului (*user id*, ``uid``), o valoare numerică, aici ``1000``
* numele utilizatorului (*username*), șirul pe care îl folosim, aici ``student``
* identificatorul grupului utilizatorului (*group id*, ``gid``) și numele grupului (*group name*), aici ``1000`` și ``student`` (poate fi considerată o coincidență egalitatea cu identificatorul utilizatorului și numele utilizatorului)
* alte grupuri din care face parte utilizatorul (*groups*)

Vom prezenta succint partea de grupuri în secțiunea TODO.

Relevante în acest moment sunt informațiile legate de identificatorul și de numele utilizatorului.
Identificatorul utilizatorului (**UID**) este folosit de sistemul de operare pentru verificarea permisiunilor.
Numele utilizatorului este folosit de noi, oamenii, care reținem mai ușor șiruri / nume în loc de numere.
Similar se întâmplă și pentru procese: sistemul de operare le identifică după un număr numit **PID** (*process identifier*).

Orice utilizator are un identificator (pentru sistemul de operare) și un nume (pentru oameni).
De obicei, primul utilizator obișnuit (neprivilegiat) de pe un sistem Linux are identificatorul ``1000``;
este cazul utilizatorului ``student`` de mai sus.

Putem folosi comanda ``id`` pentru a afișa informații și despre alți utilizatori ai sistemului, de exemplu despre utilizatorul privilegiat (``root``):

.. code-block:: bash

    razvan@uso:~$ id root
    uid=0(root) gid=0(root) groups=0(root)

    razvan@uso:~$ id -u root
    0

    razvan@uso:~$ id -un 0
    root

În prima comandă rulată am afișat informații despre utilizatorul ``root``.
Utilizatorul are UID-ul ``0``;
acesta este modul în care este recunoscut de sistemul de operare.
Practic, numele ``root`` este o convenție;
ceea ce oferă privilegii unui proces este prezența UID-ului ``0`` ca atribut al procesului.

Putem afișa doar UID-ul unui utilizator prin folosirea opțiunii ``-u`` a comenzii ``id``, ca în a doua comandă de mai sus.
La fel putem afișa doar numele corespunzător unui UID prin folosirea opțiunii ``-un``, ca în a treia comanda de mai sus.

Exerciții: Identificarea utilizatorilor
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Obțineți un shell privilegiat.
   Folosiți comenzile ``whoami`` și ``id`` pentru a afișa informații despre utilizatorul curent (``root``).

   Folosiți comanda ``id`` pentru a afișa identificatorul utilizatorului ``student``.

#. Dintr-un shell de orice fel (privilegiat sau neprivilegiat), afișați:

   * UID-ul utilizatorului ``daemon``.
   * UID-ul utilizatorului ``syslog``.
   * Numele utilizatorului cu UID-ul ``100``.
   * Numele utilizatorului cu UID-ul ``2``.

   Acești utilizatori sunt utilizatori de sistem (*system users*), neinteractivi - adică nu sunt utilizatori cu care ne putem autentifica în sistem.
   Vom discuta succint despre aceștia în secțiunea TODO.

.. _users_perms_privileged_su:

Schimbarea utilizatorului
-------------------------

Mai sus am folosit comanda ``sudo su`` pentru a obține un proces shell privilegiat.
Comanda duce, de fapt, la rularea privilegiată a comenzii ``su``.

Comanda ``su`` este folosită pentru schimbarea utilizatorului.
În forma sa simplă (fără argumente) schimbă utilizatorul în utilizatorul privilegiat (``root``).
Schimbarea unui utilizator va cere parola utilizatorului schimbat.
Astfel, în cazul comenzii de mai jos, se va cere parola contului ``root``:

.. code-block:: bash

    student@uso:~$ su
    Password:
    su: Authentication failure

Întrucât nu știm parola contului ``root``, am apăsat ``Enter`` și a fost afișat mesaj de eroare de autentificare.

Comanda ``su`` poate fi folosită pentru a schimba utilizatorul în cel al cărui nume a fost primit ca argument.
De exemplu, comanda de mai jos ar avea ca efect schimbarea utilizatorului curent în utilizatorul ``daemon``.
Din nou, necunoscând parola, nu vom reuși autentificarea:

.. code-block:: bash

    student@uso:~$ su daemon
    Password:
    su: Authentication failure

Atunci când prefixăm comanda ``su`` de comanda ``sudo`` se rulează ``su`` în mod privilegiat și nu mai este necesară parola contului ``root``:

.. code-block:: bash

    student@uso:~$ sudo su
    root@uso:/home/student#

O opțiune frecventă a comenzii ``su`` este ``-`` (semnul minus sau cratimă).
Această opțiune duce la crearea unui mediu de lucru specific unui utilizator care se autentifică (*login*).
Cel mai vizibil efect este schimbarea directorului curent în directorul home al utilizatorului către care dorim schimbarea.
De aceea, în comanda de mai jos, noul director este directorul home al utilizatorului privilegiat (``root``), adică ``/root/``:

.. code-block:: bash

    razvan@uso:~$ sudo su -
    root@uso:~# pwd
    /root

sudo, su și parole
^^^^^^^^^^^^^^^^^^

Se poate întâmpla ca în cazul folosirii ``sudo`` să fie solicitată o parolă.
Este vorba de parola utilizatorului curent, cel care rulează comanda ``sudo``.
Pentru siguranță, este nevoie de confirmarea parolei utilizatorului pentru a realiza acțiunea presupus critică prefixată de comanda ``sudo``.
Solicitarea sau nu a parolei utilizatorului curent la rularea comenzii ``sudo``, ține de configurarea acesteia, așa cum vom preciza în secțiunea TODO.

Sumarizând:

* Rularea comenzii ``su`` duce la solicitarea parolei contului de utilizator către care dorim schimbarea.
* Rularea comenzii ``sudo`` (urmată de altă comandă) **poate duce** (depinde de configurație) la solicitarea parolei contului utilizatorului curent.

Exerciții: Folosirea su
^^^^^^^^^^^^^^^^^^^^^^^

#. Obțineți un shell privilegiat.
   În shellul privilegiat, folosiți comanda ``su`` pentru a schimba utilizatorul în ``student``.
   Închideți shellul utilizatorului ``student``.
   Apoi închideți și shellul privilegiat.
   Ați revenit la punctul inițial.

#. Obțineți un shell privilegiat.
   În shellul privilegiat, folosiți comanda ``su`` pentru a schimba utilizatorul în ``student`` inclusiv mediul de login: directorul să fie ``/home/student/``.
   Închideți shellul utilizatorului ``student``.
   Apoi închideți și shellul privilegiat.
   Ați revenit la punctul inițial.

#. Obțineți un shell privilegiat.
   În shellul privilegiat, folosiți comanda ``su`` pentru a schimba utilizatorul în ``daemon``.
   Primiți eroare.

   Încercați să schimbați utilizatorul în ``bin``.
   La fel, primiți eroare.

   Aceste erori să întâmplă întrucât utilizatorii ``daemon`` și ``bin`` sunt utilizatori de sistem (*system users*) care nu sunt gândiți să fie utilizatori interactivi: adică se ne putem autentifica în sistem ca acei utilizatori și să rulăm procese shell (interactive).
   Vom discuta succint despre utilizatorii de sistem în secțiunea TODO.
