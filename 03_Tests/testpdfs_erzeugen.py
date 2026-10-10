from reportlab.lib.pagesizes import A4, landscape
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
import pikepdf, subprocess
# 1 Querformat + Farben + kursiv/fett
c=canvas.Canvas('quer.pdf',pagesize=landscape(A4))
c.setFont('Helvetica-Bold',20); c.drawString(60,520,'Quartalsbericht Querformat')
c.setFont('Helvetica-Oblique',12); c.setFillColor(HexColor('#1a4fa0')); c.drawString(60,490,'Blauer kursiver Untertitel')
c.setFillColor(HexColor('#000000')); c.setFont('Times-Roman',12)
for i in range(6): c.drawString(60,450-i*16,f'Zeile {i+1}: Umsatz im Monat {i+1} betrug {1000+i*37},00 Euro.')
c.setFillColor(HexColor('#2e7d32')); c.rect(500,300,250,40,fill=1,stroke=0); c.setFillColor(HexColor('#ffffff')); c.setFont('Helvetica-Bold',14); c.drawString(510,315,'Weisser Text auf Gruen')
c.save()
# 2 zweispaltig
c=canvas.Canvas('spalten.pdf',pagesize=A4); c.setFont('Helvetica',10)
L='Dies ist ein Beispieltext fuer die linke Spalte und er geht ueber mehrere Zeilen weiter.'.split()
for col,x in ((0,50),(1,310)):
    for i in range(12): c.drawString(x,780-i*13,f'{"Links" if col==0 else "Rechts"} Spalte Zeile {i+1} mit etwas Text')
c.save()
# 3 Seite mit /Rotate 90
c=canvas.Canvas('rot_base.pdf',pagesize=A4); c.setFont('Helvetica',14); c.drawString(72,700,'Diese Seite ist im PDF um 90 Grad gedreht.'); c.drawString(72,680,'Zweite Zeile zum Bearbeiten.'); c.save()
p=pikepdf.open('rot_base.pdf'); p.pages[0].Rotate=90; p.save('gedreht.pdf')
# 4 CropBox verschoben
p=pikepdf.open('rot_base.pdf'); p.pages[0].CropBox=[36,300,560,800]; p.pages[0].MediaBox=[0,0,595,842]; p.save('cropbox.pdf')
# 5 Formular
c=canvas.Canvas('formular.pdf',pagesize=A4); c.setFont('Helvetica',12); c.drawString(72,760,'Antrag: Name'); f=c.acroForm; f.textfield(name='name',x=180,y=752,width=200,height=20,value='Max Muster'); c.drawString(72,720,'Hinweis: Bitte vollstaendig ausfuellen.'); c.save()
# 6 Scan (nur Bild)
from PIL import Image, ImageDraw
im=Image.new('RGB',(1240,1754),'white'); d=ImageDraw.Draw(im); d.text((100,100),'Gescanntes Dokument ohne Text',fill='black'); im.save('scan.pdf')
# 7 gross: 40 Seiten
c=canvas.Canvas('gross.pdf',pagesize=A4)
for pg in range(40):
    c.setFont('Helvetica',11)
    for i in range(45): c.drawString(50,800-i*17,f'Seite {pg+1} Zeile {i+1}: Lorem ipsum dolor sit amet consectetur.')
    c.showPage()
c.save()
