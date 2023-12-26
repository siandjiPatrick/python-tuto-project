# python-tuto-project

## Klausuraufgaben

Die nachfolgenden Aufgaben stammen aus Klausuren früherer Semester. Die hier abge-
fragten Kompetenzen dürften eine hohe Relevanz für die kommende Klausur haben. Aller-
dings ist nicht ausgeschlossen, dass in der Klausur auch andere Themen abgefragt werden. 
Des Weiteren kann der Umfang einzelner Klausurfragen von dem der hier jeweils veröffent-
lichten Fragen abweichen. Dies wird dann jedoch in der Klausur über die Anzahl der zu 
rechnenden Aufgaben kompensiert. Es sei noch angemerkt, dass die hier veröffentlichten 
Aufgaben aus mehreren Klausuren stammen, weshalb Sie vermutlich mehr als 90 min be-
nötigen, um alle Aufgaben zu lösen.

## Funktionen

Gegeben ist die folgende Summenformel:

1. Schreiben Sie in Python zunächst eine Funktion `f (N, M)` in der die Summe berechnet 
wird. Das Ergebnis soll von der Funktion an das aufrufende Programm zurückgegeben 
werden (aber noch nicht von der Funktion auf dem Bildschirm ausgegeben werden).

2. Ergänzen Sie außerdem ein Hauptprogramm, in dem der Benutzer zunächst nach N und 
M gefragt wird. Anschließend soll die Funktion 'f' mit den vom Benutzer eingegebenen 
Werten aufgerufen und das Funktionsergebnis schließlich mit print ausgegeben werden.

Hinweis: Überlegen Sie sich, mit welchen Datentypen hier jeweils gearbeitet werden muss.
 
## Listen

Vorgegeben ist das nachfolgend dargestellte Hauptprogramm:

```python
lst = [1, 24, -32, 0, -13, 9733, -8, 0, 251, 22, 15423, -974563, 123, 310, -145, -793161, 
1154, 2843, 232, -1]
result = cut (lst)
print (result)
```

Erweitern bzw. modifizieren Sie dieses Programm wie folgt:

1. Ergänzen Sie die Funktion "cut". Die Funktion soll die Liste "lst" in drei Teile zerlegen. 
Zunächst muss nach dem ersten Eintrag gesucht werden, der größer als 200 und durch 
2 teilbar ist. Der Eintrag soll in "value" gespeichert werden. Alle Elemente der Liste "lst" 
vor dem gefundenen Eintrag sollen in die Ergebnisliste "head" (ausschließlich "value") 
und alle Elemente hinter dem gefundenen Eintrag sollen in die Ergebnisliste "tail" über-
tragen werden (ebenfalls ausschließlich "value") . Die Funktion "cut" soll ein Tuppel mit 
drei Einträgen zurückgeben, und zwar der Ergebnisliste "head", dem gefundenen Ein-
trag "value" und der Ergebnisliste "tail".

2. Modifizieren Sie das vorgegebene Hauptprogramm so, dass die von der Funktion "cut" 
generierten Teilergebnisse "head", "value" und "tail" jeweils in einer separaten Zeile 
ausgegeben werden. 
Tupel
Gegeben ist das nachfolgend dargestellte Python Hauptprogramm:

```python
a = int (input ('a = '))

b = int (input ('b = '))
c = int (input ('c = '))
result = h (a, b, c)
print (result)
```

Ergänzen Sie die Funktion h(a, b, c). Die Funktion soll ein Tupel mit zwei Werten zurück-
geben. Der erste Wert entspricht der Summe der als Parameter übergebenen Werte in 'a', 
'b' und 'c', der zweite Wert dem Produkt der selben Parameter.

## Dictionaries

Gegeben ist das folgende Dictionary:

```python
d = {'der': 'Artikel', 'die': 'Artikel', 'das': 'Artikel', 'gehen': 'Verb', 'laufen': 'Verb', 
 'schwimmen': 'Verb', 'Hund': 'Substantiv', 'Uni': 'Substantiv', 'Schüler': 'Substantiv', 
 'Klausur': 'Substantiv', 'schön': 'Attribut', 'hässlich': 'Attribut'}
```
 
Führen Sie nacheinander auf diesem Dictionary folgende Aktionen aus:

1. Fragen Sie den Benutzer zunächst nach einem Schlüssel. Wenn sich der Schlüssel im 
Dictionary findet, geben Sie den entsprechenden Wert auf dem Bildschirm aus. Falls 
sich der Schlüssel nicht im Dictionary befindet, fragen Sie den Benutzer nach einem 
Wert. Verwenden Sie anschließend Schlüssel und Wert um einen Eintrag in das Dictio-
nary 'd' zu schreiben und geben Sie zusätzlich die Meldung 'Ein neuer Eintrag wurde in 
d erzeugt!' auf dem Bildschirm aus.

2. Fragen Sie den Benutzer nach einem Wert. Anschließend durchsuchen Sie die Werte 
des Dictionaries nach dem eingegebenen String. Falls Sie den Wert finden, geben Sie 
den Schlüssel und den Wert zum gefundenen Eintrag aus. Falls es mehrere Einträge 
zum gegebenen Wert gibt, sollen alle passenden Einträge ausgegeben werden. Falls es 
keinen passenden Eintrag gibt, muss nichts ausgegeben werden. 

3. Geben Sie alle Einträge des Dictionaries auf dem Bildschirm aus.
Dateizugriffe
Schreiben Sie ein Python-Programm, das den Benutzer zunächst um die Eingabe einer Zahl 
N bittet. Anschließend sollen alle Zahlen von 0 bis N in eine Datei ergebnis.txt ausgegeben 
werden, und zwar so, dass in jeder Zeile der Datei immer genau eine Zahl steht.

## Exceptions

Gegeben ist die nachfolgende unvollständige Funktionsdefinition in Python:

```python
def f ():
z = int (input ('Zahl: ')) # Hier wird bei einer Falscheingabe ein ValueError ausgelöst
txt = input ('Text eingeben: ')
lst = [0, 1, 2]
if z >= 0:
lst[z] = 1/z**2 # Hier wird ein ZeroDivisionError (z=0) oder ...
# ... ein IndexError (z=3) ausgelöst!
else:
?
return lst
```

1. Vervollständigen Sie die Funktion an der mit dem Fragezeichen gekennzeichneten 
Stelle so, dass dort eine Exception vom Typ RuntimeError ausgelöst wird. Als Argument 
der Exception verwenden Sie die in der Variablen 'txt' gespeicherte Zeichenkette.

2. Schreiben Sie ein Hauptprogramm, in dem die zuvor geschriebene Funktion aufgerufen 
und der Rückgabewert auf dem Bildschirm ausgegeben wird. Außerdem sollen im

Hauptprogramm alle Exceptions eingefangen und wie folgt verarbeitet werden:
- Falls eine Exception vom Typ RuntimeError auftritt, soll die mit der Exception 
übergebene Zeichenkette ausgegeben werden.
- Falls eine Exception vom Typ ZeroDivisionError aufgetreten ist, soll die Zeichen-
kette 'Division durch 0' ausgegeben werden.
- Falls irgend eine andere Exception aufgetreten ist, soll die Zeichenkette 'Irgend 
ein Fehler' ausgegeben werden. 
Anmerkung: Sie können vier unterschiedliche Exceptions auslösen, und zwar indem Sie bei 
der Abfrage 'Zahl: '

- keine Zahl eingeben (dies führt zu einem ValueError),
- 0 eingeben (dies führt zu einem ZeroDivisionError),
- 3 eingeben (dies führt zu einem IndexError) oder
- -1 eingeben (dies sollte zu einem RuntimeError führen). 

Falls man eine 1 eingibt, wird keine Exception ausgelöst.

## Klassen und Objekte

Gegeben ist das nachfolgend dargestellte Klassendiagramm:

1. Klasse A soll entsprechend der nachfolgenden Beschreibung programmiert werden:
l: Das private Klassenattribut soll mit einer leeren Liste initialisiert werden.
`__init__ ()`: Der Konstruktor soll so realisiert werden, dass darin die Objektreferenz 'self' 
an das Ende der Liste 'l' angehängt wird.
prtA (): Diese Methode soll für jeden Eintrag in der Liste 'l' die Methode 'prtB' (siehe unten) 
aufrufen.
Klasse B soll von Klasse A erben und entsprechend der nachfolgenden Beschreibung pro-
grammiert werden:
s: Das private Attribut soll einen String speichern. Es soll im Konstruktor entsprechend des 
Parameters initialisiert werden.
newln: Das private Attribut soll eine boolesche Größe speichern. Es soll im Konstruktor ent-
sprechend des Parameters initialisiert werden.

`__init__ (s, newln)': Der Konstruktor soll den Konstruktor der Basisklasse aufrufen. An-
schließend sollen die übergebenen Parameter in den entsprechenden privaten Attributen 
gespeichert werden.
prtB (): Die Methode soll den im privaten Attribut 's' gespeicherten String ausgeben. Falls 
das private Attribut 'newln' gleich False ist, soll die Ausgabe ohne Zeilenwechsel erfolgen. 
Falls 'newln' gleich True ist, soll die Ausgabe mit Zeilenwechsel erfolgen (Hinweis: Norma-
lerweise erzeugt print am Ende einen Zeilenwechsel, der hier unterdrückt werden soll, 
wenn 'newln' gleich False ist).

2. Hauptprogramm ist wie folgt zu implementieren:
Ergänzen Sie ein Hauptprogramm, in dem ein erstes Objekt zur Klasse B mit den Parame-
tern `s = 'Hello '` und newln = False erzeugt wird und ein zweites Objekt zur Klasse B mit 
den Parametern s = 'World' und newln = True. Anschließend soll nacheinander für beide 
Objekte zunächst die Methode prtB aufgerufen werden und anschließend für beide Objekte 
die Methode prtA.

## Comprehensions
Gegeben ist das nachfolgende Python-Programm mit einem Dictionary "strtab", in dem so-
wohl die Schlüssel (key) als auch die Werte (value) in Form von Strings codiert sind. 

```python
strtab = { '-132': '24', '33': '-7', '-263': '-8821', '2': '943', '6623': '803', '1725': '5763', 
'5382': '663', '532': '2553', '744': '54212' }
result = ?
print (result)
```

Modifizieren Sie dieses Programm in folgenden Teilschritten:

1. Ersetzen Sie das Fragezeichen ? durch eine Comprehension. Damit soll ein neues Dic-
tionary erzeugt werden, in dem Schlüssel (key) und Wert (value) nicht mehr vom Typ 
String sondern vom Typ Integer sind. Außerdem sollen mit dem selben Ausdruck nega-
tive Schlüssel (keys) entfernt werden, d.h. die entsprechenden Einträge sollen nicht 
mehr in "result" auftauchen.

2. Modifizieren Sie das Programm so, dass eine Exception vom Typ "RuntimeError" ausge-
worfen wird, wenn "result" leer ist (Hinweis: Sie können die Anzahl der Einträge in 
einem Dictionary mit Hilfe der Funktion "len" ermitteln). 

3. Erweitern Sie das Programm erneut, indem Sie Exceptions aller Art auffangen. Im Falle 
einer Exception soll eine kurze Fehlermeldung auf dem Bildschirm ausgegeben werden 
(Hinweis: Um testweise eine Exception zu provozieren, können Sie den ersten Schlüssel 
in "strtab" durch '-132a' ersetzen).

## Funktionale Programmierung

Gegeben ist das folgende Python Programm:

```python
def filter (lst, fkt):
 for item in lst:
 if fkt (item):
 print (item)
lst = [12, -3, 5, 7, 3, 19, 22, -4, 5, -2, 7, -12, 11, 5, 2, 4, 3, 19, -5, -16]
filter (lst, ?)
```
Ergänzen Sie eine zweite Funktionsdefinition so, dass der Aufruf der ersten Funktion 'filter' 
im vorgegebenen Programm dazu führt, dass nur die negativen Einträge der Liste auf dem

 Bildschirm ausgegeben werden die gleichzeitig durch 4 ohne Rest teilbar sind. Das Frage-
zeichen ist hierbei geeignet zu ersetzen.
Achtung: Die dargestellten Programm-Zeilen dürfen nur an der mit einem Fragezeichen ge-
kennzeichneten Stelle modifiziert sowie um zusätzliche Funktionsdefinitionen erweitert 
werden.
