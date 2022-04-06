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

Der Auftraggeber ist bereits im Besitz von funktionsfähigen Ergometern, die er mittels der Software im Bezug auf Handling und Testauswertung verbessern möchte.

## Perspectives
### Who will use the system?

Das System wird von folgenden Personen genutzt: Proband:in, Diagnostiker:in, Ärzt:in, Testaufseher:in sowie der Auftraggeber:in selbst in seinen zukünftigen Ergometern.

### Who can provide input about the system?

Die Daten werden durch die Durchführung eines solchen Leistungstestes zur Verfügung gestellt. Somit liefert hauptsächlich der Proband:in die Daten, und die werden durchs Ergometer grob vorverbearbeitet.

*Hier geht es um Hilfestellung bei Problemen, also beispielsweise um den Softwareentwickler -YS*


## Project Objectives
### Known business rules

Das zu entwickelnde Tool soll als assistierende Unterstützung fungieren, also nicht autonom arbeiten.

*Unter business rules wird der Ablauf beschrieben, in diesem Fall die Verwendung des Programms während dem Leistungstest -YS*

### System information and/or diagrams

Beispiel von aufgezeichneten EKG Daten
![](ekg_example.png)

Aus diesem muss die Herzrate bestimmt werden.

### Assumptions and dependencies

( Anmerkungen von PÜ1: Zum einem ist die Abbrucherkennung bezüglich des Maximalspuls von der Altersangabe des Probanden:in abhängig und die endgültige Gültigkeit des durchgeführten Testes ist weiterhin stark von der Genauigkeit der nachträglichen Datendurchsicht des Diagnostikers:in abhängig.
Weiters wird nach bisher vorliegenden Definition, seitens des Auftragsgebers. die allgemeine Annahme getroffen, dass alle Personen im selben Alter den selben maximalen Puls haben.)

Die Dateien "subject_1", "subject_2" und "subject_3" beinhalten folgende Daten der einzelnen Probanden: ID-Nummer, zu erbringende Leistung, Geburstjahr. Zudem ist auch die Testdauer mit 180 Sekunden, also 3 Minuten, in diesen Dateien erfasst.
Die Dateien "power_data_1" , "power_data_2" und "power_data_3" enthalten die tatsächlich sekündlich erbrachten Leistungen des jeweiligen Probanden.
Die Dateien "ecg_data_subject_1" , "ecg_data_subject_2" und " ecg_data_subject_3" sind die aufgezeichneten EKG-Daten der Probanden. Dabei werden pro Sekunde 1000 Messdaten erfasst (1000Hz- Auflösung).

*Es wäre noch gut die Dateiformate und Einheiten zu erwähnen. -YS*

### Design and implementation constraints

Eine bereits in der Vorgabe gegeben Einschränkung ist,  dass zunächst das Programm lediglich über die Kommandozeile bedient werden soll.

## Risks

Es besteht ein gewisses Risiko im Abbruchkriterium bezüglich des maximalen Pulses, da auch Menschen mit schwachen Herzen und ähnlichem auch solche Tests machen. Denn bei jenen liegt bereits ein gesundheitsgefährender Zustand weit unter dem, aus der angegebenen Formel, berechneten Maximalpuls vor.
Aufgrund der erst nachträglich erfolgten Kontrolle durch die Diagnostiker:in kann es sein, dass ein Proband den Test nochmals bewältigen muss.

*Hier geht es weniger um medizinische Risiken und mehr um Projektrisiken wie beispielsweise eine falsche Datenausgabe -YS*

## Known future enhancements

Entwicklung einer Applikation mit einem UI.
Vor der Durchführung soll eine Abfrage auf Kontraindikationen ausgeführt werden. diese können Folgendes beinhalten:

  - Floride systemische oder kardiale Infektion
  - Instabile Angina pectoris oder Myokardinfarkt
  - Schwere Aortenstenose
  - Schwere Herzinsuffizienz
  - Akute respiratorische Insuffizienz
  - Akute Thrombose der unteren Extremitäten mit oder ohne Lungenembolie

## References

- [Link zur Aufgabenstellung](tbd)

## Open, unresolved or TBD issues

Da bei dem Abbruchkriterium nur ein Beispiel genannt wird, bedarf es des Weiteren noch einer genaueren Definition und Besprechung der automatischen bzw. selbsterkennnenden Abbruchkriterien des Ergometers.
