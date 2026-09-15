from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.colors import HexColor, white
from pathlib import Path
from pypdf import PdfReader
import pypdfium2 as pdfium
pdfmetrics.registerFont(TTFont('Arial','C:/Windows/Fonts/arial.ttf'))
pdfmetrics.registerFont(TTFont('Arial-Bold','C:/Windows/Fonts/arialbd.ttf'))
pdfmetrics.registerFontFamily('Arial',normal='Arial',bold='Arial-Bold')
OUT=Path('dist/assets/arbeitsblatt-baum.pdf')
c=canvas.Canvas(str(OUT),pagesize=A4)
c.setTitle('Ökosystem Wald - Wurzel, Stamm und Krone')
c.setAuthor('Wald entdecken')
W,H=A4
ink=HexColor('#163d30'); gray=HexColor('#4b5951'); pale=HexColor('#eaf0e5')
def text(x,y,s,size=11,bold=False,color=ink):
 c.setFillColor(color);c.setFont('Arial-Bold' if bold else 'Arial',size);c.drawString(x*mm,H-y*mm,s)
def para(x,y,s,width,size=10.5):
 p=Paragraph(s,ParagraphStyle('p',fontName='Arial',fontSize=size,leading=size*1.36,textColor=ink))
 aw,ah=p.wrap(width*mm,100*mm);p.drawOn(c,x*mm,H-y*mm-ah);return ah/mm
def line(x,y,w):
 c.setStrokeColor(HexColor('#88988c'));c.setLineWidth(.5);c.line(x*mm,H-y*mm,(x+w)*mm,H-y*mm)
def marker(x,y,n):
 c.setFillColor(white);c.setStrokeColor(ink);c.setLineWidth(1);c.circle(x*mm,H-y*mm,3.4*mm,fill=1,stroke=1)
 c.setFont('Arial-Bold',10);c.setFillColor(ink);c.drawCentredString(x*mm,H-y*mm-3,n)
def image(name,x,y,w,h):
 c.drawImage('dist/assets/'+name+'.png',x*mm,H-(y+h)*mm,w*mm,h*mm,mask='auto',preserveAspectRatio=True,anchor='c')
def header(page):
 text(17,15,'ÖKOSYSTEM WALD',10,True)
 text(17,25,'Wurzel, Stamm und Krone',20,True)
 text(17,35,'Name:',10);line(30,36,73);text(117,35,'Datum:',10);line(133,36,60)
 c.setStrokeColor(ink);c.line(17*mm,H-41*mm,193*mm,H-41*mm)
 text(17,286,'Zum Lernprogramm: Wurzel, Stamm und Krone',8,color=gray)
 text(177,286,str(page)+' / 2',9,color=gray)
def task(y,n,title):
 text(17,y,str(n)+'  '+title,12,True)
header(1)
task(49,1,'Den Baum erkunden')
para(17,53,'Öffne im Lernprogramm die drei Bereiche. Beschrifte A, B und C.',176)
image('baum',22,64,116,77.33)
marker(22+116*.62,64+77.33*.30,'A');marker(22+116*.50,64+77.33*.57,'B');marker(22+116*.57,64+77.33*.79,'C')
for y,l in [(83,'A'),(106,'B'),(129,'C')]:
 text(145,y,l+':',11,True);line(153,y+1,40)
task(154,2,'Den Grundbauplan ergänzen')
para(17,158,'Der Baum besteht aus <b>Wurzeln</b> und dem ___________________________.',176)
para(17,170,'Zum Spross gehören der __________________ und die __________________.',176)
para(17,182,'Die Krone besteht aus _________________, _________________ und Blättern.',176)
task(202,3,'Die Aufgaben festhalten')
para(17,206,'Notiere nach der digitalen Zuordnung jeweils zwei Aufgaben.',176)
# table 176 wide, 16 tall per body row
x=17;y=218;row=17
c.setFillColor(pale);c.rect(x*mm,H-(y+9)*mm,176*mm,9*mm,fill=1,stroke=0)
text(20,224,'Teil des Baumes',10,True);text(64,224,'Zwei Aufgaben',10,True)
for i,label in enumerate(['Wurzeln','Stamm','Laubblätter']):
 top=y+9+i*row
 text(20,top+10,label,10.5,True)
 line(64,top+7,126);line(64,top+14,126)
 c.setStrokeColor(HexColor('#aab8aa'));c.setLineWidth(.5);c.rect(x*mm,H-(top+row)*mm,176*mm,row*mm)
c.line(60*mm,H-y*mm,60*mm,H-(y+9+3*row)*mm)
c.showPage()
header(2)
task(49,4,'Die Wurzel unter der Lupe')
para(17,53,'Bearbeite die Wurzellupe im Lernprogramm. Beschrifte A und B.',176)
image('wurzelspitze',19,65,107,71.33)
marker(19+107*.70,65+71.33*.35,'A');marker(19+107*.50,65+71.33*.85,'B')
text(133,87,'A:',11,True);line(141,88,52)
text(133,112,'B:',11,True);line(141,113,52)
text(17,143,'Viele Wurzelhaare vergrößern die __________________________ der Wurzel.',10.5)
text(17,153,'Dadurch kann sie Wasser und gelöste ______________________ aufnehmen.',10.5)
text(17,165,'Die Wurzelhaube schützt die _______________________________________.',10.5)
task(182,5,'Richtig oder falsch?')
para(17,186,'Kreuze an. Prüfe digital und berichtige die beiden falschen Aussagen darunter.',176,10)
text(166,200,'richtig',9,True);text(183,200,'falsch',9,True)
statements=[
'Die Wurzeln halten den Baum im Boden.',
'Die Borke nimmt Wasser aus dem Boden auf.',
'Der Stamm trägt die Krone und transportiert Stoffe.',
'Zur Krone gehören nur die Blätter.',
'Die Wurzelhaube schützt die empfindliche Wurzelspitze.']
for i,s in enumerate(statements):
 yy=209+i*9;text(17,yy,str(i+1)+'. '+s,9.7)
 c.setStrokeColor(gray)
 for xx in (169,186):c.rect(xx*mm,H-yy*mm,3.2*mm,3.2*mm)
text(17,254,'So lauten die falschen Aussagen richtig:',10,True)
line(17,263,176);line(17,272,176);line(17,280,176)
c.save()
reader=PdfReader(OUT);assert len(reader.pages)==2
assert all(p.extract_text() for p in reader.pages)
Path('tmp/pdfs').mkdir(parents=True,exist_ok=True)
pdf=pdfium.PdfDocument(str(OUT))
for i in range(len(pdf)):
 pdf[i].render(scale=1.4).to_pil().save('tmp/pdfs/arbeitsblatt-baum-'+str(i+1)+'.png')
print('PDF erstellt und gerendert: 2 Seiten.')

