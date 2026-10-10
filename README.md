# LAG|ZERØ PDF Editor

**TESTED. MEASURED. OPTIMIZED.**

Kostenloser PDF-Editor als **eine einzige HTML-Datei**. Läuft komplett offline im Browser, nichts wird hochgeladen. Eine Alternative zu Adobe Acrobat für das Ändern von Text in PDFs.

## Download & Start

**Windows-App (empfohlen):** unter [Releases](https://github.com/sikkkilaci/PDF-Editor/releases/latest) die Datei
`LAGZERO-PDF-Editor-…-portable.exe` laden und doppelklicken – keine Installation nötig.
Beim ersten Start zeigt Windows evtl. „Unbekannter Herausgeber“ → *Weitere Informationen* → *Trotzdem ausführen*.

**Ohne Installation im Browser:** [`01_Programm/LAGZERO-PDF-Editor.html`](01_Programm/LAGZERO-PDF-Editor.html)
herunterladen und doppelklicken (Chrome oder Edge).

PDF öffnen, Text ändern, „PDF speichern“. Das Original bleibt unverändert.

## Funktionen
- **Zeile:** eine Zeile anklicken und ändern
- **Absatz:** ganzen Absatz ändern, wird passend neu umbrochen
- **Text hinzufügen:** an beliebiger Stelle
- Schrift, Größe, Fett/Kursiv, Farbe, Hintergrund/Textmarker werden übernommen
- **Originalschrift aus dem PDF**; fehlen Buchstaben (PDFs enthalten meist nur die benutzten), nimmt der Editor
  eine PC-Schrift, eine eingebaute gleich aussehende Schrift (Carlito ≙ Calibri, Caladea ≙ Cambria, DejaVu)
  oder ergänzt nur die fehlenden Buchstaben
- Tabellen, Spalten, Aufzählungen und gedrehte Seiten werden erkannt

## Grenzen
- Bearbeitungsgeschützte (verschlüsselte) PDFs werden nicht gespeichert.
- Der alte Text wird abgedeckt, nicht aus der Datei entfernt. Nicht zum Schwärzen geeignet.
- Text rutscht nicht nach wie in Word.

## Selbst bauen
```
cd 02_Quellcode
npm i pdfjs-dist@3.11.174 pdf-lib@1.17.1 @pdf-lib/fontkit@1.1.1
python build.py
```
Tests: `03_Tests` (Python + Playwright), Windows-App: `05_Windows-App/BAUEN.md`.

## Lizenzen der Bestandteile
Electron (MIT), pdf.js (Apache-2.0), pdf-lib (MIT), @pdf-lib/fontkit (MIT). Schriften: Carlito und Caladea (SIL OFL 1.1), DejaVu (Bitstream Vera / DejaVu License) – siehe `02_Quellcode/schriften/LIZENZ-*.txt`.

---
Programmiert von **Adem Tasdemir** · Kontakt über [Discord](https://discord.gg/TjRhpfgu2c)
