##################################################
Legarea executabilelor folosind biblioteci externe
##################################################

*************************
1) Inspectarea fișierelor
*************************

Analiză statică pe codul sursă dat. Trebuie să observe ce headere sunt 
incluse în fișiere pentru a înțelege mai încolo de ce este nevoie de 
legarea la o bibliotecă externă.

*************************
2) Compilarea fișierelor
*************************

Aici vor avea nevoie să compileze cu -l<lib> pentru a funcționa.
Și cu -L <path-to-lib> pentru a-i spune path-ul unde să caute <lib>.

a. Instalarea bibliotecii necesare pentru compilarea codului
============================================================

Lipsește una dintre bibliotecile necesare, trebuie instalată.

b. Compilarea codului sursă
===========================

Compilarea propriu-zisă.

*********************************
3) Verificare biblioteci folosite
*********************************

Se găsesc toate bibliotecile la care este legat executabilul generat anterior.
