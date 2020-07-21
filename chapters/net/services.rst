Servicii şi clienţi de reţea
============================

1) Clienţi web în linia de comandă
-----------------------------------

Pentru accesarea unui site le arătăm că putem să descărca site-ul folosind un
client cum ar fi `wget`, sau `curl` şi le arătăm că se descarcă un fişier HTML
şi le vom explica că asta face şi browser-ul, dar are un motor care
interpretează textul şi îl afişează.

2) Accesul la distanţă în linie de comandă
------------------------------------------

Pentru accesarea unui calculator de la distanţă prin shell, le arătăm cum se pot
conecta la un alt calculator şi să ruleze pe el comenzi folosind SSH.

Aici le vom arăta că există două moduri de autentificare, folosind parolă şi
folosind chei.

a. Conectarea folosind autentificare cu parolă
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

b. Conectarea folosind autentificare cu chei
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

b'. Generarea unei perechi de chei
""""""""""""""""""""""""""""""""""

Îi punem să îşi genereze cheia şi să o copieze pe o altă staţie, apoi să vadă că
nu mai trebuie tastată parola.

c. Conectarea între două calculatoare aflate în rețele private diferite
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

<TODO: de adăugat diagramă>

Pentru a demonstra principiul tunelării, ne vom folosi iar de netcat pentru a
realiza o conexiune între două staţii. Ei se vor conecta la localhost:2222 şi
vor accesa o altă maşină virtuală remote. Le vom arăta cum se face tunelul.

d. Transferul datelor la distanţă
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Pentru a transfera fişiere la distanţă îi punem să folosească `scp` pentru a
trimite un director şi un fişier către o staţie remote, iar apoi îi pune, să
copieze şi invers, de pe staţia remote pe local.

3) Controlul la distanță în mediul grafic
-----------------------------------------

Pentru controlul la distanţă în mod vizual le vom da doua exemple.

a. Controlul unei ferestre la distanţă
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Control folosind GUI host-at remote vor porni un browser pe o staţie remote. Le
vom arăta de X forwarding.

b. Controlul desktopului la distanţă
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Pentru control complet al sesiunii le vom arăta să folosească TeamViewer.

4) Securizarea conexiunii la Internet folosind un VPN
-----------------------------------------------------

Pentru demonstrarea funcționalității de VPN le vom da 3 maşini virtuale, două
care nu se pot conecta între ele şi una care să fie un server de VPN şi le vom
arăta cum să se conecteze la VPN şi să observe că a apărut o nouă interfaţă şi
să încerce să dea ping între maşini şi să vadă că funcţionează acum. Aici putem
sa le dăm şi exemplu cu Hamachi.

Aici vom puncta şi faptul că tunelul în loc sa fie folosit ca o reţea privată
între mai multe calculatoare, poate fi folosit pentru a ieşi prin altă cale în
internet. Putem face asta cu “What’s my IP”, sau un serviciu similar. Este de
cugetat aici la nivel de infrastructură cum am putea face asta.
