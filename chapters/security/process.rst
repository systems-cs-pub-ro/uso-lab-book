Securitatea proceselor - Izolare
================================

O formă extinsă de izolare este folosirea **containerelor** sau **mașinilor virtuale**.
*Containerele* oferă reguli complexe de izolare a unei aplicații sau a unui set de aplicații.
*Mașinile virtuale* adaugă, față de containere, partiționarea resurselor hardware și izolarea inclusiv a sistemului de operare al mașinii virtuale; în cazul unui sistem de operare compromis, doar mașina virtuală respectivă va fi afectată.
Diferențele între container și mașini virtuale sunt prezentate în figura de mai jos.
Mai multe noțiuni teoretice despre mașini virtuale și containere puteți citi aici (TODO: carte USO)

.. figure:: res/container_vs_VM.png


Containere
----------

Tehnologii ce implementează mecanismul de container în sistemele Linux sunt:
* LXC (Linux Containers) - oferă posibilitatea rulării unor servicii intr-un mediu izolat de sistemul de bază.
* OpenVZ - similar LXC, dar nu este prezent în mod implicit în nucleul Linux.
* Docker - oferă posibilitatea rulării într-un container doar a unei singure aplicații.



Mașina virtuală
---------------

În continuare vom folosi următoarea nomenclatura:
• *sistem gazdă* sau *host* sau *mașină fizică*: cel care a fost instalat prima dată și deasupra căruia rulăm un alt sistem de operare.
• *sistem oaspete* sau *guest* sau *mașină virtuală*: sistem de operare ce îl rulăm în cadrul sistemului gazdă.

În acest capitol de laborator prezentăm două soluții de virtualizarE:
* *Virtual Box* - se instalează pe majoritatea sistemelor de operare (Windows, Linux sau MacOS). Poate rula orice sistem de operare gazdă, are opțiuni de snapshot (salvarea stării unei mașini virtuale), posibilități avansate de a controla configurațiile de rețea. Poate fi folosit în mod gratuit.
* *VMware Workstation/Player/Fusion* - se instalează pe sistemele Windows și Linux și oferă aceleași facilități ca și VirtualBox. VMware Fusion se adresează sistemelor de operare gazdă MacOS oferind aceleași funcționalități ca VMware Workstation. Ambele versiuni necesită achiziționarea unei licențe. Cu ajutorul versiunii VMware Player se pot rula mașinile virtuale create cu VMware Workstation, dar aceasta nu deține facilități avansate (ex. snapshot). VMware Player este distribuit gratuit.


În continuare vom detalia pașii pentru pornirea unei mașini virtuale.
Pentru rularea mașinii virtuale, trebuie să importați fișierul OVA în VirtualBox accesând *File* apoi *Import Appliance*, ca în imaginea de mai jos:

.. figure:: import-appliance.png

Va apărea opțiunea de a selecta calea către fișierul OVA.
Acest fișier conține mașina virtuală.

.. figure:: import_appliance_ova_vbox.png

Apoi va începe importul şi va arăta ca mai jos:

.. figure:: screenshot_from_2018-09-27_23-15-10.png

După finalizarea importului, asigurați-vă că creați un host network: File -> Host Network Manager -> Create:

.. figure:: screenshot_from_2019-11-29_16-50-52.png

Porniți mașina virtuală și autentificați-vă.

