# LAGZERO PDF Editor – Projektanweisungen

Diesen Text in die **Anweisungen** des claude.ai-Projekts einfügen. Die Ordner `02_Quellcode`, `03_Tests` und `04_Version-1` als **Projektwissen** hochladen. Die fertige Datei aus `01_Programm` ist rund 2,5 MB groß, weil alle Bibliotheken eingebaut sind; sie muss nicht ins Projektwissen.

**Aktueller Stand: Version 2.2 (10.10.2026)** – Schriften-Treue stark verbessert, mit echten PDFs getestet.

GitHub: https://github.com/sikkkilaci/PDF-Editor

## Ziel
Ein kostenloser, offline laufender PDF-Editor als einzelne HTML-Datei, als Alternative zu Adobe Acrobat. Ursprünglich für einen Bekannten von Adem, der Text in einem PDF ändern will, ohne Online-Dienste zu nutzen. Die Formatierung soll so originalgetreu wie möglich erhalten bleiben.

## Festgelegte Anforderungen (aus dem ersten Chat)
- Läuft komplett lokal im Browser (Chrome/Edge empfohlen), keine Uploads, kein Internet nötig.
- Prinzip: Originaltext wird abgedeckt und an derselben Stelle als bearbeitbares Feld mit dem Originaltext geöffnet.
- **Zeilen-Modus:** einzelne Zeile anklicken und ändern.
- **Absatz-Modus:** ganzen Absatz bearbeiten; beim Speichern wird passend zur Absatzbreite und zum Zeilenabstand neu umbrochen. Kein echtes Nachrutschen wie in Word (bewusst akzeptiert).
- **Text hinzufügen:** an beliebiger Stelle neuen Text setzen.
- Schrift, Größe, Stil (fett/kursiv), Farbe, Position und Hintergrund/Textmarker werden erkannt und übernommen.
- Schriften (Reihenfolge ab V2.2):
  1. Originalschrift aus dem PDF, wenn alle Zeichen drin sind.
  2. Gleich aussehende Schrift für die ganze Zeile: eigene Schriftdatei → installierte PC-Schrift (Freigabe wird automatisch angefragt) → **eingebaute freie Schrift** (Carlito = Calibri, Caladea = Cambria, DejaVu Sans/Serif/Sans Mono = echt).
  3. **Mischen:** vorhandene Zeichen in Originalschrift, nur fehlende Zeichen aus der besten Ersatzschrift (Hinweis im Chip, z. B. „nur Q J y fehlen“).
  4. Erst dann ganze Zeile in Helvetica/Times/Courier mit Warnung.
- Design: **LAG|ZERØ** (schwarz/silber/rot, Eyebrow „ʟᴀɢᴢᴇʀᴏ // PDF EDITOR“, Logo „LAG|ZERØ VERIFIED“, Slogan „TESTED. MEASURED. OPTIMIZED.“, Copyright-Zeile wie auf den anderen LAGZERO-Seiten, Vorlage: lagzero-lab/de/nvidia-verstehen.html).
- Nach jedem Speichern Pop-up: „Dieses Programm wurde programmiert von Adem Tasdemir“, Kontakt über Discord, Button + QR-Code zu https://discord.gg/TjRhpfgu2c.
- Downloads zusätzlich immer als ZIP; bei Dateisammlungen ein anklickbares HTML-Inhaltsverzeichnis.

## Technik
- pdf.js 3.11.174 (Anzeige, Textpositionen, Schriftdaten mit `fontExtraProperties`), pdf-lib 1.17.1 (Speichern), @pdf-lib/fontkit 1.1.1 (eingebettete PC-Schriften).
- **Bauen:** im Ordner `02_Quellcode` einmalig `npm i pdfjs-dist@3.11.174 pdf-lib@1.17.1 @pdf-lib/fontkit@1.1.1`, dann `python build.py` → schreibt `01_Programm/LAGZERO-PDF-Editor.html`.
- **Originalschrift:** Der Editor schreibt neuen Text direkt mit der Schrift-Ressource der Seite (`Tf`/`TJ`). Zeichencodes kommen aus der umgekehrten ToUnicode-Tabelle; ob ein Glyph in der eingebetteten Teilschrift existiert, wird über `toFontChar` + fontkit geprüft. Ressource wird über BaseFont **und** Subtype (Type0 ja/nein) gefunden.
- **Fehlende Breiten (neu in 2.1):** Word schreibt bei einfachen Schriften nur Breiten für benutzte Zeichen (Rest = 0). Der Editor berechnet fehlende Breiten (eingebettet: aus der Schrift per fontkit; nicht eingebettet wie Arial/Times/Courier: aus den metrisch gleichen Standardschriften) und trägt sie beim Speichern ins `Widths`-Array ein.
- **Zeilenerkennung (neu in 2.1):** breite Leer-Stücke von pdf.js trennen Spalten/Tabellenzellen; Aufzählungszeichen sind eigene Zeilen und bleiben stehen; Zeilengröße = Größe mit den meisten Zeichen; Leerzeichen am Zeilenanfang zählen nicht.
- **Eingebaute Schriften:** `02_Quellcode/schriften/` (Latin-Teilmenge, ohne Hinting, ~570 KB). `build.py` bettet sie als JSON/Base64 ein. Lizenzen: OFL 1.1 (Carlito, Caladea), Bitstream Vera/DejaVu (siehe `LIZENZ-*.txt`). Fertige HTML: ~3,2 MB.
- Farben: aus einem zweiten Rendern ohne Anmerkungen per Farbhistogramm; Textfarbe = kräftigster Farbton mit genug Pixeln (nicht die grauen Kantenpixel).
- Abdeckung: Rechteck in Hintergrundfarbe, dann neuer Text.
- Verschlüsselte PDFs: Speichern wird mit Hinweis abgebrochen (sonst kaputte Datei). Workaround: in Chrome drucken → „Als PDF speichern“.

## Getestet
**Testdateien (Headless-Chrome + Prüfung der gespeicherten PDFs als Bild):**
- Zeile, Absatz, Text hinzufügen, Rückgängig, Markierung bleibt gelb, rote Schrift bleibt rot.
- Eingebettete Teilschriften (einfach und Type0), fehlendes Zeichen → Warnung + Ersatzschrift, manuelle Schriftdatei.
- Pop-up mit Discord-Button und QR-Code.

**Echte PDFs (10.10.2026):**
- Word-PDF mit nicht eingebettetem Arial (Bewerbung): Zeilen + Absatz in Original-Arial. Fehler „Buchstaben übereinander“ gefunden und behoben.
- Word-PDF mit Calibri-Teilschrift (ComCave-Anleitung): Absatz in Original-Calibri. Fehlen Zeichen in der Teilschrift (z. B. „U“, „c“ in Calibri Bold), wird korrekt gewarnt.
- Telekom-PDF, 58 Seiten, CID-Schriften: lädt in ca. 4 s; Tabellenkopf, Aufzählung, Preistabelle bearbeitet. Fehler „Spalten verschmolzen + Tabellenlinie gelöscht“, „graue statt schwarze Schrift“, „Aufzählungen als ein Absatz“ gefunden und behoben.
- Alle alten Tests danach erneut grün.
- V2.2: Bank-PDF (Volksbank, Schriften GenosGFG + DejaVu Sans Mono, Teilschriften ohne Q/X/j/x/y): vorher ganze Zeile Helvetica (sofort sichtbar), jetzt Brieftext in echter DejaVu Sans Mono und GenosGFG gemischt (nur fehlende Buchstaben in Helvetica). Calibri-Teilschrift → Carlito, optisch gleich. Test nur an einer entschlüsselten Kopie im Testsystem.

## Offen / noch nicht getestet
1. **Automatische PC-Schriftsuche (Local Font Access)** – wird seit V2.2 automatisch angefragt; nur in echtem Chrome/Edge mit Fenster testbar.
2. Firmen-Hausschriften (z. B. GenosGFG, TeleGrotesk): fehlende Buchstaben kommen aus Helvetica – fällt kaum auf, ist aber nicht 100 % gleich. Lösung nur mit der echten Schriftdatei.
3. Bearbeitungsgeschützte (verschlüsselte) PDFs, z. B. von Banken: Speichern wird bewusst abgelehnt.
4. Absatz-Vorschau kann minimal anders umbrechen als das gespeicherte PDF.
5. Gemischte Formatierung innerhalb eines Absatzes (einzelne fette Wörter) geht im Absatz-Modus verloren.
6. Text in Form-XObjects und gedrehter Text werden nicht erkannt.
7. Abdecken entfernt den alten Text nicht aus der Datei (für echtes Schwärzen ungeeignet).
8. Wird ein Absatz kürzer, bleibt darunter eine Lücke (kein Nachrutschen, bewusst akzeptiert).
9. pdf.js meldet „fake worker“ bei file:// – funktioniert, ist aber langsamer bei großen PDFs.

## Arbeitsweise für dieses Projekt
- Änderungen immer in `editor-quelle.html`, dann mit `build.py` bauen.
- Vor jeder Ausgabe: Code-Review + Tests aus `03_Tests` (auch `e2e5_echte_pdfs.py` mit echten PDFs) laufen lassen und das gespeicherte PDF als Bild prüfen.
- Ehrlich sagen, was getestet ist und was nicht.
