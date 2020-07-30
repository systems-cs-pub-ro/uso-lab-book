Rularea aplicațiilor
====================

Aplicații și procese
--------------------

**breviar**: când o aplicație pornește se creează un proces

**breviar**: un proces folosește resursele sistemului

**tutorial**: putem vedea procesele cu ps

**tutorial**: toate procesele cu ps -e

**breviar**: un proces este creat de un alt proces, avem o ierarhie de procese; un proces are un proces părinte; un proces poate avea mai multe procese copil

**tutorial**: informații complete cu ps -e -f

**breviar**: în vârful ierarhiei este procesul init

**tutorial**: putem vedea ierarhia de procese folosind pstree

**tutorial**: dacă vrem doar să vizualizăm anumite atribute cu ps -e -o pid,ppid,%cpu

**exercițiu**: afisarea atributelor pid, ppid, username, comandă completă (cu parametri)

**tutorial**: selectare procese după un anumit atribut (utilizator)

**exercițiu**: selectarea procese după procesul părinte 1

**exercițiu**: selectarea procese care NU aparțin unui utilizator

**tutorial**: putem vedea sortate după atribute (procesor)

**exercițiu**: sortare procese după memorie consumată

Oprirea și suspendarea proceselor. Semnale
------------------------------------------

**tutorial**: fiecare aplicație pornită primește un PID nou
de observat, folosit pidof

**tutorial**: oprirea unor aplicații se face prin semnale
kill

**tutorial**: oprirea mai multor procese (folosind pkill)

**tutorial**: aplicațiile pot fi și suspendate (și apoi continuate: suspend / resume)
Ctrl+z, kill -STOP, kill -CONT

**exercițiu**: pornire sublime, oprire cu kill

**exercițiu**: script care creează un proces care consumă procesor, identificare proces, oprire
ps, sort, kill
