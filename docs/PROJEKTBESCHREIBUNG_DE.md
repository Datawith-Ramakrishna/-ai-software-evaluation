# KI-Effekt in der Softwareentwicklung – Evaluationskonzept

## Ziel
Entwicklung eines reproduzierbaren Messkonzepts zur vergleichenden Evaluation einer Python-Programmieraufgabe mit und ohne ChatGPT-Unterstützung.

## Umsetzung
- Zwei getrennte Implementierungen mit identischer Schnittstelle und Tests.
- Zeiterfassung für die Bearbeitungsdauer einschließlich KI-Prompts und Fehlerbehebung.
- Automatisierte Testausführung und Coverage-Erfassung mittels pytest und pytest-cov.
- Python-basierte Zusammenführung und Visualisierung der Kennzahlen mit pandas und matplotlib.
- GitHub Actions für automatisierte Tests beider Implementierungen.
- Optionale SonarQube-Cloud-Analyse von Wartbarkeit, Zuverlässigkeit und Sicherheitsbefunden.

## Methodik und Grenzen
Die enthaltenen Beispielimplementierungen dienen ausschließlich der technischen Demonstration. Für die tatsächliche Evaluation müssen eigenständige Implementierungen und reale Messwerte erhoben werden. Die Bearbeitung derselben Aufgabe in zwei Bedingungen kann einen Lerneffekt verursachen. Eine einzelne Pilotmessung erlaubt keine statistisch belastbaren kausalen Schlussfolgerungen.

## Ergebnisse
CSV-Vergleichstabelle, PNG-Diagramm, Testberichte, Coverage-Kennzahlen, optionale SonarQube-Befunde und dokumentierte Versuchsbedingungen.
