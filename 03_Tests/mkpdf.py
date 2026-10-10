from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
pdfmetrics.registerFont(TTFont('DejaVu','/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'))
pdfmetrics.registerFont(TTFont('DejaVuB','/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'))
pdfmetrics.registerFont(TTFont('DejaVuSerif','/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf'))
c=canvas.Canvas('test.pdf')
c.setFont('DejaVuB',18); c.drawString(72,760,'Rechnung Nr. 2026-0147')
c.setFont('DejaVu',11); c.drawString(72,730,'Kunde: Max Müller, Würzburg')
c.setFillColorRGB(1,0.93,0.3); c.rect(70,700,250,16,stroke=0,fill=1)
c.setFillColorRGB(0,0,0); c.drawString(72,704,'Betrag: 249,00 EUR (markiert)')
c.setFillColorRGB(0.8,0.1,0.1); c.drawString(72,680,'Zahlbar bis 31.10.2026')
c.setFillColorRGB(0,0,0); c.setFont('DejaVuSerif',10)
para=["Dies ist ein Absatz in einer Serifenschrift, der über mehrere",
"Zeilen läuft. Er dient zum Testen des Absatz-Modus, bei dem der",
"Text beim Speichern neu umbrochen wird. Danach folgt Text darunter."]
for i,l in enumerate(para): c.drawString(72,640-i*14,l)
c.setFont('Helvetica',11); c.drawString(72,580,'Standardschrift Helvetica ohne Einbettung')
c.save()
