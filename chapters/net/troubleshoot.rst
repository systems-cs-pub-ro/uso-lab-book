Verificarea conectivităţii la reţea
===================================

Vom descompune fiecare nivel din stiva TCP/IP (implicit, nu le vom spune
efectiv ce face tot stiva) şi le vom arăta cum arată ea la nivelul sistemului
de operare, respectiv cum se verifică dacă funcţionează corespunzător nivelul
respectiv.

1) Interacţiunea cu nivelul fizic
---------------------------------

a. Investigarea nivelului fizic al rețelei
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Pentru primul nivel, nivelul fizic, le vom arăta, folosind poze, cum arată un
cablu de net, unde trebuie băgat, respectiv cum îţi dai seama că acel cablu
băgat are uplink.

b. Configurarea reţelei în mediul grafic
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Le vom arăta cum să se conecteze la o reţea folosind interfaţa vizuală a unui
Desktop Environment, probabil GNOME

c. Configurarea interfeţelor de reţea
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Le vom arăta output-ul comenzii `ip a s` şi le vom explica se înseamna fiecare
intrare de interfaţă şi ce înseamnă că o interfaţă este up.

Îi punem sa dea `ip link set up` şi să vadă ce se schimbă la output-ul lui `ip a
s` şi să vadă că acum le merge netul.

2) Configurarea nivelului Internet
----------------------------------

a. Configurarea unei adrese IP
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Le dăm o maşină care are interfaţa pornită, dar le arătăm ca nu are IP pe
interfaţă. Le arătăm comanda `dhclient <interfaţă>` pentru a obţine adresa IP şi
le arătăm că pot să dea ping la un calculator, dar nu se pot da ping la anumite
adrese IP.

b. Inspectarea rutelor din sistem
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Le explicăm ce înseamnă o reţea de calculatoare şi de ce nu le merge să iasă din
reţeaua lor, că nu este setat un default gateway. Îi punem să dea `traceroute`
înainte şi după ce adaugă o rută de mână (sau putem să îi punem sa dea iar
dhclient, dar pe o altă maşină pe care este configurat dhclient să dea gateway)
şi îi punem să dea a doua oară traceroute, ca să vadă că iese din reţea acum.

c. Configurarea gateway-ului
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Le explicăm ce înseamnă o reţea de calculatoare şi de ce nu le merge să iasă din
reţeaua lor, că nu este setat un default gateway. Îi punem să dea `traceroute`
înainte şi după ce adaugă o rută de mână (sau putem să îi punem sa dea iar
dhclient, dar pe o altă maşină pe care este configurat dhclient să dea gateway)
şi îi punem să dea a doua oară traceroute, ca să vadă că iese din reţea acum;

d. Verificarea conectivității la o altă stație
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Le vom arăta cum să folosească comanda `ping` pentru a verifica conexiunea cu
diverse stații.

Pentru a face troubleshooting facil este necesar să porniţi de la primul nivel
al stivei de reţea şi să verificaţi folosind comenzile de verificare de mai sus
(`ip address show`, `ip route show`, `traceroute`, `ping <adresă IP>`, `ping
<hostname>`) pentru a verifica funcţionalitatea fiecărui nivel.

d. Investigarea serviciului DNS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Le vom arăta cu o imagine cum funcţionează DNS-ul şi le vom arăta că poate fi
configurat temporar din /etc/resolv.conf, pentru a testa alte servere de DNS.

Le vom arăta cum se foloseşte comanda `dig`, pentru a verifica răspunsurile de
la diverse DNS-uri, gen Google şi CloudFlare.

3) Configurarea nivelului Transport
-----------------------------------

a. Conectivitatea între aplicații de rețea folosind porturi
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Le arătăm că fiecare aplicaţie care vrea să răspundă la cereri se foloseşte de
porturi. Pentru asta vom folosi `netcat` pentru a deschide un port, iar apoi
vom folosi `netstat` pentru a vedea ca a fost deschis portul.

b. Pornirea unei aplicaţii care folosește porturi
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Studenţii se vor conecta la portul deschis folosind `netcat`, şi vor scrie la
tastatura ceva pentru a apărea pe server.

c. Conectarea TCP la o aplicație
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Vom pune studenţii sa se conecteze la portul 80 al unui site (cum ar fi
elf.cs.pub.ro) şi să vadă ce apare la terminal. Astfel, le vom explica ca
server-ele deschid un port la care se conectează serviciile client.
