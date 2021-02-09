import pathlib
import drawbot_skia.drawbot as db
import datetime

# date
dt = datetime.datetime.today()
name = 'colors_' + dt.strftime("%d%m%Y")

p = pathlib.Path(__file__).parent.absolute()

pw = 802.2
ph = 983.6
u = 5
m = u*4
wdt = 120

h = ph/5
w = pw/2

db.size(pw, ph)

def cross(x, y):
  with db.savedState():
    db.fill(None)
    db.stroke(0)
    db.strokeWidth(1)
    db.translate(x, y)
    # line vertical
    db.line((u*2,0), (u*2,u*4))
    # line horizontale
    db .line((0,u*2), (u*4,u*2))

def c_rect(pos, s):
  x, y = pos
  db.rect(x - s / 2, y - s / 2, s , s)

def grid(xt, yt, nR):
  cell_s = (pw - (m*12)) / nR
  db.translate(xt, yt)
  for x in range(nR):
    for y in range(nR):
      db.stroke(None)
      db.linearGradient(
      (0, 0),                         
      (0, 500),                        
      [(1, 0, 0), (0, 1, 0), (0, 0, 1)],  
      [0, .6, 1]                         
      )
      c_rect((x * cell_s + cell_s / 2, y * cell_s + cell_s/2), cell_s - u)

# text
db.font("Plantin MT Pro", 11)
db.text("Soixante-quatre carrées avec un dégradé.", (m*2, m*3))

# croix
cross(m, m)
cross((pw - m*2), m)
cross(m, (ph - m*2))
cross((pw - m*2), (ph - m*2))

# grid rect
grid(m*6, m*10, 8)



db.saveImage(str(name) + '.jpg')
db.saveImage(str(name) + '.pdf')
#db.saveImage(str(name) + '.svg')

