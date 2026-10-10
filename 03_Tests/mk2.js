const {PDFDocument,rgb}=require('pdf-lib');const fk=require('@pdf-lib/fontkit');const fs=require('fs');
(async()=>{const d=await PDFDocument.create();d.registerFontkit(fk);
const f=await d.embedFont(fs.readFileSync('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'),{subset:true});
const p=d.addPage([400,200]);p.drawText('Hallo Welt',{x:40,y:150,size:14,font:f});p.drawText('Zweite Zeile',{x:40,y:110,size:14,font:f});
fs.writeFileSync('../test2.pdf',await d.save());})();
