.. _cli_automation_intro:

Perspective pentru automatizare
===============================

În acest capitol vom folosi comenzi și noțiuni prezentate în capitolele de până acum, în special :ref:`improve_cli`.
Vor fi puține comenzi nou introduse; cel mai mult ne va interesa cum, dându-se o situație practică, vom putea folosi shell-ul pentru automatizare.

**Automatizarea sarcinilor** se referă la delegarea / degrevarea acțiunilor utilizatorilor către programe în sistemul de calcul.
Un program va face automat, de sine stătător, acțiuni pe care le-ar face utilizatorul, rezultând în timp mai puțin consumat de utilizator.

Acțiunile care sunt candidate pentru automatizare sunt în general acțiuni repetitive, nu foarte simple și neinteractive.
Automatizarea acestora va elibera utilizatorul de la executarea repetată, plictisitoare, manuală a acestora.

Automatizarea sarcinilor urmărește eficiența, în special temporală.
Cu cât face mai rapid acțiuni repetitive, cu atât este mai bine.
Acțiunile repetitive necesită interacțiune minimă cu utilizatorul, pentru a eficientiza timpul.

Când automatizăm, folosim scripting și folosim funcționalități existente.
Un principiu esențial al automatizării este *don't repeat yourself* (**DRY** - nu reinventăm roata).
Dacă există comenzi sau funcționalități existente, le folosim pe acelea.
Altfel spus, urmărim atât eficiența execuției cât și eficiența dezvoltării.

Eficiența execuției o putem realiza nu doar prin scripting ci și prin acțiuni precum:

* folosirea de scurtături de taste
* folosirea funcționalităților de tipul command completion sau history search
* folosirea de alias-uri de comenzi
* folosirea de șabloane pentru căutare de text: globbing sau expresii regulate (regular expressions)
* folosirea de șabloane pentru generare de text: scrierea emailurilor sau scrierea codului (code snippets)