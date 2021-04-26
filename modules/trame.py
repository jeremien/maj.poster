import pathlib
import drawbot_skia.drawbot as db
import datetime
import math

# date
dt = datetime.datetime.today()
name = 'trame_' + dt.strftime("%d%m%Y")

p = pathlib.Path(__file__).parent.absolute()

def circle(pt, radius):
  diameter = 2 * radius
  x, y = pt
  db.oval(x - radius, y - radius, diameter, diameter)

pw = 802.2
ph = 983.6
u = 5
m = u*4
pi = math.pi
nCircles = 36
wdt = pw/4

h = ph/3
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
    # cercle
    # db.oval(u, u, u*2, u*2)

def trame(x, y, s, n, w):
  r = 0.97 * w
  step = r / n
  with db.savedState():
    db.fill(None)
    db.stroke(0)
    db.strokeWidth(s)
    db.translate(x, y)
    for i in range(n):
      f = i / (n - 1)
      x = db.sin(2 * pi * 1) * 68 * db.sin(pi * f)
      circle((x, 0), r)
      r -= step

# formes
trame(w, h, 3, nCircles, wdt)
trame(w, h*2, 3, nCircles, wdt)
# trame(w, h*3, 3, nCircles, wdt)
# trame(w, h*4, 4, nCircles, wdt)

# croix
cross(m, m)
cross((pw - m*2), m)
cross(m, (ph - m*2))
cross((pw - m*2), (ph - m*2))

# text
db.font("Plantin MT Pro", 10)
db.text("Trente-six lignes concentriques.", (m*2, m*3))

# db.saveImage(str(name) + '.jpg')
#db.saveImage('trame_01022021.pdf')
db.saveImage(str(name) + '.svg')

