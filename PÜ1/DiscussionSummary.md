## Project background

Ein Hersteller von Ergometern benötigt eine Leistungsdiagnostik-Software für ein bereits funktionsfähiges Ergometer, welches die gesetzte Leistung, erbrachte Leistung sowie das Elektrokardiogramm der Proband:in aufzeichnet.

### Purpose of project

Dieses Projekt ermöglicht die Automatisierung sowie eine Vereinfachung von Leistungstests. Die Auswertung und Visualisierung basiert auf EKG-Daten und Leistungswerte von Patient:innen.

### Scope of project

Derzeit gibt es nur einen Test-Typ: Ein festes Leistungsziel soll binnen 3 Minuten erreicht werden. Der Puls, die erbrachte Leistung und die Zeit wird von dem Ergometer als sperate Dateien abgespeichert. Derzeit gibt es noch kein UI, dh. die Software wird über eine Kommandozeile bedient. Der Test kann durch folgende Kriterien abgebrochen werden:

  - wenn der Puls 90% der maximalen Herzfrequenz erreicht
  - Abbruch durch den Diagnostiker:in 

Zudem werden Daten der Proband:in, wie Name, User-ID und Geburtsdatum gespeichert.
Aufgezeichnete Plots und deren Daten können abgespeichert werden. Je nach Kriteriumserfüllung werden diese in seperaten Ordner gespeichert.

### Other background information

...

## Perspectives
### Who will use the system?

Proband:in, Diagnostiker:in, Ärzt:in sowie Testaufseher:in.

### Who can provide input about the system?

Die Leistungsdaten, die der/die Proband:in erbringt, werden durch das Ergometer selber aufgezeichnet.

## Project Objectives
### Known business rules
'Definition (später löschen): Weiters können es auch einfach Vorgaben sein, die beschreiben, wie sich ein
Computerprogramm oder Geschäftsprozess, der durch ein Computerprogramm gesteuert wird,
verhalten soll.'

Die einzig bekannte Business Rule kommt bei der angemerkte zukünftigen Erweiterungmöglichkeit: Nutzerinterface soll eine:n Diagnostiker:in durch einen solchen Leistungstest führen. Dies bedeutet für das Programm, dass es nicht komplett autonom funktionieren soll sondern als Wegbereiter/Gehhilfe für den zukünftigen Anwender:in fungieren soll.

### System information and/or diagrams

Beispiel von aufgezeichneten EKG Daten
![](ekg_example.png)

Aus diesem muss die Herzrate bestimmt werden.

### Assumptions and dependencies

...

### Design and implementation constraints

...

## Risks

...

## Known future enhancements

Entwicklung einer Applikation mit einem UI.
Vor der Durchführung soll eine Abfrage auf Kontraindikationen ausgeführt werden. diese können beinhalten:

  - Floride systemische oder kardiale Infektion
  - Instabile Angina pectoris oder Myokardinfarkt
  - Schwere Aortenstenose
  - Schwere Herzinsuffizienz
  - Akute respiratorische Insuffizienz
  - Akute Thrombose der unteren Extremitäten mit oder ohne Lungenembolie

## References

- [Link zur Aufgabenstellung](tbd)

## Open, unresolved or TBD issues

...
