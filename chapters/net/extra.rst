Funcţionalităţi suplimentare de reţelistică
===========================================

Aceste exerciţii sunt menite să abordeze lucruri care nu sunt neapărat necesare
pentru utilizarea şi înţelegerea conceptelor din acest capitol, dar oferă bune
practici şi cunoştinţe extra despre conectarea calculatorului la internet şi
funcţionarea serviciilor în internet.

1) Folosirea proxy-urilor HTTP
------------------------------

Proxy-ul HTTP este o alternativă a VPN care în loc să îţi tuneleze tot traficul
în internet, o va face doar pentru traficul HTTP. Putem să folosim un serviciu
online de proxying, ca sa nu ne ia cu capul când facem infrastructura.

2) Evitarea elementelor de tip paywall
--------------------------------------

a. Ştergerea elementelor din pagina web
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Îi putem pune să se conecteze pe un site cu paywall şi să le arătăm cum să
scoată paywallul folosind inspect element şi să şteargă elementul din pagină ca
să vadă conţinutul. Aici putem folosi un site care oferă cărţi.

b. Instalarea add-on-urilor de tip paywall bypass
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Le arătăm că pot să îşi instaleze pluginuri ca să şteargă paywalluri de la
site-uri cum ar fi cele de research, sau ştiri.

3) Configurarea avansată pentru SSH
-----------------------------------

a. Configurarea scurtăturilor SSH
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Le vom arăta cum să facă “scurtături” pentru conectarea şi configurarea
conexiunilor SSH la anumite host-uri folosind fişierul de configurare pentru
SSH.

b. Configurarea accesului prin chei SSH
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Pentru conectarea remote la calculatoare fără parolă, le putem arăta ca
alternativa la ssh-copy-id cum să adauge “de mână” cheia SSH în fişierul
authorized_keys.

4) Gestiunea avansată a conexiunilor la rețea
---------------------------------------------

a. Configurarea conexiunilor folosind `nmcli`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Aici propun să le arătăm cum să se conecteze la reţele folosind `nmcli` şi să le
arătăm cum pot să vadă într-un singur loc toate conexiunile pe care le are un
calculator şi cum sa le configureze. Aici putem să le arătăm cum să schimbe
DNS-ul;

b. Conectarea la reţelele wireless
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Dacă avem infrastructura, mi se pare că ar fi foarte fain dacă le-am arăta cum
să se conecteze la un wifi folosind `nmcli`.
