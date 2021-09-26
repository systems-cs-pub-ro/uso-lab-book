.. _data_proc_tasks:

Exerciții de prelucrare a datelor
=================================

Exercițiile de mai jos sunt aplicații practice ale noțiunilor și competențelor de prelucrare a datelor.
Fișierele de suport pentru exerciții se găsesc în directorul ``support/tasks/`` din directorul acestui capitol:

.. code-block:: bash

    student@uso:~$ cd uso-lab-book/chapters/data-proc/support/tasks/

    student@uso:~/.../data-proc/support/tasks$ ls -F
    01-exchange/  02-gradebook/  03-github/  04-bitcoin/  05-datahub/  06-testssl/  07-syscall/  08-vim/

.. _data_proc_tasks_01_exchange:

Tutorial: Analiza cursului valutar USD-EUR
------------------------------------------

Ne propunem să analizăm cursul valutar USD-EUR, prezentat la adresa https://data.humdata.org/dataset/ecb-fx-rates.

Lucrăm în subdirectorul ``01-exchange/``:

.. code-block:: bash

    student@uso:~/.../data-proc/support/tasks$ cd 01-exchange/

    student@uso:~/.../support/tasks/01-exchange$ ls -F
    process_exchange.py*

Pentru început, descărcăm fișierul CSV care cuprinde cursul valutar, folosind o comandă precum:

.. code-block:: bash

    student@uso:~/.../support/tasks/01-exchange$ wget https://proxy.hxlstandard.org/data/e6e27d/download/ECB_FX_USD-quote.csv
    [...]
    2021-08-28 12:11:38 (3.24 MB/s) - ‘ECB_FX_USD-quote.csv’ saved [3138594/3138594]

Fișierul ``ECB_FX_USD-quote.csv`` conține data și evaluarea valorii unui dolar (``1 USD``) pentru fiecare dintre celelalte monede.
Astfel, pentru data de ``2021-08-27``, valoarea ``0.8502678343678259`` de pe a doua coloană (EUR) înseamnă că ``1 USD`` valorează ``0.85... EUR``.

Ne dorim să aflăm următoarele informații:

#. Care a fost cea mai mică valoare a cursului (adică atunci când EUR a fost cel mai valoros față de dolar).
#. Care a fost cea mai mare valoare a cursului (adică atunci când EUR a fost cel mai valoros față de dolar).
#. Care a fost cea mai mare scădere a cursului între două zile consecutive.
#. Care a fost cea mai mare creștere a cursului între două zile consecutive.
#. Care a fost cel mai lung interval de scădere consecutivă a cursului.
#. Care a fost cel mai lung interval de creștere consecutivă a cursului.

Pentru primele două informații, putem folosi one-linere:

.. code-block:: bash

    student@uso:~/.../support/tasks/01-exchange$ < ECB_FX_USD-quote.csv tail -n +3 | cut -d ',' -f 1,2 | sort -t ',' -k 2n | head -1
    2008-07-15,0.6253908692933083
    student@uso:~/.../support/tasks/01-exchange$ < ECB_FX_USD-quote.csv tail -n +3 | cut -d ',' -f 1,2 | sort -t ',' -k 2rn | head -1
    2000-10-26,1.2118274357731458

Cea mai mică valoare a cursului este ``0.625...``, în data de ``2008-07-15``, iar cea mai mare valoare a cursului a fost ``1.211...`` în data de ``2000-10-26``.

În cazul celor două one-linere, am folosit comenzile următoare (cu rolul aferent):

* ``< ECB_FX_USD-quote.csv``: redirectează conținutul fișierului către comanda următoare
* ``tail -n +3``: afișează de la a 3-a linie, eliminând astfel antetul din tabelul din fișier
* ``cut -d ',' -f 1,2``: afișează doar primele două coloane: data și cursul USD-EUR
* ``sort -t ',' -k 2n``: sortează numeric după a doua coloană, folosind separatorul virgulă
* ``sort -t ',' -k 2nr``: sortează numeric inversat după a doua coloană, folosind separatorul virgulă
* ``head -1``: afișează prima intrare, adică ceea ce căutam

Pentru celalte informații, devine complicat să folosim one-linere sau shell.
Așa că vom folosi un script Python: ``process_exchange.py``.
În acest script Python vom integra aflarea tuturor informațiile, inclusiv cele două informații pe care le-am aflat cu one-linere.
Rulăm scriptul Python și aflăm toate informațiile:

.. code-block:: bash

    student@uso:~/.../support/tasks/01-exchange$ ./process_exchange.py
    Highest exchange rate: 1.2118274357731458 (on 2000-10-26)
    Lowest exchange rate: 0.6253908692933083 (on 2008-07-15)
    Largest increase of exchange rate: 0.033178396113141106 (on 2008-12-19)
    Largest decrease of exchange rate: -0.04829874914157539 (on 2000-09-22)
    Largest period of exchange rage increase: 10 days starting from 2015-02-25
    Largest period of exchange rage decrease: 10 days starting from 2006-11-21

Prezentăm câteva secvențe din scriptul ``process_exchange.py``:

* Variabila globală ``data`` reține datele citite într-o listă de perechi de forma ``(date, value)``.
  Variabila globală ``diff_data`` reține diferențele între valorile dintre date / zile consecutive într-o listă de perechi de forma ``(data, diff``).

  .. code-block:: python

      # Data is read in list of tuples (pairs), i.e. (2020-02-21, 0.73).
      # Date is the first item of the tuple / pair.
      # Exchange rate is the next item in the tuple / pair.
      data = []

      # Store differential values in list of tuples (pairs), i.e. (2020-02-21, 0.012).
      # This means that on 2020-02-21 there was an increase of 0.012 of the exchange rate
      # compared to the previous day (2020-02-20).
      diff_data = []

* Funcțiile de afișare sortează o listă de perechi după valoare:

  .. code-block:: python

      sorted_data = list(sorted(data, key=lambda x: x[1]))
      [..]
      sorted_data = list(sorted(diff_data, key=lambda x: x[1]))

* Datele sunt citite din fișierul CSV (folosind pachetul CSV din Python [#python_csv]_) în variabila ``data``:

  .. code-block:: python

      with open(FILENAME, 'rt') as csvfile:
          reader = csv.reader(csvfile)
          # Read header.
          header = next(reader)
          date_idx = header.index('Date')
          currency_idx = header.index(CURRENCY)
          # Skip comment line.
          next(reader)
          # Read contents.
          for row in reader:
              data.append((row[date_idx], float(row[currency_idx])))

* Diferențele sunt calculate în variabila ``diff_data``:

  .. code-block:: python

      # Compute differential data.
      for i in range(0, len(data)-1):
          cur_date = data[i][0]
          cur_value = data[i][1]
          prev_value = data[i+1][1]
          diff_data.append((cur_date, cur_value - prev_value))

.. _data_proc_tasks_02_register:

Prelucrări în catalog
---------------------

Ne interesează prelucrarea datelor din cataloage de note.
Cataloagele sunt în format ``.xlsx``.
Veți realiza prelucrare interactivă în LibreOffice sau Google Spreadsheets.
Și veți realiza o prelucrare neinteractivă (scriptată), care să realizeze automat prelucrarea pe mai multe fișiere.

Lucrați în subdirectorul ``02-gradebook/``.
Directorul conține patru fișiere ``.xlsx`` reprezentând cataloagele din patru ani universitari diferiți:

.. code-block:: bash

    student@uso:~/.../data-proc/support/tasks$ cd 02-gradebook/

    student@uso:~/.../support/tasks/02-gradebook$ ls -F
     process_gradebook.py*   process_gradebook.sh*  'SO 2014-2015 - Catalog.xlsx'  'SO 2015-2016 - Catalog.xlsx'  'SO 2016-2017 - Catalog.xlsx'  'SO 2017-2018 - Catalog.xlsx'

Realizați, în LibreOffice sau, online, în Google Spreadsheets, următoarele prelucrări (în mod interactiv) pe fișierul ``SO 2014-2015 - Catalog.xlsx``:

#. Sortați notele, descrescător, în funcție de coloana ``Punctaj final``.

#. Obțineți media notelor pentru mai multe coloane:

   * coloana ``Notă finală``
   * coloana ``Punctaj final``
   * coloana ``Notă curs``
   * coloana ``Examen final``
   * coloana ``Notă lucrări``
   * coloana ``Notă teme``

#. Calculați câte note finale (coloana ``Notă finală``) sunt ``10``, câte note sunt ``4`` și câte sunt fără notă.

Realizați aceleași prelucrări ca mai sus automat, folosind scripting.
Pentru aceasta va trebui să convertiți fișierele din format ``.xlsx`` în format ``.csv``.
Realizați acest lucru cu o comandă de forma:

.. code-block:: bash

    student@uso:~/.../support/tasks/02-gradebook$ libreoffice --headless --convert-to csv SO\ 2014-2015\ -\ Catalog.xlsx
    student@uso:~/.../support/tasks/02-gradebook$ ls
    student@uso:~/.../support/tasks/02-gradebook$ ls -F
     process_gradebook.py*  'SO 2014-2015 - Catalog.csv'   'SO 2015-2016 - Catalog.xlsx'  'SO 2017-2018 - Catalog.xlsx'
     process_gradebook.sh*  'SO 2014-2015 - Catalog.xlsx'  'SO 2016-2017 - Catalog.xlsx'

În urma comenzii de conversie se generează un fișier CSV (în cazul acesta ``SO 2014-2015 - Catalog.csv``.
Fișierul format CSV trebuie curățat: trebuie șterse primele linii (capul de tabel) și ultimele linii (informații vide).

Porniți, la alegere, de la scheletul de script Bash ``process_gradebook.sh`` sau de la scheletul de script Python ``process_gradebook.py``.
Urmăriți comentariile marcate cu ``TODO`` în cadrul scheletelor de script.

La o rezolvare corectă, rezultatul rulării scriptului va fi:

.. code-block:: bash

    student@uso:~/.../support/tasks/02-gradebook$ ./process_gradebook.py SO\ 2014-2015\ -\ Catalog.csv | tail -8
    Average (Notă finală): 6.82
    Average (Punctaj final): 6.02
    Average (Notă curs): 5.11
    Average (Examen final): 5.34
    Average (Notă lucrări): 5.84
    Average (Notă teme): 5.30
    Number of items (Notă finală) with value of 10: 17
    Number of items (Notă finală) with value of 4 or nothing: 23
    student@uso:~/.../support/tasks/02-gradebook$ ./process_gradebook.py SO\ 2015-2016\ -\ Catalog.csv | tail -8
    Average (Notă finală): 7.04
    Average (Punctaj final): 6.07
    Average (Notă curs): 5.15
    Average (Examen final): 5.75
    Average (Notă lucrări): 5.77
    Average (Notă teme): 5.41
    Number of items (Notă finală) with value of 10: 23
    Number of items (Notă finală) with value of 4 or nothing: 32
    student@uso:~/.../support/tasks/02-gradebook$ ./process_gradebook.py SO\ 2016-2017\ -\ Catalog.csv | tail -8
    Average (Notă finală): 6.36
    Average (Punctaj final): 5.83
    Average (Notă curs): 4.88
    Average (Examen final): 4.86
    Average (Notă lucrări): 5.45
    Average (Notă teme): 5.03
    Number of items (Notă finală) with value of 10: 14
    Number of items (Notă finală) with value of 4 or nothing: 24
    student@uso:~/.../support/tasks/02-gradebook$ ./process_gradebook.py SO\ 2017-2018\ -\ Catalog.csv | tail -8
    Average (Notă finală): 6.94
    Average (Punctaj final): 6.30
    Average (Notă curs): 5.56
    Average (Examen final): 6.14
    Average (Notă lucrări): 5.32
    Average (Notă teme): 6.51
    Number of items (Notă finală) with value of 10: 21
    Number of items (Notă finală) with value of 4 or nothing: 25

.. _data_proc_tasks_03_github:

GitHub Ranking
--------------

Ne interesează să analizăm cele mai urmărite repository-uri de pe GitHub, disponibile în `repository-ul GitHub-Ranking`_.

Lucrați în subdirectorul ``03-github/``:

.. code-block:: bash

    student@uso:~/.../data-proc/support/tasks$ cd 03-github/

    student@uso:~/.../support/tasks/03-github$ ls -F
    top10lang.py*  top10lang.sh*

Descărcați un fișier CSV din din `repository-ul GitHub-Ranking`_.
Dați click pe fișier și apoi pe butonul ``Raw`` ca să obțineți varianta primară a fișierului.
URL-ul corect începe cu ``https://raw.github.com/...``.

Odată fișierul descărcat, obțineți top 10 repository-uri pentru un limbaj de programare primit ca argument în linia de comandă.
Porniți, la alegere, de la scheletul de script Bash ``top10lang.sh`` sau de la scheletul de script Python ``top10lang.py``.
Urmăriți comentariile marcate cu ``TODO`` în cadrul scheletelor de script.

La o rezolvare corectă, rezultatul rulării scriptului va fi:

.. code-block:: bash

    student@uso:~/.../support/tasks/03-github$ ./top10lang.sh github-ranking-2021-08-24.csv C
    1,C,linux,116734,38510,C,https://github.com/torvalds/linux,torvalds,0,2021-08-23T17:02:25Z,Linux kernel source tree
    2,C,netdata,55684,5004,C,https://github.com/netdata/netdata,netdata,232,2021-08-24T00:33:27Z,"Real-time performance monitoring, done right! https://www.netdata.cloud"
    3,C,scrcpy,53385,5538,C,https://github.com/Genymobile/scrcpy,Genymobile,826,2021-08-17T14:12:23Z,Display and control your Android device
    4,C,redis,50696,19868,C,https://github.com/redis/redis,redis,1598,2021-08-23T18:01:08Z,"Redis is an in-memory database that persists on disk. The data model is key-value, but many different kind of values are supported: Strings, Lists, Sets, Sorted Sets, Hashes, Streams, HyperLogLogs, Bitmaps."
    5,C,git,39062,22056,C,https://github.com/git/git,git,0,2021-08-23T21:38:30Z,Git Source Code Mirror - This is a publish-only repository and all pull requests are ignored. Please follow Documentation/SubmittingPatches procedure for any of your improvements.
    6,C,php-src,31178,6791,C,https://github.com/php/php-src,php,0,2021-08-23T21:20:41Z,The PHP Interpreter
    7,C,obs-studio,30412,5107,C,https://github.com/obsproject/obs-studio,obsproject,411,2021-08-24T02:08:36Z,OBS Studio - Free and open source software for live streaming and screen recording
    8,C,wrk,29970,2467,C,https://github.com/wg/wrk,wg,100,2021-07-28T11:06:07Z,Modern HTTP benchmarking tool
    9,C,ijkplayer,29289,7602,C,https://github.com/bilibili/ijkplayer,bilibili,2607,2021-07-23T16:15:29Z,"Android/iOS video player based on FFmpeg n3.4, with MediaCodec, VideoToolbox support."
    10,C,FFmpeg,25866,8621,C,https://github.com/FFmpeg/FFmpeg,FFmpeg,0,2021-08-23T23:15:23Z,Mirror of https://git.ffmpeg.org/ffmpeg.git

    student@uso:~/.../support/tasks/03-github$ ./top10lang.sh github-ranking-2021-08-24.csv Python
    1,Python,public-apis,152482,17285,Python,https://github.com/public-apis/public-apis,public-apis,5,2021-08-23T19:18:24Z,A collective list of free APIs
    2,Python,system-design-primer,141941,26142,Python,https://github.com/donnemartin/system-design-primer,donnemartin,118,2021-08-23T22:32:48Z,Learn how to design large-scale systems. Prep for the system design interview.  Includes Anki flashcards.
    3,Python,Python,114883,31176,Python,https://github.com/TheAlgorithms/Python,TheAlgorithms,6,2021-08-24T02:20:08Z,All Algorithms implemented in Python
    4,Python,Python-100-Days,107367,42475,Python,https://github.com/jackfrued/Python-100-Days,jackfrued,422,2021-08-12T02:21:24Z,Python - 100天从新手到大师
    5,Python,awesome-python,101958,19714,Python,https://github.com/vinta/awesome-python,vinta,4,2021-08-04T14:18:43Z,"A curated list of awesome Python frameworks, libraries, software and resources"
    6,Python,youtube-dl,99205,5752,Python,https://github.com/ytdl-org/youtube-dl,ytdl-org,3736,2021-08-23T17:02:29Z,Command-line program to download videos from YouTube.com and other video sites
    7,Python,models,70998,44682,Python,https://github.com/tensorflow/models,tensorflow,1060,2021-08-23T23:05:45Z,Models and examples built with TensorFlow
    8,Python,thefuck,63633,2963,Python,https://github.com/nvbn/thefuck,nvbn,174,2021-08-17T13:41:54Z,Magnificent app which corrects your previous console command.
    9,Python,flask,56392,14549,Python,https://github.com/pallets/flask,pallets,17,2021-08-15T09:21:19Z,The Python micro framework for building web applications.
    10,Python,keras,52199,18796,Python,https://github.com/keras-team/keras,keras-team,371,2021-08-24T01:51:56Z,Deep Learning for humans

.. _`repository-ul GitHub-Ranking`: https://github.com/EvanLi/Github-Ranking/tree/master/Data

.. _data_proc_tasks_04_bitcoin:

Istoric Bitcoin
---------------

Ne interesează să analizăm istoricul Bitcoin disponibil pe `Token Database`_.

Lucrați în subdirectorul ``04-bicoin/``.
În acest subdirector există descărcat în prealabil un fișier CSV (`btc-assets-vwap5.csv`) de la `Token Database`_.

.. code-block:: bash

    student@uso:~/.../data-proc/support/tasks$ cd 04-bitcoin/

    student@uso:~/.../support/tasks/03-github$ ls -F
    btc-assets-vwap5.csv

La fel ca în cazul :ref:`data_proc_tasks_01_exchange`, ne dorim să aflăm următoarele informații:

#. Care a fost cea mai mică valoare a deschiderii (*open*).
#. Care a fost cea mai mare valoare a deschiderii.
#. Care a fost cea mai mare scădere a deschiderii între două zile consecutive.
#. Care a fost cea mai mare creștere a deschiderii între două zile consecutive.
#. Care a fost cel mai lung interval de scădere consecutivă a deschiderii.
#. Care a fost cel mai lung interval de creștere consecutivă a deschiderii.

Creați a copie a scriptului ``../01-exchange/process_exchange.py`` și actualizați-o pentru cerințele curente.

La o rezolvare corectă, rezultatul rulării scriptului va fi:

.. code-block:: bash

    $ python process_bitcoin.py
    Highest exchange rate: 63375.2371077903 (on 2021-04-14T00:00:00)
    Lowest exchange rate: 3389.01136388369 (on 2019-02-08T00:00:00)
    Largest increase of exchange rate: 7661.562806823698 (on 2021-02-09T00:00:00)
    Largest decrease of exchange rate: -6257.173214731105 (on 2021-05-13T00:00:00)
    Largest period of Bitcoin opening increase: 9 days starting from 2020-12-11T00:00:00
    Largest period of Bitcoin opening decrease: 7 days starting from 2019-11-03T00:00:00

Bonus: Graficul evoluției
^^^^^^^^^^^^^^^^^^^^^^^^^

Realizați un grafic al evoluției deschiderii pentru Bitcoin.
Puteți folosi Matplotlib [#matplotlib]_.
Vedeți `tutorialul de la Moonbooks`_ sau `tutorialul Pyplot de la Matplotlib`_

.. _`Token Database`: https://tokendatabase.com/
.. _`tutorialul de la Moonbooks`: https://moonbooks.org/Articles/How-to-create-a-simple-scatter-plot-using-matplotlib-/
.. _`tutorialul Pyplot de la Matplotlib`: https://matplotlib.org/stable/tutorials/introductory/pyplot.html#sphx-glr-tutorials-introductory-pyplot-py

.. _data_proc_tasks_05_github:

datahub.io
----------

Folosiți-vă de cunoștințele de până acum și alegeți un set de date care vă interesează și realizați prelucrări cu acest set.
Accesați `datahub.io`_ și căutați un set de informații de interes.
Aveți de ales din informații demografice, sportive, economice, geografice etc.

Lucrați în subdirectorul ``05-datahub/``:

.. code-block:: bash

    student@uso:~/.../data-proc/support/tasks$ cd 05-datahub/
    student@uso:~/.../support/tasks/05-datahub$

.. _`datahub.io`: https://datahub.io/

.. _data_proc_tasks_06_testssl:

testssl.sh
----------

`testssl.sh`_ este un utilitar care investighează configurația TLS/SSL a unui server.
În urma unei investigații, utilitarul creează un fișier de jurnalizare în format JSON.

Lucrați în subdirectorul ``06-testssl/``.
În acest subdirector se găsesc patru fișiere JSON obținute în urma investigației cu ``testssl.sh`` și un schelet de script Python pentru prelucrarea acestora:

.. code-block:: bash

    student@uso:~/.../data-proc/support/tasks$ cd 06-testssl/

    student@uso:~/.../support/tasks/06-testssl$ ls -F
    balarama.lt.json  mage2.pro.json  process_testssl.py*  www.click2sell.eu.json  www.llri.lt.json

Realizați modificări în scheletul de script ``process_testssl.py`` astfel încât:

#. Să afișați și evaluarea de ansamblu (``overall_grade``) din fișierele JSON.

#. Să afișați vulnerabilitățile serverului, adică acele intrări de tipul vulnerabilitate pentru care câmpul ``severity`` **NU** are valoarea ``OK``.

Urmăriți comentariile marcate cu ``TODO`` în cadrul scheletului de script.

La o rezolvare corectă, rezultatul rulării scriptului va fi:

.. code-block:: bash

    student@uso:~/.../support/tasks/06-testssl$ ./process_testssl.py balarama.lt.json
    final_score: 94, overall_grade: B

    Vulnerabilities:

    BREACH (CVE-2013-3587) - MEDIUM
    DROWN_hint (CVE-2016-0800 CVE-2016-0703) - INFO
    LOGJAM-common_primes (CVE-2015-4000) - INFO
    BEAST_CBC_TLS1 (CVE-2011-3389) - MEDIUM
    BEAST (CVE-2011-3389) - LOW
    LUCKY13 (CVE-2013-0169) - LOW
    student@uso:~/.../support/tasks/06-testssl$ ./process_testssl.py mage2.pro.json
    final_score: 91, overall_grade: B

    Vulnerabilities:

    BREACH (CVE-2013-3587) - MEDIUM
    DROWN_hint (CVE-2016-0800 CVE-2016-0703) - INFO
    BEAST_CBC_TLS1 (CVE-2011-3389) - MEDIUM
    BEAST (CVE-2011-3389) - LOW
    LUCKY13 (CVE-2013-0169) - LOW
    student@uso:~/.../support/tasks/06-testssl$ ./process_testssl.py www.click2sell.eu.json
    final_score: 92, overall_grade: B

    Vulnerabilities:

    BREACH (CVE-2013-3587) - MEDIUM
    DROWN_hint (CVE-2016-0800 CVE-2016-0703) - INFO
    LUCKY13 (CVE-2013-0169) - LOW
    student@uso:~/.../support/tasks/06-testssl$ ./process_testssl.py www.llri.lt.json
    final_score: 91, overall_grade: B

    Vulnerabilities:

    BREACH (CVE-2013-3587) - MEDIUM
    DROWN_hint (CVE-2016-0800 CVE-2016-0703) - INFO
    LOGJAM-common_primes (CVE-2015-4000) - INFO
    BEAST_CBC_TLS1 (CVE-2011-3389) - MEDIUM
    BEAST (CVE-2011-3389) - LOW
    LUCKY13 (CVE-2013-0169) - LOW

.. _data_proc_tasks_07_syscall:

Apeluri de sistem
-----------------

Avem colectate două fișiere în fomat CSV cu informații legate de apeluri de sistem (din cadrul proiectului `Unikraft`_).
Lucrați în subdirectorul ``07-syscall/``:

.. code-block:: bash

    student@uso:~/.../data-proc/support/tasks$ cd 07-syscall/

    student@uso:~/.../support/tasks/07-syscall$ ls -F
    process_syscalls.py*  process_syscalls.sh*  syscall-status.csv  syscall-use.csv

Fișierul ``syscall-use.csv`` conține două coloane:

#. ``syscall``: numele apelului de sistem
#. ``num_apps``: numărul de aplicații care folosesc acel apel de sistem (maxim 30)

Fișierul ``syscall-status.csv`` conține informații despre implementarea curentă a apelurilor de sistem în trei coloane:

#. ``syscall_id``: identificatorul apelului de sistem
#. ``syscall_name``: numele apelului de sistem
#. ``status``: starea implementării apelului de sistem

Realizați o asociere între cele două fișiere astfel încât să obțineți, unificat, o afișare de tip CSV care să conțină coloanele ``syscall_id``, ``syscall_name``, ``status`` și ``num_apps``.

Apoi din acea afișare, să afișați, în ordinea numărului de aplicații care folosesc acel apel de sistem (de la cele mai multe la cele mai puține), acele apeluri de sistem a căror stare **NU** este ``okay``.

Scriptul Bash ``process_syscalls.sh`` conține deja rezolvarea.
Este ineficient, apelând ``grep`` (adică ducând la crearea unui proces nou) de mai multe ori.
Acest lucru arată limitările folosirii Bash pentru prelucrării mai complexe.

O rezolvare mai eficientă, mai extensibilă și mai ușor de înțeles se poate realiza în Python.
Porniți sau de la scheletul de script Python ``process_syscalls.py`` și rezolvați cerințele.
Urmăriți comentariile marcate cu ``TODO`` în cadrul scheletului de script.

La o rezolvare corectă, rezultatul rulării scriptului va fi:

.. code-block:: bash

    student@uso:~/.../support/tasks/07-syscall$ ./process_syscalls.py
    [...]
    158,arch_prctl,broken,30
    12,brk,incomplete/restricted,30
    59,execve,registration missing,30
    13,rt_sigaction,incomplete/restricted,29
    257,openat,registration missing,29
    60,exit,incomplete/restricted,28
    72,fcntl,registration missing,28
    14,rt_sigprocmask,incomplete/restricted,27
    231,exit_group,incomplete/restricted,26
    218,set_tid_address,,25

.. _Unikraft: https://www.unikraft.org/

.. _data_proc_tasks_08_vim:

Bonus: Prelucrare interactivă în Vim
------------------------------------

Vim oferă suport în automatizarea (interactivă) folosind macro-uri pentru înregistrarea acțiunilor (*recording*) [#vimrecord]_.
Această funcționalitate este prezentată în tutorialul `Vi and Vim Macro Tutorial`_.

Lucrați în subdirectorul ``08-vim/``:

.. code-block:: bash

    student@uso:~/.../data-proc/support/tasks$ cd 08-vim/
    student@uso:~/.../support/tasks/08-vim$ ls
    contact.reference.csv  email.reference.txt  names.txt

Realizați o copie a fișierului ``names.txt`` numită ``contact.csv``.
Folosiți funcționalitatea Vim de *recording* pentru a edita fișierul ``contact.csv`` pentru a ajunge la conținutul fișierului ``contact.reference.csv``.

Realizați o copie a fișierului ``contact.csv`` numită ``email.txt``.
Folosiți funcționalitatea Vim de *recording* pentru a edita fișierul ``email.txt`` pentru a ajunge la conținutul fișierului ``email.reference.txt``.

.. hint::

    Folosiți-vă de următoarele comenzi în Vim:

    * ``dd``: decupează (*cut*) linia curentă
    * ``p``: lipește (*paste*) textul decupat
    * ``qa``: se pornește înregistrarea în macro-ul ``a``
    * ``q``: se oprește înregistrarea macro-ului curent
    * ``@a``: executarea înregistrării din macro-ul ``a``
    * ``0``: plasare la începutul liniei
    * ``$``: plasare la sfârșitul liniei
    * ``f<character>``: deplasează până la prima apariție ulterioară a caracterului ``<character>`` (cursorul este plasat pe caracter)
    * ``F<character>``: deplasează înapoi până la prima apariție anterioară a caracterului ``<character>`` (cursorul este plasat pe caracter)
    * ``df<character>``: decupează (*cut*) până la prima apariție ulterioară a caracterului ``<character>`` (cursorul este plasat pe caracter)
    * ``d<position>``: în general, decupează până la o construcție de tip poziție
    * ``h``, ``j``, ``k``, ``l``: deplasare un caracter la stânga, o linie jos, o linie sus, un caracter la dreapta
    * ``i``: trecere în modul inserare din modul ecran, cursorul este sub caracterul curent
    * ``a``: trecere în modul inserare din modul ecran, cursorul este sub următorul caracter
    * ``A``: trecere în modul inserare din modul ecran, cursorul este la sfârșitul liniei
    * ``ESC``: trecere în modul ecran din modul inserare
    * ``x``: ștergerea caracterului de sub cursor (în modul ecran)
    * ``J``: alăturarea (*join*) liniei următoare la linia curentă
    * ``gu$``: transformă majusculele în minuscule până la sfârșitul liniei
    * ``gu<position>``: în general, transformă majusculele în minuscule până la o construcție de tip poziție

.. _`Vi and Vim Macro Tutorial`: https://www.thegeekstuff.com/2009/01/vi-and-vim-macro-tutorial-how-to-record-and-play/

.. rubric:: Note de subsol

.. [#python_csv]

    https://docs.python.org/3/library/csv.html

.. [#matplotlib]

    https://matplotlib.org/stable/index.html

.. [#vimrecord]

    http://vimdoc.sourceforge.net/htmldoc/repeat.html#recording
